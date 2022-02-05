<template>
        <div class="fit row wrap justify-center items-start content-start q-mt-xl">
      <div class="column">
        <trainee-get-message-popup  :trainingData="trainingData" :userId="user.id"/>
      <q-btn
        v-if="!is_message_new"
        style="width: 239px;"
        class="text-h5 group_header  q-mb-none q-mt-md"
        color="grey-2"
        text-color="primary"
        @click="recieve_message = true">
        {{ $t("app.confirmation.post") }}
      </q-btn>
      <q-btn
        v-if="is_message_new"
        style="width: 239px;"
        class="text-h5 group_header  q-mb-none q-mt-md"
        color="grey-2"
        text-color="primary"       
        @click="markAsRead()">
        {{ $t("app.confirmation.post") }}
        <q-icon name="error_outline" color="red" class="q-ml-sm"/>
      </q-btn>
      <trainee-recieve-message-popup v-model="recieve_message" :trainingData="trainingData" :user="user"/>
      </div>
        </div>
</template>

<script>
import {ref, defineComponent, onMounted } from 'vue'
import TraineeGetMessagePopup from '../basic/popup/TraineeGetMessagePopup.vue'
import TraineeRecieveMessagePopup from '../basic/popup/TraineeRecieveMessagePopup.vue'
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default defineComponent({
  components: { 
      TraineeGetMessagePopup ,
      TraineeRecieveMessagePopup,
  },
    name: "EditorButtons",
    props:["trainingData", "user"],
    setup(props){
      const get_message= ref(false);
      const recieve_message= ref(false);
      const is_message_new= ref(false);
    
    function onRequest() {
      is_message_new.value = (props.trainingData.trainer_notes[props.user.id][1] != "") && (props.trainingData.trainer_notes[props.user.id][0] == 0);
      console.log((props.trainingData.trainer_notes[props.user.id][0]));

    }


    async function markAsRead(){
        const response = await axios.put(`${serverUrl}/trainee/mark_message/${props.user.id}/${props.trainingData.id}/`,
        JSON.stringify({
        "mark": 1
      }),
        {
          headers: { 
              'x-access-token': id_token,
              'Content-Type': 'application/json',
          },
        })    
        .then(function (response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
          console.log(error);
        });
      recieve_message.value = true;
      is_message_new.value=false;
      }

    
    onMounted(() => {
      onRequest();
    });

    return{
      get_message,
      recieve_message,
      is_message_new,
      onRequest,
      markAsRead,
    }
  }

});
</script>
