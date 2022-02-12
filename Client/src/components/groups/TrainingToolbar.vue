<template>
  <div>
    <div class="row justify-left q-gutter-x-md items-center q-pa-sm item">
      <div class="q-my-none  items-center row">
        <p class="q-ma-none q-mr-md">{{ $t("dashboard.date") }}</p>
      <q-input class="item q-mr-md" type="date" v-model="editedTraining.date" @change="saved_changes=false; getday()" dense />
      </div>
      <div class="q-my-none  items-center row">
      <p class="q-ma-none q-mr-md">{{ $t("dashboard.day") }}</p>
          <!-- <q-select
          v-model="editedTraining.day"
          disable
          :options="days.map((day) => (day = $t(day)))"
          emit-value
          map-options
          name="day"
          dense
          item-aligned
          class="item"
          @change="updated=true"
        /> -->
      <q-input
        disable
        class="item"
        v-model="editedTraining.day"
        type="day"
        dense
        @change="updated=true"
      />
    </div>
    </div>

    <div class="row justify-left q-gutter-x-md items-center q-pa-sm item">
      <div class="q-my-none  items-center row">
      <p class="q-ma-none q-mr-md">{{ $t("dashboard.time") }}</p>
      <q-input class="item q-mr-md" v-model="editedTraining.time" @change="saved_changes=false" type="time" dense />
    </div>
    <div class="q-my-none items-center row">
      <p class="q-ma-none q-mr-md">{{ $t("dashboard.location") }}</p>
      <q-input
        class="item "
        v-model="editedTraining.meeting_place"
        type="text"
        dense
        item-aligned
        @change="saved_changes=false"
      />
    </div>
    </div>

    <div class="row justify-left q-gutter-x-md items-center q-pa-sm item">
      <p class="q-ma-none">{{ $t("dashboard.trainer") }}</p>
      <q-select
        v-model="trainer"
        :options="trainers"
        :option-label="(item) => item.full_name"
        emit-value
        class="item"
        @change="saved_changes=false"
      />
      <q-space />
      <black-button
        class="q-mt-sm q-mr-md"
        :loading="loading"
        v-if="updated && !saved_changes"
        @click="saveTraining"
        color="primary"
        text-color="white"
        outline
        ripple
        >{{ $t("table.save") }}
      </black-button>
      <saved-changes-popup v-model="saved_dialog" :goBack="false" />
    </div>
  <relogin-popup v-model="logout"/>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import axios from "axios";
import BlackButton from "components/basic/BlackButton.vue";
import SavedChangesPopup from "components/basic/popup/SavedChangesPopup.vue";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  name: "TrainingToolbar",
  props: ["training", "isReady"],
  components: {
    BlackButton,
    SavedChangesPopup,
    ReloginPopup,
  },
  data() {
    return {
      editedTraining: {
        day: this.training.day,
        time: this.training.time,
        meeting_place: this.training.meeting_place,
        date:"",
      },
      trainers: {},
      trainer: {},
      updated: false,
      saved_changes: true,
      saved_dialog: false,
      everythingIsready: false,
      logout:false,
      daysHebrew: {
        ראשון: "ראשון",
        שני: "שני",
        שלישי: "שלישי",
        רביעי: "רביעי",
        חמישי: "חמישי",
        שישי: "שישי",
        שבת: "שבת",
        Sunday: "ראשון",
        Monday: "שני",
        Tuesday: "שלישי",
        Wednesday: "רביעי",
        Thursday: "חמישי",
        Friday: "שישי",
        Saturday: "שבת",
      },
      days: [
        "trainee.days.sunday",
        "trainee.days.monday",
        "trainee.days.tuesday",
        "trainee.days.wednesday",
        "trainee.days.thursday",
        "trainee.days.friday",
        "trainee.days.saturday",
      ],
    };
  },

  computed: {

  },

  methods: {
    //put traning info in database (update)
    async saveTraining() {
      var data = this.editedTraining;
      data.trainers_id = this.trainer.id;
      const response = await axios
        .put(
          `${serverUrl}/training/${this.training.id}/`,
          JSON.stringify(data),
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
        if (error.response.status == 401 && error.response.data.message == "Token is invalid!"){
          return "logout";
        }
      });
    if (response == "logout"){
        this.logout=true;
      }
    else{      
      this.updated = false;
      this.saved_changes = true,
      this.saved_dialog = true;}
    },

    getday(){
    this.editedTraining.day = this.$t(this.days[new Date(this.editedTraining.date).getDay()]);
    },
  },


  

  async beforeMount() {
    const response = await axios
      .get(
        `${serverUrl}/get_all_trainers_by_group/${this.training.group_id}/`,
        {
          headers: {
            "x-access-token": id_token,
          },
        }
      )
      .then((res) => res.data)
      .catch((error) => {
        console.log(error);
        if (error.response.status == 401 && error.response.data.message == "Token is invalid!"){
          return "logout";
        }
        return error;
      });
    if (response == "logout"){
        this.logout=true;
      }
    else{
      if (response.success) {
        this.trainers = JSON.parse(JSON.stringify(response.trainers));
        if (
          this.trainers.find((item) => item.id == this.training.trainers_id[0])
        ) {
          this.trainer = this.trainers.find(
            (item) => item.id == this.training.trainers_id[0]
          );
          this.trainers_id = this.trainer.id;
        }
      }
      var myDate = new Date(this.training.date);
        var dd = myDate.getDate();
        var mm = myDate.getMonth() + 1;
        var yyyy = myDate.getFullYear();
        if (dd < 10) {
          dd = "0" + dd;
        }
        if (mm < 10) {
          mm = "0" + mm;
        }
      this.editedTraining.date = yyyy + "-" + mm + "-" + dd;
}
  },

  updated() {
      this.updated = true;
    },





});
</script>
<style scoped>
@import "assets/groupStyle.css";
</style>
