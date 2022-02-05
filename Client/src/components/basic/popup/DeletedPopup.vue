<template>
    <q-dialog persistent>
        <q-card >
          <q-card-section class="row items-center" icon="done">
            <span class="q-ml-sm item">
              {{$t('app.popup.deleted')}}
            </span>
            <q-btn align="left" icon="done" flat  color="primary" v-close-popup @click="this.$router.go(-1)"/>
          </q-card-section>
      </q-card>
      </q-dialog >
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "DeletedPopup",
});
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>