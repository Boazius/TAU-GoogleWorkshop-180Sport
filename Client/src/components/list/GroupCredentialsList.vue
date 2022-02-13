<template>
  <div>
    <section class="item col q-gutter-x-md bg-grey-2 q-pa-md">
      <q-form
        @submit.prevent="formHandler"
        autofocus
        v-if="isReady"
        class="max-width"
      >
        <div
          class="row max-width justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none"
        >
          <p class="q-ma-none q-pb-none">{{ $t("groups.chooseDay") + ":" }}</p>
          <q-select
            v-model="editedGroup.day"
            :options="days.map((day) => (day = $t(day)))"
            emit-value
            map-options
            name="day"
            class="q-pb-md"
          />
        </div>
        <div
          class="row justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none"
        >
          <p class="q-ma-none q-pb-none">{{ $t("groups.chooseTime") + ":" }}</p>
          <q-input
            no-error-icon
            clearable
            lazy-rules
            clear-icon="close"
            label-color="text-grey-1"
            name="time"
            v-model="editedGroup.time"
            type="time"
            :rules="[
              (val) => (val && val.length > 0) || $t('authentication.field'),
            ]"
          />
        </div>
        <div
          class="row justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none"
        >
          <p class="q-ma-none q-pb-none">
            {{ $t("groups.chooseLocation") + ":" }}
          </p>
          <q-input
            no-error-icon
            v-model="editedGroup.meeting_place"
            name="area"
            clearable
            lazy-rules
            clear-icon="close"
            :rules="[
              (val) => (val && val.length > 0) || $t('authentication.field'),
            ]"
            label-color="text-grey-1"
          />
        </div>
        <div
          class="row justify-left q-my-none q-gutter-x-md items-center bg-grey-2 q-pa-none"
        >
          <p class="q-ma-none q-pb-none">
            {{ $t("table.title.trainers") + ":" }}
          </p>
          <q-select
            v-model="trainers"
            map-options
            use-chips
            :options="allTrainers"
            multiple
            :option-label="(item) => item.full_name"
            emit-value
            lazy-rules
            clearable
            clear-icon="close"
            no-error-icon
            :rules="[
              (val) => (val && val.length > 0) || $t('authentication.field'),
            ]"
            class="q-pb-md"
          />
        </div>

        <div class="row q-mt-lg">
          <black-button
            class="q-mt-sm q-mr-md"
            :type="'submit'"
            :loading="loading"
            @click="setGroupInfo"
            color="primary"
            >{{ $t("table.save") }}
            <saved-changes-popup v-model="saved_dialog" :goBack="true" />
            <missing-details-popup v-model="missing_dialog" />
          </black-button>
          <black-button
            class="q-mt-sm"
            color="primary"
            :outline="true"
            @click="onGoBack"
            >{{ $t("table.cancel") }}</black-button
          >
          <q-space></q-space>
          <black-button class="q-mt-sm" v-if="!isNew && isReady" color="red">
            {{ $t("groups.delete") }}
            <q-popup-proxy>
              <q-card>
                <q-card-section class="row items-center">
                  <q-avatar icon="warning" color="red" text-color="white" />
                  <span class="q-ml-sm">
                    {{ $t("groups.deleteMessagePart1") }}
                    <br />
                    {{ $t("groups.deleteMessagePart2") }}
                  </span>
                </q-card-section>
                <q-card-actions align="right">
                  <q-btn
                    flat
                    :label="$t('groups.cancle')"
                    color="primary"
                    v-close-popup
                  />
                  <q-btn
                    flat
                    :label="$t('groups.delete')"
                    color="red"
                    @click="deleteGroup"
                    v-close-popup
                  />
                </q-card-actions>
              </q-card>
            </q-popup-proxy>
            <deleted-popup v-model="deleted_dialog" />
          </black-button>
        </div>
      </q-form>
    </section>
    <relogin-popup v-model="logout" />
  </div>
</template>

