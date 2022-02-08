<template>
  <q-page padding>
    <dashboard-toolbar
      v-if="everthingIsReady"
      :everthingIsReady="everthingIsReady"
      :trainingData="trainingData"
    ></dashboard-toolbar>
    <h3 class="text-h5 text-center group_header" v-if="everthingIsReady">
      {{ $t("app.confirmation.areYouComing") }}
    </h3>
    <div class="row justify-center q-gutter-md q-pa-md q-mb-xl" v-if="everthingIsReady">
      <q-btn
        v-if="attendance != 2"
        size="22px"
        class="q-px-xl q-py-xs"
        color="green"
        :label="$t('app.confirmation.yes')"
        @click="saveSelection(1)"
        >
        <confirmation-popup v-model="dialog"></confirmation-popup>
      </q-btn>
      <q-btn
        v-if="attendance == 2"
        size="22px"
        class="q-px-xl q-py-xs"
        color="grey-6"
        :label="$t('app.confirmation.yes')"
        @click="saveSelection(1)"
        >
        <confirmation-popup v-model="dialog"></confirmation-popup>
      </q-btn>

      <q-btn
        v-if="attendance != 1"
        size="22px"
        class="q-px-xl q-py-xs"
        color="red"
        :label="$t('app.confirmation.no')"
        @click="saveSelection(2)">
        <confirmation-popup v-model="dialog"></confirmation-popup>
      </q-btn>
      <q-btn
        v-if="attendance == 1"
        size="22px"
        class="q-px-xl q-py-xs"
        color="grey-6"
        :label="$t('app.confirmation.no')"
        @click="saveSelection(2)"
         >
        <confirmation-popup v-model="dialog"></confirmation-popup>
      </q-btn>
    </div>
    <q-separator />
    <div>
    <editor-buttons v-if="everthingIsReady" :trainingData="trainingData" :user="currentUser">
    </editor-buttons>
    </div>
  </q-page>
</template>

<script>
import { useI18n } from "vue-i18n";
import { defineComponent } from "vue";
import DashboardToolbar from "components/DashboardToolbar.vue";
import confirmationPopup from "components/basic/popup/ConfirmationPopup.vue";
import EditorButtons from "components/ClosestTraining/EditorButtons.vue";
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");
// import Vue from "vue";

//  axios.interceptors.response.use(
//     function(response){
//       return response;
//     },
//     async function(err){
//       console.log(err.response.status);
//       console.log(err.response.data.message);
//       if (err.response.status== 401 && err.response.data.message == "Token is invalid!"){
//       console.log("logout");
//       await Vue.store.dispatch("authentication/logout");
//             router.push({
//               path: "/login",
//             });
//       console.log("logout");
//       }
//       return err;
//     }        
//   );

export default defineComponent({
  name: "Trainee",
  data() {
    return {
      trainingData: {},
      everthingIsReady: false,
      // user: {},
      attendance: 0,
      dialog: false,
    };
  },
  computed: {
    currentUser() {
      return this.$store.getters["authentication/getCurrentUser"];
    },
  },

  methods: {
    
    async onLogout() {
      console.log("loging out");
        //     await store.dispatch("authentication/logout");
        //     router.push({
        //       path: "/login",
        //     });

    },

    async saveSelection(num) {
      this.attendance = num;
      var data = JSON.stringify({
        attendance: num,
      });
      this.dialog = true
      
      const response = await axios
        .put(
          `${serverUrl}/trainee/update_attendance/${this.currentUser.id}/`,
          data,
          {
            headers: {
              "x-access-token": id_token,
              "Content-Type": "application/json",
            },
          }
        )
        .then(function (response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(async function (error) {
          console.log(error);
          // if (error[response][status]== 401 && error.response.data.message == "Token is invalid!"){
          //   console.log("logout");
          //   await store.dispatch("authentication/logout");
          //   router.push({
          //     path: "/login",
          //   });
          //  console.log("logout");
          //  }

        });

    },




    formatDate(date) {
      var myDate = new Date(date);
      var dd = myDate.getDate();
      var mm = myDate.getMonth() + 1;
      var yyyy = myDate.getFullYear();
      if (dd < 10) {
        dd = "0" + dd;
      }
      if (mm < 10) {
        mm = "0" + mm;
      }
      return yyyy + "-" + mm + "-" + dd;
    },
  },
  async beforeMount() {
    //get next training data from server
    const response = await axios
      .get(
        `${serverUrl}/trainee/get_closest_training/${this.currentUser.id}/`,
        {
          headers: {
            "x-access-token": id_token,
          },
        }
      )
      .then((res) => res.data)
      .catch((error) => {
        console.log(error);
        return error;
      });

    response["training"]["date"] = this.formatDate(
      response["training"]["date"]
    );

    this.trainingData = JSON.parse(JSON.stringify(response["training"]));
    const days = ["sunday","monday","tuesday","wednesday", "thursday","friday","saturday"];
    this.trainingData.day="trainee.days."+days[new Date(this.trainingData.date).getDay()];
    this.attendance = this.trainingData.attendance_users[this.currentUser.id][0];
    this.everthingIsReady = true;
  },
  components: {
    DashboardToolbar,
    EditorButtons,
    confirmationPopup,
  },
});



</script>
