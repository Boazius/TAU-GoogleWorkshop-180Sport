<template >
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">{{$t('table.title.trainees')}}</h3>
      <user-table  :tableType="3" v-if="everthingIsReady" :fromGroupPage="false" :table_data='trainees'></user-table>
    </div>
  </q-page>
</template>

<script>
import userTable from 'components/table/UserTable.vue';
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
export default {
  data(){
    return{
      trainees:[],
      everthingIsReady:false
    }
  },
  components: {
    userTable
    },

  async created() {
    const id_token = localStorage.getItem("id_token");
    //get trainees data from server
    const response = await axios.get(`${serverUrl}/admin/get_all_trainees/`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    this.trainees =JSON.parse(JSON.stringify(response["list of trainees"]));
    this.everthingIsReady=true;
  },
 
};
</script>

