<template>
  <q-page padding>
    <dashboard-toolbar
      v-if="isReady"
      :isReady="isReady"
      :trainingData="trainingData"
    ></dashboard-toolbar>
    <h3 class="text-h5 text-center group_header" v-if="isReady">
      {{ $t("app.confirmation.areYouComing") }}
    </h3>
    <div class="row justify-center q-gutter-md q-pa-md q-mb-xl" v-if="isReady">
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
        @click="saveSelection(2)"
      >
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
      <editor-buttons
        v-if="isReady"
        :trainingData="trainingData"
        :user="currentUser"
      >
      </editor-buttons>
    </div>
    <relogin-popup v-model="logout" />
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import DashboardToolbar from "components/DashboardToolbar.vue";
import confirmationPopup from "components/basic/popup/ConfirmationPopup.vue";
import EditorButtons from "components/ClosestTraining/EditorButtons.vue";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  name: "Trainee",
  data() {
    return {
      trainingData: {},
      isReady: false,
      logout: false,
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
          if (
            error.response.status == 401 &&
            error.response.data.message == "Token is invalid!"
          ) {
            return "logout";
          }
        });
      if (response == "logout") {
        this.logout = true;
      } else this.dialog = true;
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
        if (
          error.response.status == 401 &&
          error.response.data.message == "Token is invalid!"
        ) {
          return "logout";
        }
        return error;
      });
    if (response == "logout") {
      console.log("logout");
      this.logout = true;
    } else {
      response["training"]["date"] = this.formatDate(
        response["training"]["date"]
      );
    }

    this.trainingData = JSON.parse(JSON.stringify(response["training"]));
    const days = [
      "sunday",
      "monday",
      "tuesday",
      "wednesday",
      "thursday",
      "friday",
      "saturday",
    ];
    this.trainingData.day =
      "trainee.days." + days[new Date(this.trainingData.date).getDay()];
    this.attendance =
      this.trainingData.attendance_users[this.currentUser.id][0];
    this.isReady = true;
  },
  components: {
    DashboardToolbar,
    EditorButtons,
    confirmationPopup,
    ReloginPopup,
  },
});
</script>
