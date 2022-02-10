<template>
    <q-dialog>
      <q-card style="width: 400px;">
        <q-card-section>
          <div style="text-decoration: underline;" class="text-h4 group_header">{{$t("app.confirmation.postTrainee")}}</div>
        </q-card-section>

        <q-card-section  class="q-pt-none">
          <div class="text-primary text-h4 text-bold item q-pa-none q-ma-none">
              {{recievedMessage}}
          </div>
          <!-- <div v-if="recievedMessage == ''" class="text-primary text-h4 text-bold item q-pa-none q-ma-none">
              {{$t("app.confirmation.noNewPosts")}}
          </div> -->
          </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat color="primary" class="item q-ma-none items-end" :label="$t('app.confirmation.close')" v-close-popup/>
        </q-card-actions>
      </q-card>
      </q-dialog >
</template>

<script>
import { ref,onMounted } from 'vue'
import {defineComponent} from "vue";

export default defineComponent({
  name: "TrainerRecieveMessagePopup",
  props:["trainingData", "userId"],
  setup (props) {
    const recievedMessage= ref("");

    function onRequest() {
      recievedMessage.value = props.trainingData.notes[props.userId][1];
    }

    onMounted(() => {
      onRequest();
    });

    return {
      recievedMessage,
    }
  }
});
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>