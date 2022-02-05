<template>
    <q-dialog >
        <q-card >
          <q-card-section class="row items-center" icon="done">
            <span class="q-ml-sm item">
              {{$t('app.popup.missingDetails')}}
            </span>
            <q-btn align="left" icon="clear" flat  color="primary" v-close-popup />
          </q-card-section>
      </q-card>
      </q-dialog >
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "MissingDetailsPopup",
});
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>