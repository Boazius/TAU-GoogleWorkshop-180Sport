<template>
  <section class="col q-gutter-x-md bg-grey-2 q-pa-md">
    <q-form
      @submit.prevent="formHandler"
      v-if="isReady"
      autofocus
      class="max-width"
    >
      <q-input
        no-error-icon
        v-model="editedUser.full_name"
        name="name"
        clearable
        lazy-rules
        clear-icon="close"
        :label="$t('table.name')"
        :rules="[
          (val) => (val && val.length > 0) || $t('authentication.field'),
        ]"
        label-color="text-grey-1"
      />
      <q-input
        v-if="!isNew"
        disable
        no-error-icon
        v-model="editedUser.email"
        ref="email"
        name="email"
        type="email"
        lazy-rules
        :label="$t('authentication.email')"
        label-color="text-grey-1"
        :rules="emailRules"
      />
      <q-input
        v-if="isNew"
        no-error-icon
        v-model="editedUser.email"
        ref="email"
        name="email"
        type="email"
        lazy-rules
        :label="$t('authentication.email')"
        label-color="text-grey-1"
        :rules="emailRules"
      />
      <q-input
        no-error-icon
        v-model="editedUser.phone_number"
        name="phone"
        type="tel"
        clearable
        clear-icon="close"
        lazy-rules
        mask="###-#######"
        :label="$t('table.phone')"
        :rules="[
          (val) => (val && val.length > 9) || $t('authentication.field'),
        ]"
        label-color="text-grey-1"
      />

      <q-list class="q-ma-none q-pa-none" v-if="!fromAdmin">
        <q-item-label header>{{ $t("table.groups") }}</q-item-label>
        <q-separator />
        <q-item v-for="item in editedUserGroups" :key="item">
          <q-item-section>
            {{ item.day + "- " + item.meeting_place + " " + item.time }}
            <q-separator />
          </q-item-section>
        </q-item>
      </q-list>
      <q-select
        v-if="fromAdmin"
        v-model="editedUserGroups"
        :options="allGroups"
        emit-value
        map-options
        use-chips
        multiple
        :option-label="
          (item) => item.day + '- ' + item.meeting_place + ' ' + item.time
        "
        :label="$t('table.groups')"
        class="q-pb-md"
      />

      <q-select
        v-if="fromAdmin"
        v-model="editedUserType"
        :options="allUserTypes"
        emit-value
        map-options
        :option-label="(item) => $t(item.label)"
        :label="$t('userPage.userType')"
        class="q-pb-md"
      />

      <div class="row q-mt-lg">
        <black-button
          class="q-mt-sm q-mr-md"
          :type="'submit'"
          :loading="loading"
          color="primary"
          @click="setUserInfo"
          >{{ $t("table.save") }}
          <saved-changes-popup v-model="saved_dialog" :goBack="fromAdmin" />
          <missing-details-popup v-model="missing_dialog" />
        </black-button>
        <black-button
          class="q-mt-sm"
          :outline="true"
          @click="onGoBack"
          color="primary"
          >{{ $t("table.cancel") }}</black-button
        >
        <q-space></q-space>
        <black-button
          class="q-mt-sm"
          v-if="!isNew && isReady && fromAdmin"
          color="red"
        >
          {{ $t("groups.delete") }}
          <q-popup-proxy>
            <q-card>
              <q-card-section class="row items-center">
                <q-avatar icon="warning" color="red" text-color="white" />
                <span class="q-ml-sm">
                  {{ $t("groups.deleteMessagePart1") }}
                  <br />
                  {{ $t("groups.deleteMessagePart2") }}
                </span>
              </q-card-section>
              <q-card-actions align="right">
                <q-btn
                  flat
                  :label="$t('groups.cancle')"
                  color="primary"
                  v-close-popup
                />
                <q-btn
                  flat
                  :label="$t('groups.delete')"
                  color="red"
                  @click="deleteUser"
                  v-close-popup
                />
              </q-card-actions>
            </q-card>
          </q-popup-proxy>
          <deleted-popup v-model="deleted_dialog" />
        </black-button>
      </div>
    </q-form>
  </section>
