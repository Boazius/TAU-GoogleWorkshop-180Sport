<template>
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">
        {{ $t("table.title.volunteers") }}
      </h3>
      <user-table
        v-if="isReady"
        :tableType="4"
        :byUser="false"
        :table_data="volunteers"
      ></user-table>
    </div>
  <relogin-popup v-model="logout"/>
  </q-page>
</template>

<script>
import userTable from "components/table/UserTable.vue";
import axios from "axios";
import ReloginPopup from "components/basic/popup/ReloginPopup.vue";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
export default {
  data() {
    return {
      volunteers: [],
      logout: false,
      isReady: false,
    };
  },
  components: {
    userTable,
    ReloginPopup,
  },

  async created() {
    const id_token = localStorage.getItem("id_token");

    //get volunteers data from server
    const response = await axios
      .get(`${serverUrl}/admin/get_all_volunteers/`, {
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
      this.volunteers = JSON.parse(
        JSON.stringify(response["list of volunteers"])
      );
      this.isReady = true;
      }

  },
};
</script>
