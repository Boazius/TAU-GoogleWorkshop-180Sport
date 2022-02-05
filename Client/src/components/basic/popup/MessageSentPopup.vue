<template>
    <q-dialog >
        <q-card >
        <q-card-actions class="q-ma-none q-pb-none q-pt-xs q-pl-xs" align="left">
          <q-btn class="q-pa-none bg-white text-primary" padding="xs xs" flat icon="clear" dense v-close-popup />
        </q-card-actions>
          <q-card-section class="q-ma-none q-pt-none q-pl-lg q-pr-lg row items-center">
            <span class="q-ml-sm item">
              {{$t('app.popup.sentMessage')}}
            </span>
          </q-card-section>
      </q-card>
      </q-dialog >
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "MessageSentPopup",
});
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>             