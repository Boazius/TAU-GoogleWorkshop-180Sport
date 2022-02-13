<template>
  <q-dialog persistent>
    <q-card>
      <q-card-section class="row items-center" icon="done">
        <q-btn
          align="left"
          icon="logout"
          flat
          color="primary"
          @click="onLogout"
          v-close-popup
        />
        <span class="q-ml-sm item">
          {{ $t("authentication.relogin") }}
        </span>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ReloginPopup",
  methods: {
    async onLogout() {
      console.log("logging out");
      await this.$store.dispatch("authentication/logout");
      this.$router.push({
        path: "/login",
      });
    },
  },
});
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>
