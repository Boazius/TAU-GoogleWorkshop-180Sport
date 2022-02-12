<template>
<div>
  <groups-list
    v-if="isReady"
    :fromTrainer="true"
    :groups="groups"
    :user="trainer"
    :noGroups="noGroups"
  ></groups-list>
  <relogin-popup v-model="logout"/>
</div>
</template>

<script>
import groupsList from "components/list/GroupsList.vue";
import axios from "axios";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default {
  name: "Trainer",
  components: { 
    groupsList,
    ReloginPopup,
    },

  data() {
    return {
      groups: [],
      isReady: false,
      noGroups: false,
      logout:false,
    };
  },

  computed: {
    trainer() {
      return this.$store.getters["authentication/getCurrentUser"];
    },
  },

  async created() {
    //get groups data from server
    const response = await axios
      .get(`${serverUrl}/trainer/groups_list/${this.trainer.id}/`, {
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
        this.logout=true;
      }
    else{
      this.groups = JSON.parse(JSON.stringify(response["trainer groups"]));
      if (this.groups.length == 0) this.noGroups = true;
        this.isReady = true;
        }
  },
};
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
