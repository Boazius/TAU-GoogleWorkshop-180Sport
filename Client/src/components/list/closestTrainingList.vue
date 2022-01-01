<template>
<q-list bordered class="rounded-borders" style="max-width: 600px" v-if="everthingIsReady">
        <q-separator spaced />
        <training-toolbar :training="training"></training-toolbar>
        <!-- <q-item v-for="item in attendanceKeysArray" :key="item" >
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">{{(JSON.parse(item))[0]}}</span>
            </q-item-label>
          </q-item-section>

          <q-item-section side>
            <div class="column">
            <q-icon v-if='item.postick != ""' name="message" size="sm" color="primary"/>
            <q-menu icon="message" color="primary">
            <next-training-posticks :postick="training.notes"></next-training-posticks>
            </q-menu >
           </div>
          </q-item-section>
                    <q-item-section side>
          <div class="column">

            <q-chip
            dense
            style='width:60px;'
            class="text-center"
            text-color="white"
            :color="item==0 ? 'grey darken-1': item==1 ? 'green' : 'red' " 
            >
            <div  
 
            class="text-center full-width">
            {{item==0 ? $t('user.unknown'): item==1 ? $t('user.yes') : $t('user.no')}}
            </div>
            </q-chip>
          </div>
          </q-item-section>
        </q-item> -->
      </q-list>
</template>

<script>
import { defineComponent } from 'vue'
import { ref, onMounted } from "vue";
// import NextTrainingPosticks from '../basic/NextTrainingPosticks.vue';
const id_token = localStorage.getItem("id_token");
import axios from "axios";
import TrainingToolbar from '../groups/TrainingToolbar.vue';
const serverUrl = "http://127.0.0.1:5000";

export default defineComponent({
  // components: { NextTrainingPosticks, TrainingToolbar },
    components: { TrainingToolbar },
    name:"closestTrainingList",
    props:["group", "user"],
    
   setup(props) {
    const loading = ref(false);
    const training = ref({});
    const everthingIsReady = ref(false);
    const attendanceKeysArray = ref([]);

    async function onRequest() {
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
      // attendanceKeysArray.value = Object.keys(training.value.attendance_users);
      // console.log(attendanceKeysArray.value);
      // console.log(JSON.parse(attendanceKeysArray.value[0]));
      }
    
  

    onMounted(() => {
       onRequest({ });
    });

    return {
      loading,
      props,
      onRequest,
      everthingIsReady,
      training,
      attendanceKeysArray,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>