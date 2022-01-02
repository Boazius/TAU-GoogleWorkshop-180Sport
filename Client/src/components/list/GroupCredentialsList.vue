<template>
  <section class=" item col q-gutter-x-md bg-grey-2  q-pa-md">
    <!-- Edited data: {{ editedGroup }} <br />
    Group data: {{ groupdata }} -->
    <q-form @submit.prevent="formHandler" autofocus v-if="everthingIsReady" class="max-width">
      <div class="row max-width justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none">
        <p class="q-ma-none q-pb-none">{{ $t('groups.chooseDay')+":" }}</p>
        <q-input
          no-error-icon
          v-model="editedGroup.day"
          name="day"
          clearable
          lazy-rules
          clear-icon="close"
          :rules="[
            (val) => (val && val.length > 0) || $t('authentication.field'),
          ]"
          label-color="text-grey-1"
        />
      </div>
      <div class="row justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none">
        <p class="q-ma-none q-pb-none">{{ $t('groups.chooseTime')+":" }}</p>
        <q-input 
        no-error-icon
        clearable  
        lazy-rules
        clear-icon="close"
        label-color="text-grey-1"
        name="time"
        v-model="editedGroup.time"         
        type="time"
        :rules="[
            (val) => (val && val.length > 0) || $t('authentication.field'),
          ]"/>
      </div>
      <div class="row justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none">
        <p class="q-ma-none q-pb-none">{{ $t('groups.chooseLocation')+":" }}</p>
      <q-input
        no-error-icon
        v-model="editedGroup.meeting_place"
        name="area"
        clearable
        lazy-rules
        clear-icon="close"
        :rules="[
          (val) => (val && val.length > 0) || $t('authentication.field'),
        ]"
        label-color="text-grey-1"
      />
        </div>
       <div class="row justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none">
        <p class="q-ma-none q-pb-none">{{ $t("table.title.trainers")+":" }}</p>
    <q-select v-model="trainers" 
      map-options  
      use-chips
     :options="allTrainers" multiple :option-label="(item)=>item.full_name" emit-value 
      lazy-rules clearable clear-icon="close"
      no-error-icon           
      :rules="[
      (val) => (val && val.length > 0) || $t('authentication.field'),
      ]"
     class="q-pb-md" />
      </div>

      <div class="row q-mt-lg">
      <black-button
        class="q-mt-sm q-mr-md"
        :type="'submit'"
        :loading="loading"
        @click="setGroupInfo"
        color="primary"
        >{{ $t("table.save") }}</black-button
      >
      <black-button class="q-mt-sm " color="primary" :outline="true" @click="onGoBack">{{
        $t("table.cancel")
      }}</black-button>
      <q-space></q-space>
      <black-button class="q-mt-sm " v-if="(!isNew)&&everthingIsReady" color="red"  >
        {{$t("groups.delete")}}
      <q-popup-proxy>
        <q-card >
          <q-card-section class="row items-center">
            <q-avatar icon="warning" color="red" text-color="white" />
            <span class="q-ml-sm">
              {{$t('groups.deleteMessagePart1')}}
              <br/>
              {{$t('groups.deleteMessagePart2')}}
            </span>
          </q-card-section>
        <q-card-actions align="right">
          <q-btn flat :label="$t('groups.cancle')" color="primary" v-close-popup />
          <q-btn flat :label="$t('groups.delete')" color="red" @click="deleteGroup" v-close-popup />
        </q-card-actions>
      </q-card>
      </q-popup-proxy>
        </black-button>
      </div>
    </q-form>
  </section>
</template>

