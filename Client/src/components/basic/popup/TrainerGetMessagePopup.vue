<template>
<div>
  <q-btn dense  flat size="lg" class="bg-white text-primary" @click="openMessages()">
    <i class="fas fa-pencil-alt"></i>
  <q-dialog  v-model="message">
      <q-card style="width: 450px;">
        <q-card-section>
          <div style="text-decoration: underline;" class="text-h4 group_header">{{$t("app.confirmation.lastMessage")}}</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div class="text-primary text-h4  q-pa-none q-ma-none">
              {{initialEditor}}
          </div>

          </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat color="primary" class="item q-ma-none" :label="$t('app.confirmation.edit')" @click="editor=initialEditor; edit=true; message=false"/>
          <q-btn flat color="primary" class="item q-ma-none" :label="$t('app.confirmation.close')" v-close-popup/>
        </q-card-actions>
      </q-card>
  </q-dialog >

    <q-dialog v-model="edit" transition-show="scale" transition-hide="scale">
      <q-card style="width: 450px;">
        <q-card-section>
          <div style="text-decoration: underline;" class="text-h4 group_header">{{$t("app.confirmation.newPost")}}</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="editor" autofocus text-color="primary" color="primary" class="text-primary text-bold text-h5" />
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat class="item q-ma-none"
              :label="$t('app.confirmation.send')" 
              @click="sendMessage(); edit=false" />
          <q-btn flat color="primary" class="item q-ma-none" :label="$t('app.confirmation.close')"  v-close-popup/>
        </q-card-actions>
      </q-card>
  </q-dialog >
  <message-sent-popup  v-model="dialog" />
  </q-btn>
</div>
</template>

<script>
import { ref,onMounted ,defineComponent} from 'vue'
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");
import MessageSentPopup from "components/basic/popup/MessageSentPopup.vue";

export default defineComponent({
    name:"TrainerGetMessagePopup",
    props:["trainingData", "userId"],
    components:{MessageSentPopup},

setup (props) {
    const editor= ref("");
    const initialEditor= ref("");
    const dialog = ref(false);
    const edit = ref(false);
    const message = ref(false);
  


    function onRequest() {
      editor.value = props.trainingData.trainer_notes[props.userId][1];
      initialEditor.value = editor.value;
    }

    async function sendMessage(){
      var message = JSON.stringify({
      "message": editor.value,
      "trainee_id": props.userId
     });
      const id =this.$store.getters["authentication/getCurrentUser"].id;

      const response = await axios.post(`${serverUrl}/trainer/message/${id}/${props.trainingData.id}/`,
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
      initialEditor.value = editor.value;
      dialog.value = true;
      }
    

    async function markAsRead(userId,isRead){
      if(!isRead){
      const response = await axios.put(`${serverUrl}/trainer/update_notes_per_user/${userId}/`,
       JSON.stringify({
      "user_id": userId,
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
      }
    }


    function openMessages(){
      if(initialEditor.value != ""){
        message.value = true;
      }
      else edit.value=true;
    }

    onMounted(() => {
      onRequest();
    });

    return {
      editor,
      initialEditor,
      sendMessage,
      dialog,
      edit,
      markAsRead,
      message,
      openMessages,
    }
}
});
</script>

<style scoped>
@import "assets/groupStyle.css";
@import "assets/postickStyle.css";
</style>