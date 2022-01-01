<template>
<groups-list v-if="everthingIsReady" fromTrainer="true" :groups="groups" :user="trainer"></groups-list>
</template>

<script>
import groupsList from 'components/list/GroupsList.vue'
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default {
  name: 'Trainer',
  components: { groupsList },
  data(){
    return {
      groups: [],
      everthingIsReady: false,
      trainer:{}
    }
  },
  async created() {
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
    this.trainer =  JSON.parse(JSON.stringify(response1["user"]));

    //get groups data from server
    const response = await axios.get(`${serverUrl}/trainer/groups_list/${this.trainer.id}/`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    
    this.groups =JSON.parse(JSON.stringify(response["trainer groups"]));
    console.log(this.groups)
    this.everthingIsReady=true;
  },
  }
</script>



<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>



