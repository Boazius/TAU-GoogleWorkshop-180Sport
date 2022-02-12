<template>
<div>
  <groups-list
    v-if="isReady"
    :groups="groups"
    :user="user"
    :isReady="isReady"
    :noGroups="noGroups"
  ></groups-list>
  <relogin-popup v-model="logout"/>
</div>
</template>

<script>
import groupsList from "components/list/GroupsList.vue";
import axios from "axios";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
const id_token = localStorage.getItem("id_token");
const serverUrl = "https://server-idhusddnia-ew.a.run.app";

export default {
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
    user() {
      return this.$store.getters["authentication/getCurrentUser"];
    },
  },
  async beforeMount() {

    //get groups data from server
    const response = await axios
      .get(`${serverUrl}/admin/get_all_groups/`, {
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
    if (response.success) {
      this.groups = JSON.parse(JSON.stringify(response["list of group"]));
      if (this.groups.length == 0) this.noGroups = true;
      this.isReady = true;
    } else {
      this.$router.push("/login");
    }
  }
    
  },
};
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
