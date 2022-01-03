<template>
  <div class="justify-center row align-center q-pa-md q-gutter-sm">
    <q-banner class="bg-primary text-white" style="max-width: 250px" >
            {{postick}}
      <template v-slot:action>
      <q-btn flat color="white" :label="$t('app.confirmation.close')" v-close-popup/>
      <q-btn flat color="white" :label="$t('app.confirmation.reply')" >
      <q-menu anchor="bottom left" self="bottom right" :offset="[35, 24]" v-model="label" >
        <q-editor 
        style="max-width: 194px"
          v-model="editor"
          flat
          content-class="bg-amber-3 text-h6"
          toolbar-text-color="white"
          toolbar-toggle-color="yellow-8"
          toolbar-bg="primary"
          :toolbar="[
          ['bold', 'italic', 'underline'],
          [{
          label: $q.lang.editor.formatting,
          icon: $q.iconSet.editor.formatting,
          list: 'no-icons',
          options: ['p', 'h3', 'h4', 'h5', 'h6', 'code']
        }]
        ]"
    />
    <div class="row">
        <q-btn
      style="width:195px"
      class="e-caret-up item-small item-center q-px-md q-py-xs wrap"
      :label="$t('app.confirmation.send')" 
      @click="sendMessage()"
      outline
      />
    </div>
        </q-menu>
      </q-btn>
        </template>
        </q-banner>    
</div>
</template>

<script>
import { ref, onMounted} from 'vue'
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default {
    name:"NextTrainingPosticks",
    props:['postick', "training", "userId"],
    
  setup (props) {
    const editor= ref("");


    function onRequest(){
      editor.value = props.training.trainer_notes[props.userId];
    }

    async function sendMessage(){
      var message = JSON.stringify({
      "message": editor.value,
      "trainee_id": props.userId
     });

//******************** change to current user********************//
      const response = await axios.post(`${serverUrl}/trainer/message/4/${props.training.id}/`,
      message,
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
      //editor.value = "";
      alert("ההודעה נשלחה")
      }
    

    onMounted(() => {
      onRequest();
    });
    return {
      editor,
      sendMessage,
    }
  }
}
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>