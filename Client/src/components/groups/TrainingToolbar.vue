<template>
  <div >
  <div class="row justify-left q-gutter-x-md items-center  q-pa-sm item" >
    <p class="q-ma-none">{{ $t("dashboard.date") }}</p>
    <q-input  class="item" v-model="date" type="date" dense/>

    <p class="q-ma-none">{{ $t("dashboard.day") }}</p>
    <q-input class="item" v-model="editedTraining.day" type="day" dense/>
  </div>
  
  <div class="row justify-left q-gutter-x-md items-center  q-pa-sm item" >
    <p class="q-ma-none">{{ $t("dashboard.time") }}</p>
    <q-input class="item" v-model="editedTraining.time" type="time" dense/>

    <p class="q-ma-none">{{ $t("dashboard.location") }}</p>
    <q-input class="item" v-model="editedTraining.meeting_place" type="text" dense/>
  </div>

  <div class="row justify-left q-gutter-x-md items-center  q-pa-sm item" >
    <p class="q-ma-none">{{ $t("dashboard.trainer") }}</p>
    <q-select v-model="trainer" :options="trainers" :option-label="(item)=>item.full_name" emit-value 
     class="q-pb-md" />
     <q-space/>
      <black-button
        class="q-mt-sm q-mr-md"
        :loading="loading"
        v-if="updated"
        @click="saveTraining"
        color="primary"
        text-color="white"
        outline
        ripple 
        >{{ $t("table.save") }}</black-button
      >
  </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import axios from "axios";
import BlackButton from "components/basic/BlackButton.vue"
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  name: "TrainingToolbar",
  props: ["training","everthingIsReady"],
  components:{BlackButton},
  data() {
    return {
      editedTraining: {
        day: this.training.day,      
        time: this.training.time,
        meeting_place: this.training.meeting_place,
      },
      trainers:{},
      trainer:{},
      updated : false,
    };
  },

  computed:{
    date(){
      var myDate = new Date(this.training.date)
      var dd = myDate.getDate(); 
      var mm = myDate.getMonth()+1;
      var yyyy = myDate.getFullYear(); 
      if(dd<10){dd='0'+dd} 
      if(mm<10){mm='0'+mm}; 
      return  yyyy+'-'+mm+'-'+dd
    },

  },
   async beforeMount (){
         const response = await axios.get(`${serverUrl}/get_all_trainers_by_group/${this.training.group_id}/`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });

    this.trainers = JSON.parse(JSON.stringify(response["trainers"]));
    if (this.trainers.find(item => item.id == this.training.trainers_id[0])){
      this.trainer = this.trainers.find(item => item.id == this.training.trainers_id[0]);
      this.trainers_id=this.trainer.id;
    }
      },

  
  updated(){
    this.updated = true;
  },

  methods:{
    //put traning info in database (update)
   async saveTraining(){
      var data = this.editedTraining;
      data = Object.assign({date:this.date});
      data = Object.assign({trainers_id : this.trainer.id});
            
      const response = await axios.put(`${serverUrl}/training/${this.training.id}/`,
      JSON.stringify(data),
      {
          headers: { 
              'x-access-token': id_token,
              'Content-Type': 'application/json',
          },
      })    .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
        alert("השינויים נשמרו");
        this.updated=false;
      },
  },
});
</script>
<style scoped>
@import "assets/groupStyle.css";
</style>