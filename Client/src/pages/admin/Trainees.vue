<template>
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">
        {{ $t("table.title.trainees") }}
      </h3>
      <user-table
        v-if="isReady"
        :tableType="3"
        :fromGroupPage="false"
        :table_data="trainees"
      ></user-table>
    </div>
  </q-page>
</template>

<script>
import userTable from "components/table/UserTable.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
export default {
  data() {
    return {
      trainees: [],
      isReady: false,
    };
  },
  components: {
    userTable,
  },

  async created() {
    const id_token = localStorage.getItem("id_token");
    //get trainees data from server
    const response = await axios
      .get(`${serverUrl}/admin/get_all_trainees/`, {
        headers: {
          "x-access-token": id_token,
        },
      })
      .then((res) => res.data)
      .catch((error) => {
        console.log(error);
        return error;
      });
    this.trainees = JSON.parse(JSON.stringify(response["list of trainees"]));
    this.isReady = true;
  },
};
</script>
