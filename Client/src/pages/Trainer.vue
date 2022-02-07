<template>
  <groups-list
    v-if="isReady"
    :fromTrainer="true"
    :groups="groups"
    :user="trainer"
    :noGroups="noGroups"
  ></groups-list>
</template>

<script>
import groupsList from "components/list/GroupsList.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default {
  name: "Trainer",
  components: { groupsList },
  data() {
    return {
      groups: [],
      isReady: false,
      noGroups: false,
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
        return error;
      });

    this.groups = JSON.parse(JSON.stringify(response["trainer groups"]));
    if (this.groups.length == 0) this.noGroups = true;
    this.isReady = true;
  },
};
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
