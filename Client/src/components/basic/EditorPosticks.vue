<template>
  <div class="justify-center row align-center q-pa-md q-gutter-sm">
    <q-editor 
      v-model="editor"
      flat
      content-class="bg-amber-3"
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
      size="22px"
      style="height:10px;"
      class="e-caret-up item-small q-px-md q-py-xs wrap"
      :label="$t('app.confirmation.send')" 
      @click="sendMessage()"
      />
    <q-btn
      size="22px"
      style="height:10px;"
      class="e-caret-up item-small q-px-md q-py-xs wrap"
      :label="$t('table.posticks')" >
        <q-icon name="message" size="lg" color="primary"/>
        <q-menu anchor="bottom start" v-model="label" >

        <q-banner class="bg-primary text-white">
            {{$t('app.confirmation.noNewPosts')}}
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
    
    function onRequest() {
      editor.value = props.trainingData.notes[props.user.id];
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
      editor.value = "";
      alert("ההודעה נשלחה")
    }
    

    onMounted(() => {
      onRequest();
    });

    return {
      editor,
      sendMessage
    }
  }
}
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>