</template>

<script>
import BlackButton from "components/basic/BlackButton";
import SavedChangesPopup from "components/basic/popup/SavedChangesPopup.vue";
import DeletedPopup from "components/basic/popup/DeletedPopup.vue";
import MissingDetailsPopup from "components/basic/popup/MissingDetailsPopup.vue";
import axios from "axios";
const serverUrl = "https://server-idhusddnia-ew.a.run.app";
const id_token = localStorage.getItem("id_token");

export default {
  name: "UserCredentialsList",
  props: ["fromAdmin", "userDataFrom"],
  data() {
    return {
      loading: false,
      isNew: false,
      userData: {},
      editedUser: {
        full_name: "",
        email: "",
        phone_number: "",
        user_type: 0,
      },
      isReady: false,
      editedUserGroups: [],
      editedUserType: {},
      emailRules: [
        (email) => !!email || this.$t("authentication.email1"),
        (email) => /.+@.+\..+/.test(email) || this.$t("authentication.email2"),
      ],
      userOriginalGroupIds: [],
      allGroups: [],
      allUserTypes: [
        { type: 1, label: "userPage.types.admin" },
        { type: 2, label: "userPage.types.trainer" },
        { type: 3, label: "userPage.types.trainee" },
        { type: 4, label: "userPage.types.volunteer" },
      ],
      saved_dialog: false,
      missing_dialog: false,
      deleted_dialog: false,
    };
  },

  async created() {
    this.user = JSON.parse(localStorage.getItem("user"));
    if (this.fromAdmin) {
      await this.getAllGroups();
      if (this.user.id != 0) {
        await this.getUser();
        this.editedUser = this.userData;
        if (this.userData.group_ids != null) {
          this.userOriginalGroupIds = this.userData.group_ids.split(/,/);
          for (let i = 0; i < this.userOriginalGroupIds.length; i++) {
            var groupid = parseInt(this.userOriginalGroupIds[i]);
            console.log(groupid);
            for (let i = 0; i < this.allGroups.length; i++) {
              var group = this.allGroups[i];
              if (group.id == groupid) {
                this.editedUserGroups.push(group);
              }
            }
          }
        }
        this.editedUserType = this.allUserTypes[this.editedUser.user_type - 1];
      } else {
        this.editedUserType = this.allUserTypes[this.user.type - 1];
        this.isNew = true;
      }
    } else {
      await this.getUser();
      this.editedUser = this.userData;
      if (this.editedUser.group_ids) {
        const group_id_array = this.editedUser.group_ids.split(/,/);
        for (let i = 0; i < group_id_array.length; i++) {
          this.editedUserGroups.push(await this.getGroup(group_id_array[i]));
        }
      }
    }
    this.isReady = true;
  },

  methods: {
    onGoBack() {
      const storeuser = { id: 0 };
      localStorage.setItem("user", JSON.stringify(storeuser));
      this.$router.go(-1);
    },

    formHandler() {},

    //get groups data from server
    async getAllGroups() {
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
      this.allGroups = JSON.parse(JSON.stringify(response["list of group"]));
    },

    async getUser() {
      const response = await axios
        .get(`${serverUrl}/user/${this.user.id}/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
        .then((res) => res.data)
        .catch((error) => {
          console.log(error);
          return error;
        });
      this.userData = JSON.parse(JSON.stringify(response.user));
    },

    async addUserToGroup(userid, groupid) {
      console.log("add");
      const response = await axios
        .put(
          `${serverUrl}/add_user_to_group/${groupid}/`,
          JSON.stringify({ user_id: userid }),
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
    },

    async getGroup(groupid) {
      const response = await axios
        .get(`${serverUrl}/group/${groupid}/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
        .then((res) => res.data)
        .catch((error) => {
          console.log(error);
          return error;
        });
      return JSON.parse(JSON.stringify(response["Group"]));
    },

    userDataToSend() {
      const data = this.editedUser;
      data["user_type"] = this.editedUserType.type;
      return data;
    },

    // remove user from group
    async removeUserFromGroup(userId, groupId) {
      await axios
        .put(
          `${serverUrl}/delete_user_from_group/${groupId}/`,
          JSON.stringify({ user_id: userId }),
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
    },

    async deleteUser() {
      localStorage.setItem("user", {});
      this.editedUser = {};
      this.editedUserGroups = [];
      this.editedUserType = {};

      await axios
        .delete(`${serverUrl}/user/${this.userData.id}/`, {
          headers: {
            "x-access-token": id_token,
          },
        })
        .then((res) => res.data)
        .catch((error) => {
          console.log(error);
          return error;
        })
        .then((this.deleted_dialog = true));
      const storeuser = { id: 0 };
      localStorage.setItem("user", JSON.stringify(storeuser));
    },

    //post group info in database (create new)
    async saveNewUser(data) {
      if (
        this.editedUser.full_name != "" &&
        this.editedUser.email != "" &&
        this.editedUser.phone_number != "" &&
        this.editedUserType != {}
      ) {
        const response = await axios
          .post(`${serverUrl}/signup`, JSON.stringify(data), {
            headers: {
              "x-access-token": id_token,
              "Content-Type": "application/json",
            },
          })
          .then((res) => res.data)
          .catch(function (error) {
            console.log(error);
          })
          .then((this.saved_dialog = true));
        const newUserId = JSON.parse(JSON.stringify(response.user)).id;

        // add user to groups
        for (let i = 0; i < this.editedUserGroups.length; i++) {
          var group = this.editedUserGroups[i];
          await this.addUserToGroup(newUserId, group.id);
        }
        const storeuser = { id: 0 };
        localStorage.setItem("user", JSON.stringify(storeuser));
      } else this.missing_dialog = true;
    },

    //put group info in database (update)
    async saveExistingUser(data) {
      if (
        this.editedUser.full_name != "" &&
        this.editedUser.email != "" &&
        this.editedUser.phone_number != "" &&
        this.editedUserType != {}
      ) {
        const response = await axios
          .put(`${serverUrl}/user/${this.userData.id}/`, JSON.stringify(data), {
            headers: {
              "x-access-token": id_token,
              "Content-Type": "application/json",
            },
          })
          .then((res) => res.data)
          .catch(function (error) {
            console.log(error);
          });

        if (!response.success) {
          return;
        }

        this.saved_dialog = true;

        const newUserId = JSON.parse(JSON.stringify(response.user)).id;

        if (this.fromAdmin) {
          // add user to groups
          for (let i = 0; i < this.editedUserGroups.length; i++) {
            var group = this.editedUserGroups[i];
            if (!this.userOriginalGroupIds.some((el) => el == group.id)) {
              await this.addUserToGroup(newUserId, group.id);
            }
          }

          // remove user from groups
          for (let i = 0; i < this.userOriginalGroupIds.length; i++) {
            var groupid = this.userOriginalGroupIds[i];
            if (!this.editedUserGroups.some((el) => el.id == groupid)) {
              await this.removeUserFromGroup(newUserId, groupid);
            }
          }
        }
        const storeuser = { id: 0 };
        localStorage.setItem("user", JSON.stringify(storeuser));
      } else {
        this.missing_dialog = true;
      }
    },

    //set user's new/updated info using post/put determined by isNew, set to true if came to page from clicking on an existing user
    async setUserInfo() {
      const data = this.userDataToSend();
      if (this.isNew) {
        this.saveNewUser(data);
      } else this.saveExistingUser(data);
    },
  },

  components: {
    BlackButton,
    MissingDetailsPopup,
    SavedChangesPopup,
    DeletedPopup,
  },
};
</script>

<style scoped lang="scss">
@import "assets/tableStyle.css";
</style>
