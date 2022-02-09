<template>
  <q-dialog>
    <q-card>
      <q-card-section class="row items-center" icon="done">
        <span class="q-ml-sm item">
          {{ $t("app.popup.savedChanges") }}
        </span>
        <q-btn
          align="left"
          icon="done"
          flat
          color="primary"
          v-close-popup
          @click="this.$router.go(-1)"
          v-if="goBack"
        />
        <q-btn
          align="left"
          icon="done"
          flat
          color="primary"
          v-close-popup
          v-if="!goBack"
        />
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "SavedChangesPopup",
  props: ["goBack"],
});
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>
