<template>
  <div class="justify-center row align-center q-pa-md q-gutter-sm">
    <q-editor 
    style="max-width: 194px,   font-size:50px"
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
  <div class="column">
    <q-btn
    outline
      size="22px"
      style="height:10px;"
      class="e-caret-up item-small q-px-md q-py-xs wrap"
      :label="$t('app.confirmation.send')" 
      @click="sendMessage()"
      />
    <q-btn
    v-if='recievedMessage != ""'
    outline
      size="22px"
      style="height:10px;"
      class="e-caret-up item-small q-px-md q-py-xs wrap"
      :label="$t('table.posticks')"
      >
        <q-icon name="message" size="lg" color="primary"/>
        <q-menu anchor="top left" self="top right" v-model="label" >

        <q-banner class="bg-primary text-white">
            <!-- {{$t('app.confirmation.newPostFrom')+sender.full_name}}
            <br/> -->
            {{recievedMessage}}
          <template v-slot:action>
      <q-btn flat color="white" :label="$t('app.confirmation.close')" v-close-popup/>
        </template>
        </q-banner>
    </q-menu>
    </q-btn>
  </div>
</div>
</template>

<script>
import { ref,onMounted } from 'vue'
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");

export default {
    name:"EditorPosticks",
    props:["trainingData", "user"],
setup (props) {
    const editor= ref("");
    const recievedMessage= ref("");
    const sender = ref({});
    const senderId = ref();

    function onRequest() {
      editor.value = props.trainingData.notes[props.user.id];
      recievedMessage.value = props.trainingData.trainer_notes[props.user.id];
      // senderId.value = props.trainingData.trainers_id[0];
      // if(recievedMessage.value!= "" && (senderId.value != null || senderId.value != undefined)){
      // }
      // console.log(recievedMessage.value);
      // console.log(senderId.value);
    }

    async function sendMessage(){
      var message = JSON.stringify({
      "message": editor.value
     });
      const response = await axios.post(`${serverUrl}/trainee/message/${props.user.id}/${props.trainingData.id}/`,
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
    

    // async function getTrainerById(){
    //   const response1 = await axios.get(`${serverUrl}/user/${senderId.value}/`,{
    //     headers: { 
    //         'x-access-token': id_token,
    //     },
    // })
    // .then((res)=> res.data)
    // .catch((error)=>{
    //     console.log(error);
    //     return error;
    // });
    // sender.value =  JSON.parse(JSON.stringify(response1["user"]));
    // }

    onMounted(() => {
      onRequest();
    });

    return {
      editor,
      sendMessage,
      recievedMessage,
      // sender,
      // senderId,
      // getTrainerById,
    }
  }
}
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>

