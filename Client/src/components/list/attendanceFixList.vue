<template>
  <q-list bordered class="rounded-borders" style="max-width: 600px">
    <q-item-label header>{{ header }}</q-item-label>
    <template v-for="item in editedAttendance">
      <q-item v-if="item[0] == attendance" :key="item">
        <q-item-section top>
          <q-item-label lines="1">
            <span class="item-small">{{ item[2] }}</span>
          </q-item-label>
        </q-item-section>
        <q-item-section side>
          <div class="text-grey-8 q-gutter-xs">
            <q-btn
              v-if="attendance == 0 || attendance == 2"
              color="green"
              outlined
              class="gt-xs"
              size="12px"
              flat
              dense
              label="סמן שנכח"
              icon="check"
              @click="markAsAttandant(item)"
            />
            <q-btn
              v-if="attendance == 0 || attendance == 1"
              color="red"
              class="gt-xs"
              size="12px"
              flat
              dense
              label="סמן שלא נכח"
              icon="close"
              @click="markAsUnattandant(item)"
            />
          </div>
        </q-item-section>
      </q-item>
    </template>
  </q-list>
</template>

<script>
import { defineComponent } from "vue";
import { ref, onMounted, onBeforeUnmount } from "vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  name: "attendanceFixList",
  props: ["header", "attendance", "training"],
  setup(props) {
    const loading = ref(false);
    const editedAttendance = ref({});

    function onRequest() {
      loading.value = true;
      setTimeout(() => {
        loading.value = false;
      }, 1500);
    }

    function markAsAttandant(item) {
      item[0] = 1;
      console.log("1!", editedAttendance);
    }

    function markAsUnattandant(item) {
      item[0] = 2;
      console.log("2!", editedAttendance);
    }

    onMounted(() => {
      editedAttendance.value = props.training.attendance_users;

      onRequest({});
    });

    onBeforeUnmount(async () => {
      await axios
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
        .then(function (response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
          console.log(error);
        });
    });

    return {
      loading,
      editedAttendance,
      markAsAttandant,
      markAsUnattandant,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>
