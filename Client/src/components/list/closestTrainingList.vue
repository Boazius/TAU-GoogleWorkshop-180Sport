<template>
<q-list bordered class="rounded-borders" style="max-width: 600px" v-if="everthingIsReady">
        <q-separator spaced />
        <training-toolbar :training="training"></training-toolbar>
        <q-item v-for="item in training.attendance_users" :key="item" >
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">{{item[2]}}</span>
            </q-item-label>
          </q-item-section>

          <q-item-section side>
            <div class="column">
            <q-btn dense v-if='(training.notes[item[1]][1] != "") && (training.notes[item[1]][0]==0)' class="bg-white text-primary" flat icon="markunread" size="md" @click=" markAsRead(item[1]); onRequest(); print(5)"/>
            <q-btn dense v-if='((training.notes[item[1]][1] != "") && training.notes[item[1]][0]==1)' class="bg-white text-primary" flat icon="drafts" size="md" color="primary" @click=" read=true" />
           <trainer-recieve-message-popup v-if='training.notes[item[1]][1] != ""' v-model="read" :trainingData="training" :userId="item[1]"/>
           </div>
          </q-item-section>

          <q-item-section side>
            <trainer-get-message-popup :trainingData="training" :userId="item[1]"/>
          </q-item-section>

          <q-item-section side>
          <div class="column">

            <q-chip
            dense
            style='width:60px;'
            class="text-center"
            text-color="white"
            :color="item[0]==0 ? 'grey darken-1': item[0]==1 ? 'green' : 'red' " 
            >
            <div  
 
            class="text-center full-width">
            {{item[0]==0 ? $t('user.unknown'): item[0]==1 ? $t('user.yes') : $t('user.no')}}
            </div>
            </q-chip>
          </div>
          </q-item-section>
        </q-item>
      </q-list>
</template>

<script>
import { defineComponent } from 'vue'
import { ref, onMounted } from "vue";
import axios from "axios";
import TrainingToolbar from '../groups/TrainingToolbar.vue';
import TrainerGetMessagePopup from '../basic/popup/TrainerGetMessagePopup.vue';
import TrainerRecieveMessagePopup from '../basic/popup/TrainerRecieveMessagePopup.vue';
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");


export default defineComponent({
    components: { TrainingToolbar, TrainerGetMessagePopup, TrainerRecieveMessagePopup },
    name:"closestTrainingList",
    props:["group", "user"],
    
   setup(props) {
    const loading = ref(false);
    const training = ref({});
    const everthingIsReady = ref(false);
    const read = ref(false);

    async function onRequest() {
            console.log(2);
      loading.value = true;
      setTimeout(() => {
          loading.value = false;
      }, 1500);

      const response = await axios.get(`${serverUrl}/trainer/get_closest_training/${props.group.id}/`,{
          headers: { 
              'x-access-token': id_token,
          },
      })
      .then((res)=> res.data)
      .catch((error)=>{
          console.log(error);
          return error;
      });
      training.value =JSON.parse(JSON.stringify(response["training"]));
      everthingIsReady.value=true;
      }
    

    onMounted(() => {
       onRequest({ });
    });


    async function markAsRead(userId){
      const response = await axios.put(`${serverUrl}/trainer/update_notes_per_user/${training.value.id}/`,
       JSON.stringify({
      "user_id": userId,
      "mark": 1
     }),
      {
        headers: { 
            'x-access-token': id_token,
            'Content-Type': 'application/json',
        },
      })    
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
      training.value.notes[userId][0]=1;
      read.value=true;
      }
    
  function print(s){
    console.log(s);
  }


    return {
      loading,
      props,
      onRequest,
      everthingIsReady,
      training,
      markAsRead,
      read,
      print
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>