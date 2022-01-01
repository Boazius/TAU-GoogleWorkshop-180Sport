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
      <div class="row">
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
    };
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

    //post group info in database (create new)
    async saveNewGroup(){
      console.log("new");
      const response = await axios.post(`${serverUrl}/group`,
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
        alert("הקבוצה החדשה נשמרה");
      this.$router.go(-1);
      },
    
  //put group info in database (update)
   async saveExistingGroup(){
      console.log("exist");
            console.log(JSON.stringify(this.editedGroup))

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
        alert("השינויים נשמרו");
      this.$router.go(-1);
      },

//set group's new/updated info using post/put determined by isNew, set to true if came to page using "add group" button
    async setGroupInfo(){
      console.log("set");
      if(this.isNew) {
        this.saveNewGroup();
      }
      else  this.saveExistingGroup();
    },

  },


  async created() {
    if ((JSON.parse(localStorage.getItem("groupId")).id) != 0) {
      await this.getGroup()
      this.editedGroup.day = this.groupdata.day;
      this.editedGroup.time = this.groupdata.time;
      this.editedGroup.meeting_place = this.groupdata.meeting_place;
    }
    else this.isNew=true;
    this.everthingIsReady = true;
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
