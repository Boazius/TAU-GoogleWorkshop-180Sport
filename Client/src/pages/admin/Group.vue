<template>
  <div class="q-pa-md">
    <div class="column">
      <div class="row items-start">
        <q-btn
          size="sm"
          class="q-mr-md q-mt-md"
          padding="sm"
          glossy
          :ripple="{ center: true }"
          color="primary"
          icon="arrow_forward"
          @click="onGoBack"
        />
        <q-item-section
          class="table_header wrap q-mb-sm"
          style="font-size: xx-large"
          >{{ groupdata.day + " - " + " " + groupdata.meeting_place }}<br />{{
            $t("dashboard.time") + ": " + groupdata.time
          }}
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
          <user-table
            v-if="groupIsReady"
            :fromGroupPage="true"
            :table_data="group"
          ></user-table>
        </q-expansion-item>

        <q-expansion-item
          class="item"
          switch-toggle-side
          expand-separator
          :header-inset-level="1"
          :label="$t('table.title.trainers')"
        >
          <trainer-table
            v-if="trainersIsReady"
            :fromGroupPage="true"
            :table_data="trainers"
          ></trainer-table>
        </q-expansion-item>
      </q-expansion-item>

      <q-expansion-item
        class="item"
        expand-separator
        switch-toggle-side
        :label="$t('group.closest')"
      >
        <closest-training-list
          style="width: 85%; max-width: 100%"
          :group="groupdata"
          :user="user"
          v-if="isReady"
        ></closest-training-list>
      </q-expansion-item>
      <q-expansion-item
        class="item"
        expand-separator
        switch-toggle-side
        :label="$t('group.prior')"
      >
        <last-training-list
          style="width: 85%; max-width: 100%"
          :group="groupdata"
          :user="user"
          v-if="isReady"
        ></last-training-list>
      </q-expansion-item>

      <q-expansion-item
        class="item"
        expand-separator
        switch-toggle-side
        :label="$t('group.history.title')"
      >
        <history-table :trainingHistory="trainingHistory" />
      </q-expansion-item>
    </div>
    <relogin-popup v-model="logout" />
  </div>
</template>
<script>
import { ref, onMounted, computed } from "vue";
import { useStore } from "vuex";

import axios from "axios";

import HistoryTable from "src/components/table/HistoryTable.vue";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
import TrainerTable from "components/table/TrainerTable.vue";
import UserTable from "components/table/UserTable.vue";
import closestTrainingList from "components/list/closestTrainingList.vue";
import lastTrainingList from "components/list/lastTrainingList.vue";

const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

const formatDate = (date) => {
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
};

export default {
  components: {
    UserTable,
    TrainerTable,
    closestTrainingList,
    lastTrainingList,
    ReloginPopup,
    HistoryTable,
  },

  methods: {
    onGoBack() {
      this.$router.go(-1);
    },
  },

  setup() {
    const group = ref({});
    const groupIsReady = ref(false);
    const groupdata = ref({});
    const isReady = ref(false);
    const loading = ref(false);
    const logout = ref(false);
    const store = useStore();
    const trainers = ref({});
    const trainersIsReady = ref(false);
    const user = ref({});
    const trainingHistory = ref([]);
    const currentUser = computed(() => {
      return store.getters["authentication/getCurrentUser"];
    });

    async function getContent(url) {
      const response = await axios
        .get(url, {
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
        logout.value = true;
      }
      return response;
    }

    async function onRequest() {
      const { email } = currentUser.value;

      if (localStorage.getItem("groupdata")) {
        groupdata.value = JSON.parse(localStorage.getItem("groupdata"));
      }
      //get group participants data from server
      const response1 = await getContent(
        `${serverUrl}/get_all_users_by_group/${groupdata.value.id}/`
      );
      group.value = JSON.parse(JSON.stringify(response1["users"]));
      groupIsReady.value = true;

      //get group trainers data from server
      const response2 = await getContent(
        `${serverUrl}/get_all_trainers_by_group/${groupdata.value.id}/`
      );
      trainers.value = JSON.parse(JSON.stringify(response2["trainers"]));
      trainersIsReady.value = true;

      //get user data from server
      const response3 = await getContent(`${serverUrl}/user/email/${email}`);
      user.value = JSON.parse(JSON.stringify(response3["user"]));
      isReady.value = true;
    }

    async function getAllDates() {
      const callServer = async (url) => {
        return await axios
          .get(url, {
            headers: {
              "x-access-token": id_token,
            },
          })
          .then((res) => res.data)
          .catch((error) => {
            console.log(error);
          });
      };

      const getAllTraningsUrl = `${serverUrl}/get_all_dates_by_group/${groupdata.value.id}/`;

      const res1 = await callServer(getAllTraningsUrl);
      if (res1.success && res1.dates.length) {
        let { dates } = res1;
        dates = dates.map((date) => {
          return formatDate(date);
        });

        const doSomethingAsync = async (trainingDate) => {
          const getTrainingByDateUrl = `${serverUrl}/training_by_group_by_date/${trainingDate}/${groupdata.value.id}/`;

          const res = await callServer(getTrainingByDateUrl);
          return res;
        };

        const getAllTrainings = async () => {
          return Promise.all(
            dates.map((trainingDate) => doSomethingAsync(trainingDate))
          );
        };

        return getAllTrainings().then((res) => {
          return res;
        });
      }
    }

    onMounted(async () => {
      await onRequest();
      const result = await getAllDates();

      trainingHistory.value = result
        .filter((training) => {
          if (training.success) {
            return training;
          }
        })
        .map((training) => training.Training);
      console.log(trainingHistory.value);
    });

    return {
      currentUser,
      group,
      groupIsReady,
      groupdata,
      isReady,
      loading,
      logout,
      trainers,
      trainersIsReady,
      user,
      trainingHistory,
    };
  },
};
</script>
<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>
