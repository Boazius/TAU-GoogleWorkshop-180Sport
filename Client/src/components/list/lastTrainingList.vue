<template>
  <div>
    <q-list
    bordered
    class="rounded-borders bg-grey-1"
      v-if="isReady && !isEmpty">      
      <training-toolbar :training="training" v-if="isReady"></training-toolbar>
            <q-separator spaced />
        <div class="column flex">
      <attendance-fix-list
        v-if="isReady"
        :training="training"
        :header="$t('group.notPresent')"
        :attendance="2"
      ></attendance-fix-list>
            <q-separator spaced />
      <attendance-fix-list
        v-if="isReady"
        :training="training"
        :header="$t('group.present')"
        :attendance="1"
      ></attendance-fix-list>
            <q-separator spaced />

      <attendance-fix-list
        v-if="isReady"
        :training="training"
        :header="$t('group.unknown')"
        :attendance="0"
      ></attendance-fix-list>
            </div>
    </q-list>
    <div class="text-h8 q-ml-xl item2" v-if="isReady && isEmpty">
      {{ $t("group.noTraining") }}
    </div>
  <relogin-popup v-model="logout"/>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { ref, onMounted } from "vue";
import attendanceFixList from "./attendanceFixList.vue";
import TrainingToolbar from "components/groups/TrainingToolbar.vue";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  components: { 
    attendanceFixList, 
    TrainingToolbar,
    ReloginPopup,
   },
  name: "lastTrainingList",
  props: ["group", "user"],

  setup(props) {
    const loading = ref(false);
    const training = ref([]);
    const isReady = ref(false);
    const isEmpty = ref(true);
    const logout = ref(false);

    async function onRequest() {
      loading.value = true;
      setTimeout(() => {
        loading.value = false;
      }, 1500);
      const response = await axios
        .get(`${serverUrl}/trainer/get_last_training/${props.group.id}/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
        .then((res) => res.data)
        .catch((error) => {
          console.log(error);
          if (error.response.status == 401 && error.response.data.message == "Token is invalid!"){
            return "logout";
          }
        return error;
      });
      if (response == "logout"){
        logout.value=true;
      }
      else{
        if (response["training"]) {
          training.value = JSON.parse(JSON.stringify(response["training"]));
          isEmpty.value = false;
        } 
        isReady.value = true;
      }

    }

    onMounted(() => {
      onRequest({});
    });

    return {
      loading,
      training,
      isReady,
      logout,
      isEmpty,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>
