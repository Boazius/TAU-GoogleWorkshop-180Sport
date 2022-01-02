<template>
  <div class="q-pa-md">
    <div class="row">
      <div >
      <q-btn
        size="sm"
        class="q-mr-md q-mt-md"
        padding="sm"
        
        glossy
        ripple="center"
        color="primary"
        icon="arrow_forward"
        @click="onGoBack"
      />
      </div>
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
      >{{groupdata.day+' - '+' '+groupdata.meeting_place}}<br>{{$t('dashboard.time')+': '+ groupdata.time}}
      </q-item-section>
      <q-space />
    </div>
    <q-expansion-item
      class="item"
      switch-toggle-side
      expand-separator
      :label="$t('group.groupDetails')"
    >
      <q-expansion-item
        class="item"
        switch-toggle-side
        expand-separator
        :header-inset-level="1"
        :label="$t('group.groupParticipants')"
      >
      <user-table v-if="groupIsReady" :fromGroupPage="true" :table_data='group'></user-table>
      </q-expansion-item>

      <q-expansion-item
        class="item"
        switch-toggle-side
        expand-separator
        :header-inset-level="1"
        :label="$t('table.title.trainers')"
      >
        <trainer-table v-if="trainersIsReady" fromGroupPage="true" :table_data='trainers'></trainer-table>
        </q-expansion-item>
    </q-expansion-item>

    <q-expansion-item
      class="item"
      expand-separator
      switch-toggle-side
      :label="$t('group.closest')"
    >
    <closest-training-list :group="groupdata" :user="user" v-if="everthingIsReady"></closest-training-list>
    </q-expansion-item>
    <q-expansion-item
      class="item"
      switch-toggle-side
      expand-separator
      :label="$t('group.prior')"
    >
    <last-training-list :group="groupdata" :user="user" v-if="everthingIsReady"></last-training-list>
    </q-expansion-item>
  </div>
</template>
<script>
import { ref, onMounted } from "vue";
import UserTable from 'components/table/UserTable.vue';
import TrainerTable from 'components/table/TrainerTable.vue'
import closestTrainingList from 'components/list/closestTrainingList.vue'
import lastTrainingList from 'components/list/lastTrainingList.vue'
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");



export default {
  components: { UserTable, TrainerTable,closestTrainingList, lastTrainingList},

  methods:{
    onGoBack() {
      this.$router.go(-1);
    }
  },

  setup() {
    const loading = ref(false);
    const groupdata = ref({});
    const group = ref({});
    const trainers = ref({});
    const user = ref({});
    const everthingIsReady = ref(false);
    const groupIsReady = ref(false);
    const trainersIsReady = ref(false);

    async function getContent(url){
      const response = await axios.get(url,{
          headers: { 
              'x-access-token': id_token,
          },
      })
      .then((res)=> res.data)
      .catch((error)=>{
          console.log(error);
          return error;
      });
      return response;
      }



    async function onRequest() {
      const email = "rotholtz@mail.tau.ac.il";
        if(localStorage.getItem("groupdata")){
          groupdata.value = JSON.parse(localStorage.getItem("groupdata"));
          console.log("groupdata", groupdata.value)
    }
    //get group participants data from server
      const response1 = await getContent(`${serverUrl}/get_all_users_by_group/${groupdata.value.id}/`);
      group.value = JSON.parse(JSON.stringify(response1["users"]));
      groupIsReady.value=true;

      //get group trainers data from server
      const response2 = await getContent(`${serverUrl}/get_all_trainers_by_group/${groupdata.value.id}/`);
      trainers.value = JSON.parse(JSON.stringify(response2["trainers"]));
      trainersIsReady.value=true;


      //get user data from server
      const response3 = await getContent(`${serverUrl}/user/email/${email}`);
      user.value = JSON.parse(JSON.stringify(response3["user"]));
      everthingIsReady.value=true;

  }


    onMounted(() => {
       onRequest({ });
    });

    return {
      loading,
      groupdata,
      group,
      trainers,
      user,
      everthingIsReady,
      trainersIsReady,
      groupIsReady,
    };
  },
};
</script>
<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";

</style>