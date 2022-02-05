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
      <!-- 
      <div class="col">
        <h5
        class="row group_header justify-center wrap q-mb-none"
        v-if="everthingIsReady"
      >
        {{ $t("app.confirmation.post") }}
      </h5>
      <editor-posticks
        :trainingData="trainingData"
        :user="currentUser"
        v-if="everthingIsReady">
      </editor-posticks>
    </div> -->
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import DashboardToolbar from "components/DashboardToolbar.vue";
import confirmationPopup from "components/basic/popup/ConfirmationPopup.vue";
import EditorButtons from "components/ClosestTraining/EditorButtons.vue";
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

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
        .catch(function (error) {
          console.log(error);
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
    setDayToLanguage(date) {
      const days = [["Sunday","ראשון"],["Monday","שני"],["Tuesday","שלישי"],["Wednesday","רביעי"],["Thursday","חמישי"],["Friday","שישי"],["Saturday","שבת"]];
      return days[new Date(date).getDay()][0];
      
      //***change to use $t insead */
      // switch (new Date(date).getDay()) {
      //   case 0:
      //     return "ראשון";
      //   case 1:
      //     return "שני";
      //   case 2:
      //     return "שלישי";
      //   case 3:
      //     return "רביעי";
      //   case 4:
      //     return "חמישי";
      //   case 5:
      //     return "שישי";
      //   case 6:
      //     return "שבת";
      //   default:
      //     return this.trainingData.day;
      // }
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
    if (localStorage.getItem("user_lang") == "en-US") {
      this.trainingData.day = this.setDayToLanguage(this.trainingData.date);
    }
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
