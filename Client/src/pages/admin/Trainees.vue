<template >
  <q-page>
    <div class="q-pa-md">
      <p>{{trainees}}</p>

      <h3 class="table_header wrap q-mb-none">{{$t('table.title.trainees')}}</h3>
      <user-table  :table_data='trainees'></user-table>
    </div>
  </q-page>
</template>

<script>
import userTable from 'components/table/UserTable.vue';
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token ='eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ5OGY0OWJjNmNhNDU4MWVhZThkZmFkZDQ5NGZjZTEwZWEyM2FhYjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiOTE5NjE5ODQ4MTI3LTBkNWF0YThvaTY0ZzRuZWVzbTd2c3MwY2IzMGV2bnBoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiOTE5NjE5ODQ4MTI3LTBkNWF0YThvaTY0ZzRuZWVzbTd2c3MwY2IzMGV2bnBoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAzNzc3NjcyNDYwNjM0Mjc3MDg5IiwiZW1haWwiOiJkYW5pZWxsZS5yb3Rob2x0ekBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IlZaendmRmZ5a2REVkVzTW1JQ29iOHciLCJub25jZSI6Im9RckZhaGg4YjFkZmRSVkozZThYIiwiaWF0IjoxNjQwNDI1MTg0LCJleHAiOjE2NDA0Mjg3ODR9.Dv6IiGNbvHHwdF14xqQovrNchZ4bkrnqs037PV4Y5SUu9Mxvk9j9TCJhFoRG6YfdYAGF5hb8oCMKQJ5VNlVVkGyg5Wu_m2woDU9uia7sCVXk1nqqLbyG-v-ChhnTy5PK-5c5JinwznJ_D0mMeWI_FGPlthzZUAWJ28C999cBqzXTYfg-FiQ1QJy5OX9cv_fb2z5nG-bjx0PHBs7U2FlQvirDNJbeCeaDVZUDXOGUgVRc94B0Z-Nqp-y_uIHH_Q95S2S3jfmWB7n20LFRQkqR34m1FAsa_oDcn0z1qdRyZbpiEuQbm8DcRNKun6pwaPHJ9hGz711VcdcMxh7IsxxWJg'
export default {
  data(){
    return{
      trainees:[
          {
    id: 7,
    name: "אליהו ענבי",
    phone: "0527766455",
    groups: 3,
    postick: "",
    attendance: 2,
    userType:3

  }
      ],
      // everthingIsReady:false
    }
  },
  components: {
    userTable
    },
  // computed: {
  //   traineesData() {
       
  //     return response;
  //   },
  // },
  // async created() {
  //   //get trainees data from server
  //   const response = await axios.get(`${serverUrl}/admin/get_all_users`,{
  //       headers: { 
  //           'x-access-token': id_token,
  //       },
  //   })
  //   .then((res)=> res.data)
  //   .catch((error)=>{
  //       console.log(error);
  //       return error;
  //   });
    
  //     this.trainees =JSON.parse(JSON.stringify(response["list of users"]));
  //     this.everthingIsReady=true;
  //     console.log(this.everthingIsReady);
  // },
 
}
</script>

