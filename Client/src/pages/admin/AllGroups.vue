<template>
  <groups-list
    v-if="isReady"
    :groups="groups"
    :user="user"
    :isReady="isReady"
    :noGroups="noGroups"
  ></groups-list>
</template>

<script>
import groupsList from "components/list/GroupsList.vue";
import axios from "axios";
const id_token = localStorage.getItem("id_token");
const serverUrl = "http://127.0.0.1:5000";

export default {
  components: { groupsList },
  data() {
    return {
      groups: [],
      isReady: false,
      noGroups: false,
    };
  },

  computed: {
    user() {
      return this.$store.getters["authentication/getCurrentUser"];
    },
  },
  async beforeMount() {
    //   //this.user = localStorage.getItem("user")
    //       const email = "rotholtz@mail.tau.ac.il";

    // const response1 = await axios.get(`${serverUrl}/user/email/${email}`,{
    //       headers: {
    //           'x-access-token ': id_token,
    //       },
    //   })
    //   .then((res)=> res.data)
    //   .catch((error)=>{
    //       console.log(error);
    //       return error;
    //   });
    //   this.user =  JSON.parse(JSON.stringify(response1["user"]));

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
        return error;
      });

    if (response.success) {
      this.groups = JSON.parse(JSON.stringify(response["list of group"]));
      if (this.groups.length == 0) this.noGroups = true;
      this.isReady = true;
    } else {
      this.$router.push("/login");
    }
  },
};
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
