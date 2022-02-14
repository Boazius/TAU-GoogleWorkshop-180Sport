<template>
  <div>
    <q-list>
      <div
        :class="' q-mb-sm q-ml-md text-h6 text-bold text-' + colors[attendance]"
        header
      >
        {{ header }}
      </div>
      <div v-for="item in editedAttendance" :key="item">
        <q-item v-if="item[0] == attendance">
          <q-item-section top>
            <q-item-label>
              <span class="item-small">{{ item[2] }}</span>
            </q-item-label>
          </q-item-section>
          <q-item-section side>
            <div class="row text-grey-8">
              <q-btn
                v-if="attendance == 0 || attendance == 2"
                outlined
                class="lt-xs"
                size="12px"
                flat
                dense
                :label="$t('group.markPresent')"
                icon="check"
                @click="markAsAttandant(item)"
              />
              <q-btn
                v-if="attendance == 0 || attendance == 1"
                class="lt-xs"
                size="12px"
                flat
                dense
                :label="$t('group.markNotPresent')"
                icon="close"
                @click="markAsUnattandant(item)"
              />
            </div>
          </q-item-section>
        </q-item>
      </div>
    </q-list>
    <relogin-popup v-model="logout" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { ref, onMounted, onBeforeUnmount } from "vue";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  name: "attendanceFixList",
  props: ["header", "attendance", "training"],
  components: {
    ReloginPopup,
  },
  setup(props) {
    const loading = ref(false);
    const editedAttendance = ref({});
    const colors = ref(["grey-7 ", "green", "red"]);
    const logout = ref(false);

    function onRequest() {
      loading.value = true;
      setTimeout(() => {
        loading.value = false;
      }, 1500);
    }

    async function markAsAttandant(item) {
      item[0] = 1;
      updateAttendance();
    }

    async function markAsUnattandant(item) {
      item[0] = 2;
      updateAttendance();
    }

    onMounted(() => {
      editedAttendance.value = props.training.attendance_users;
      onRequest({});
    });

    onBeforeUnmount(async () => {
      updateAttendance();
    });

    async function updateAttendance() {
      const response = await axios
        .put(
          `${serverUrl}/trainer/update_attendance_list/${props.training.id}/`,
          JSON.stringify({ attendance_users: editedAttendance.value }),
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
        logout.value = true;
      }
    }

    return {
      loading,
      editedAttendance,
      markAsAttandant,
      markAsUnattandant,
      updateAttendance,
      colors,
      logout,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>