<script>
import BlackButton from "components/basic/BlackButton";
import SavedChangesPopup from "components/basic/popup/SavedChangesPopup.vue";
import DeletedPopup from "components/basic/popup/DeletedPopup.vue";
import MissingDetailsPopup from "components/basic/popup/MissingDetailsPopup.vue";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default {
  name: "GroupCredentialsList",
  data() {
    return {
      groupdata: {},
      loading: false,
      editedGroup: {
        day: "",
        time: "",
        meeting_place: "",
      },
      isNew: false,
      isReady: false,
      confirm: false,
      logout: false,
      allTrainers: [],
      originalTrainers: [],
      trainers: [],
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
      saved_dialog: false,
      missing_dialog: false,
      deleted_dialog: false,
    };
  },

  async created() {
    if (JSON.parse(localStorage.getItem("groupId")).id != 0) {
      await this.getGroup();
      await this.getTrainersForGroup();
      this.trainers = this.originalTrainers;
      this.editedGroup.day = this.groupdata.day;
      this.editedGroup.time = this.groupdata.time;
      this.editedGroup.meeting_place = this.groupdata.meeting_place;
    } else this.isNew = true;
    await this.getAllTrainers();
    this.isReady = true;
  },

  methods: {
    onGoBack() {
      this.$router.go(-1);
    },

    formHandler() {},

    async deleteGroup() {
      this.editedGroup = {};
      this.trainers = [];
      await this.getTrainersForGroup();
      for (let i = 0; i < this.originalTrainers.length; i++) {
        this.removeTrainerFromGroup(this.originalTrainers[i].id);
      }
      const response1 = await axios
        .delete(`${serverUrl}/group/${this.groupdata.id}/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
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
        })
        .then((this.deleted_dialog = true));
      if (response1 == "logout") {
        this.logout = true;
      } else localStorage.setItem("groupId", JSON.stringify({ id: 0 }));
    },

    //if !isNew - get group info using get, else return {}
    async getGroup() {
      const id = JSON.parse(localStorage.getItem("groupId")).id;
      if (id != 0) {
        const response1 = await axios
          .get(`${serverUrl}/group/${id}/`, {
            headers: {
              "x-access-token": id_token,
            },
          })
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
        if (response1 == "logout") {
          this.logout = true;
        } else {
          this.groupdata = JSON.parse(JSON.stringify(response1["Group"]));
        }
      } else this.groupdata = {};
    },

    //get group's trainers
    async getTrainersForGroup() {
      const id = JSON.parse(localStorage.getItem("groupId")).id;
      const response = await axios
        .get(`${serverUrl}/get_all_trainers_by_group/${id}/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
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
        this.logout = true;
      } else {
        this.originalTrainers = JSON.parse(
          JSON.stringify(response["trainers"])
        );
      }
    },

    async getAllTrainers() {
      const response = await axios
        .get(`${serverUrl}/admin/get_all_trainers/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
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
        this.logout = true;
      } else {
        this.allTrainers = JSON.parse(
          JSON.stringify(response["list of trainers"])
        );
      }
    },

    async addTrainerToGroup(trainerid, groupid) {
      const response = await axios
        .put(
          `${serverUrl}/add_user_to_group/${groupid}/`,
          JSON.stringify({ user_id: trainerid }),
          {
            headers: {
              "x-access-token": id_token,
              "Content-Type": "application/json",
            },
          }
        )
        .catch(function (error) {
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
      }
    },

    async removeTrainerFromGroup(id) {
      const response = await axios
        .put(
          `${serverUrl}/delete_user_from_group/${this.groupdata.id}/`,
          JSON.stringify({ user_id: id }),
          {
            headers: {
              "x-access-token": id_token,
              "Content-Type": "application/json",
            },
          }
        )
        .catch(function (error) {
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
      }
    },

    //post group info in database (create new)
    async saveNewGroup() {
      if (
        this.editedGroup.meeting_place != "" &&
        this.editedGroup.date != "" &&
        this.editedGroup.day != "" &&
        this.trainers.length != 0
      ) {
        const data = this.editedGroup;
        data.day = this.daysHebrew[this.editedGroup.day];
        const response = await axios
          .post(`${serverUrl}/group`, JSON.stringify(this.editedGroup), {
            headers: {
              "x-access-token": id_token,
              "Content-Type": "application/json",
            },
          })
          .then((res) => res.data)
          .catch(function (error) {
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
        } else {
          const newgroupid = JSON.parse(JSON.stringify(response["group"])).id;
          // add trainers to group
          for (let i = 0; i < this.trainers.length; i++) {
            var trainer = this.trainers[i];
            await this.addTrainerToGroup(trainer.id, newgroupid);
          }
          // await this.createTraining(newgroupid); /* trainings are created automaticlly by server script
          this.saved_dialog = true;
        }
      } else this.missing_dialog = true;
    },

    //put group info in database (update)
    async saveExistingGroup() {
      if (
        this.editedGroup.meeting_place !== "" &&
        this.editedGroup.date !== "" &&
        this.editedGroup.day !== "" &&
        this.trainers.length !== 0
      ) {
        //*** check */
        const data = this.editedGroup;
        data.day = this.daysHebrew[this.editedGroup.day];

        const response = await axios
          .put(
            `${serverUrl}/group/${this.groupdata.id}/`,
            JSON.stringify(this.editedGroup),
            {
              headers: {
                "x-access-token": id_token,
                "Content-Type": "application/json",
              },
            }
          )
          .catch(function (error) {
            console.log(error);
            if (
              error.response.status == 401 &&
              error.response.data.message == "Token is invalid!"
            ) {
              return "logout";
            }
          })
          .then((this.saved_dialog = true));

        if (response == "logout") {
          this.logout = true;
        } else {
          // add trainers to group
          for (let i = 0; i < this.trainers.length; i++) {
            var trainer = this.trainers[i];
            if (!this.originalTrainers.some((el) => el.id == trainer.id)) {
              await this.addTrainerToGroup(trainer.id, this.groupdata.id);
            }
          }
          // remove trainers from group
          for (let i = 0; i < this.originalTrainers.length; i++) {
            var trainer = this.originalTrainers[i];
            if (!this.trainers.some((el) => el.id == trainer.id)) {
              await this.removeTrainerFromGroup(trainer.id);
            }
          }
        }
      } else this.missing_dialog = true;
    },

    //set group's new/updated info using post/put determined by isNew, set to true if came to page using "add group" button
    async setGroupInfo() {
      if (this.isNew) {
        this.saveNewGroup();
      } else {
        this.saveExistingGroup();
      }
    },
  },

  components: {
    BlackButton,
    SavedChangesPopup,
    DeletedPopup,
    ReloginPopup,
    MissingDetailsPopup,
  },
};
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
