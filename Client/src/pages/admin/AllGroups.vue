<template>
    <groups-list :groups="groups" :user="user"  :everthingIsReady="everthingIsReady" v-if="everthingIsReady"></groups-list>
</template>

<script>
import groupsList from 'components/list/GroupsList.vue'
const id_token = localStorage.getItem("id_token");
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";

export default {
  components: { groupsList },
  data(){
    return {
      groups: [],
      everthingIsReady: false,
      user:{}
    }
  },
    async beforeMount (){
    //this.user = localStorage.getItem("user")
        const email = "rotholtz@mail.tau.ac.il";

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

    //get groups data from server
    const response = await axios.get(`${serverUrl}/admin/get_all_groups/`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    
    this.groups =JSON.parse(JSON.stringify(response["list of group"]));
    this.everthingIsReady=true;
  },
  }
</script>



<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>

