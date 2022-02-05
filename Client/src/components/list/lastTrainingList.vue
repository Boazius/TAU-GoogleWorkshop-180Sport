<template>
<div>
    <q-list bordered v-if="everthingIsReady&&!isEmpty" class="rounded-borders" style="max-width: 600px">
        <q-separator spaced />
        <training-toolbar :training="training" v-if="everthingIsReady"></training-toolbar>
        <attendance-fix-list v-if="everthingIsReady" :training="training" :header="$t('group.notPresent')" :attendance="2"></attendance-fix-list>
        <attendance-fix-list v-if="everthingIsReady" :training="training" :header="$t('group.present')" :attendance="1"></attendance-fix-list>
        <attendance-fix-list v-if="everthingIsReady" :training="training" :header="$t('group.unknown')" :attendance="0"></attendance-fix-list>       
    </q-list>
    <div class="text-h8 q-ml-xl item2" v-if="everthingIsReady&&isEmpty ">
      {{ $t('group.noTraining') }}
    </div>
</div>
</template>

<script>
import { defineComponent } from 'vue'
import { ref, onMounted } from "vue";
import attendanceFixList from './attendanceFixList.vue';
import TrainingToolbar from 'components/groups/TrainingToolbar.vue';
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  components: { attendanceFixList ,TrainingToolbar},
    name:"lastTrainingList",
    props:["group", "user"],

   setup(props) {
    const loading = ref(false);
    const training = ref([]);
    const everthingIsReady = ref(false);
    const isEmpty = ref(true);



    async function onRequest() {
      loading.value = true;
      setTimeout(() => {
          loading.value = false;
      }, 1500);
      const response = await axios.get(`${serverUrl}/trainer/get_last_training/${props.group.id}/`,{
          headers: { 
              'x-access-token': id_token,
          },
      })
      .then((res)=> res.data)
      .catch((error)=>{
          console.log(error);
          console.log("sdfsdfsdfsdfsdf");
          return error;
      });
      if(response["training"]){
        training.value =JSON.parse(JSON.stringify(response["training"]));
        isEmpty.value=false;
      }
      else if(response["message"] == "no training found"){
        console.log("no training found");
      }
      everthingIsReady.value=true;   
    }
    
    onMounted(() => {
       onRequest({ });
    });

    return {
      loading,
      training,
      everthingIsReady,
      isEmpty,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>