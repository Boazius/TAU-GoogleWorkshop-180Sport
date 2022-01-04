<template>
<groups-list v-if="everthingIsReady" :fromTrainer="true" :groups="groups" :user="trainer"></groups-list>
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
    }
  },

  computed: {
    trainer() {
      console.log(this.$store.getters["authentication/getCurrentUser"])
      return this.$store.getters["authentication/getCurrentUser"];
    },
  },
  
  async created() {
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