<script>
import BlackButton from "components/basic/BlackButton";
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default {
  name: "GroupCredentialsList",
  data() {
    return {
      groupdata:{},
      loading: false,
      editedGroup: {
        day: "",
        time: "",
        meeting_place: "",
      },
      isNew:false,
      everthingIsReady:false,
      confirm:false,
      allTrainers:[],
      originalTrainers:[],
      trainers:[],
    };
  },



  async created() {
    console.log((JSON.parse(localStorage.getItem("groupId")).id));
    console.log((JSON.parse(localStorage.getItem("groupId")).id) != 0);
    if ((JSON.parse(localStorage.getItem("groupId")).id) != 0) {
      await this.getGroup()
      await this.getTrainersForGroup()
      this.editedGroup.day = this.groupdata.day;
      this.editedGroup.time = this.groupdata.time;
      this.editedGroup.meeting_place = this.groupdata.meeting_place;
    }
    else this.isNew=true;
    await this.getAllTrainers()
    this.everthingIsReady = true;
    
  },


  methods: {
    onGoBack() {
      this.$router.go(-1);
    },



    formHandler() {},
    


    async deleteGroup(){
      localStorage.setItem('groupId', JSON.stringify({id:0}));
      this.editedGroup = {};      
      const response1 = await axios.delete(`${serverUrl}/group/${this.groupdata.id}/`,{
      headers: { 
          'x-access-token': id_token,
      },
      })
      .then((res)=> res.data)
      .catch((error)=>{
          console.log(error);
          return error;
      });
      alert("הקבוצה נמחקה");
      this.$router.go(-1);
    },



    //if !isNew - get group info using get, else return {}
    async getGroup(){
      const id = (JSON.parse(localStorage.getItem("groupId"))).id ;
      if(id != 0){
        const response1 = await axios.get(`${serverUrl}/group/${id}/`,{
        headers: { 
            'x-access-token': id_token,
        },
        })
        .then((res)=> res.data)
        .catch((error)=>{
            console.log(error);
            return error;
        });
        this.groupdata =  JSON.parse(JSON.stringify(response1["Group"]));
      }
      else this.groupdata =  {};
    },



    //get group's trainers
    async getTrainersForGroup(){
      const id = (JSON.parse(localStorage.getItem("groupId"))).id ;
      const response = await axios.get(`${serverUrl}/get_all_trainers_by_group/${id}/`,{
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
      this.originalTrainers = JSON.parse(JSON.stringify(response["trainers"]));
      },



      async getAllTrainers(){
        const response = await axios.get(`${serverUrl}/admin/get_all_trainers/`,{
        headers: { 
            'x-access-token': id_token,
        },
        })
        .then((res)=> res.data)
        .catch((error)=>{
            console.log(error);
            return error;
        });
        this.allTrainers =JSON.parse(JSON.stringify(response["list of trainers"]));
      },

    

    async addTrainerToGroup(trainerid,groupid){
      const response = await axios.put(`${serverUrl}/add_user_to_group/${groupid}/`,
      JSON.stringify({user_id:trainerid}),
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
    },



    async removeTrainerFromGroup(id){
      const response = await axios.put(`${serverUrl}/delete_user_from_group/${this.groupdata.id}/`,
      JSON.stringify({user_id:id}),
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
    },
    


    //post group info in database (create new)
    async saveNewGroup(){
      console.log("new");
      if (this.editedGroup.meeting_place != "" && this.editedGroup.date != "" && this.editedGroup.day != "" && this.trainers != []){
        const response = await axios.post(`${serverUrl}/group`,
        JSON.stringify(this.editedGroup),
      {
          headers: { 
              'x-access-token': id_token,
              'Content-Type': 'application/json',
          },
      }).then((res)=> res.data)   
      .catch(function (error) {
        console.log(error);
      });
      const newgroupid = (JSON.parse(JSON.stringify(response["group"]))).id;
      // add trainers to group
      for (let i = 0; i <  this.trainers.length; i++){
        var trainer = this.trainers[i];
        await this.addTrainerToGroup(trainer.id, newgroupid);
      }

      alert("הקבוצה החדשה נשמרה");
      this.$router.go(-1);
      }
      else alert("לא ניתן לשמור את הקבוצה מכיוון שיש פרטים חסרים");
      },
    


  //put group info in database (update)
   async saveExistingGroup(){
      console.log("exist");

    if (this.editedGroup.meeting_place != "" && this.editedGroup.date != "" && this.editedGroup.day != "" && this.trainers != []){
      const response = await axios.put(`${serverUrl}/group/${this.groupdata.id}/`,
      JSON.stringify(this.editedGroup),
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

      // add trainers to group 
      for (let i = 0; i <  this.trainers.length; i++){
        var trainer = this.trainers[i];
        if (! this.originalTrainers.some(el=> el.id == trainer.id )){
          await this.addTrainerToGroup(trainer.id, this.groupdata.id);
        }
      }
      // remove trainers from group 
      for (let i = 0; i <  this.originalTrainers.length; i++){
        var trainer = this.originalTrainers[i];
        if (!  this.trainers.some(el=> el.id == trainer.id )){
          await this.removeTrainerFromGroup(trainer.id);
        }
      }
     alert("השינויים נשמרו");
      this.$router.go(-1);
      }
      else alert("לא ניתן לעדכן את השינויים מכיוון שיש פרטים חסרים");
      },



//set group's new/updated info using post/put determined by isNew, set to true if came to page using "add group" button
    async setGroupInfo(){
      console.log("set");
      console.log("is new",this.isNew);
      if(this.isNew) {
        this.saveNewGroup();
      }
      else  this.saveExistingGroup();
    },

  },



  // unmounted() {
  //   this.$store.dispatch("authentication/setEditedUser", {});
  // },
  components: {
    BlackButton,
  },
};
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
