<template>
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">{{$t('table.title.volunteers')}}</h3>
      <user-table :tableType="4" v-if="everthingIsReady" :byUser="false" :table_data='volunteers'></user-table>
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
      volunteers:[],
      everthingIsReady:false
    }
  },
  components: { 
    userTable
    },

  async created() {
    const id_token = localStorage.getItem("id_token");

    //get volunteers data from server
    const response = await axios.get(`${serverUrl}/admin/get_all_volunteers/`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    
      this.volunteers =JSON.parse(JSON.stringify(response["list of volunteers"]));
      this.everthingIsReady=true;
  },
 };
</script>

