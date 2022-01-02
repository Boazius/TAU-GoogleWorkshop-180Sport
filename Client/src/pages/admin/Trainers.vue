<template>
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">{{$t('table.title.trainers')}}</h3>
      <trainer-table  v-if="everthingIsReady" fromGroupPage="false" :table_data='trainers'></trainer-table>
    </div>
  </q-page>
</template>

<script>
import TrainerTable from 'components/table/TrainerTable.vue';
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";

export default {
   data(){
    return{
      trainers:[],
      everthingIsReady:false
    }
  },
 components: { 
    TrainerTable
    },

    async created() {
    const id_token = localStorage.getItem("id_token");

    //get trainers data from server
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
    
    this.trainers =JSON.parse(JSON.stringify(response["list of trainers"]));
    this.everthingIsReady=true;
  },
 };
 
</script>

