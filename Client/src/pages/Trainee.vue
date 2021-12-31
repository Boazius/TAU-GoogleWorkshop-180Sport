<template>
  <q-page padding>
    <dashboard-toolbar v-if="everthingIsReady" :everthingIsReady="everthingIsReady" :trainingData="trainingData"></dashboard-toolbar>
    <h3 class="text-h5 text-center group_header" v-if="everthingIsReady">{{ $t('app.confirmation.areYouComing') }}</h3>
    <div class="row justify-center q-gutter-md q-pa-md" v-if="everthingIsReady">
       <q-btn v-if="attendance!=2"
      size="22px"
      class="q-px-xl q-py-xs"
      color="green"
      :label="$t('app.confirmation.yes')"
      @click="saveSelection(1)"
    />
    <q-btn v-if="attendance==2"
      size="22px"
      class="q-px-xl q-py-xs"
      color="grey-6"
      :label="$t('app.confirmation.yes')"
      @click="saveSelection(1)"
       
    />

     <q-btn v-if="attendance!=1"
      size="22px"
      class="q-px-xl q-py-xs"
      color="red"

      :label="$t('app.confirmation.no')"
      @click="saveSelection(2)"
       />
      <q-btn v-if="attendance==1"
      size="22px"
      class="q-px-xl q-py-xs"
      color="grey-6"
      :label="$t('app.confirmation.no')"
      @click="saveSelection(2)"
      
       />
    </div>
    <div class="col">
      <h6 class="row group_header justify-center wrap q-mb-none" v-if="everthingIsReady">{{$t('app.confirmation.post')}}</h6>
    <editor-posticks :trainingData="trainingData" :user="user" v-if="everthingIsReady"></editor-posticks>
    </div>

  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import DashboardToolbar from "components/DashboardToolbar.vue";
import EditorPosticks from "../components/basic/EditorPosticks.vue";
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  name: "Trainee",
  data() {
    return {
      trainingData: {},
      everthingIsReady:false,
      user:{},
      attendance: 0,
    };
  },

  methods:{
    async saveSelection(num){
      this.attendance = num
    var data = JSON.stringify({
      "attendance": num
    });
   
    const response = await axios.put(`${serverUrl}/user/${this.user.id}/`,
    data,
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

      alert("תודה רבה, בחירתך נשמרה!")
    },

    formatDate(date){
      var myDate = new Date(date)
      var dd = myDate.getDate(); 
      var mm = myDate.getMonth()+1;
      var yyyy = myDate.getFullYear(); 
      if(dd<10){dd='0'+dd} 
      if(mm<10){mm='0'+mm}; 
      return  yyyy+'-'+mm+'-'+dd
    },
    setDayToLanguage(date){ //***change to use $t insead */
      switch(new Date(date).getDay()) {
        case 0:
          return "ראשון";
        case 1:
          return "שני";
        case 2:
          return "שלישי";
        case 3:
          return "רביעי";
        case 4:
          return "חמישי";
        case 5:
          return "שישי";
        case 6:
          return "שבת";
        default:
          return this.trainingData.day;
    }
  },
},
  async beforeMount (){
    const email = "danielle.rotholtz@gmail.com";
    
    //get user id **** check if saved in local storee and if yes take from there and delete
    const response1 = await axios.get(`${serverUrl}/user/email/${email}`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    this.user =  JSON.parse(JSON.stringify(response1["user"]));

  //get next training data from server
    const response = await axios.get(`${serverUrl}/trainee/get_closest_training/${this.user.id}/`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });

    response["training"]["date"] = this.formatDate(response["training"]["date"]);


    this.trainingData =JSON.parse(JSON.stringify(response["training"]));
    if(localStorage.getItem("user_lang")=="he"){
      this.trainingData.day = this.setDayToLanguage(this.trainingData.date);
    }
    this.attendance = this.user.attendance;
    this.everthingIsReady = true;


  },
  components: {
    DashboardToolbar,
    EditorPosticks,
  },
});
</script>

  
 
