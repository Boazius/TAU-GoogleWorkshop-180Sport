<template>
  <q-page padding>
    <dashboard-toolbar :trainingData="trainingData"></dashboard-toolbar>
    <h3 class="text-h5 text-center group_header">{{ $t('app.confirmation.areYouComing') }}</h3>
    <div class="row justify-center q-gutter-md q-pa-md">
       <q-btn
      size="22px"
      class="q-px-xl q-py-xs"
      color="green"
      :label="$t('app.confirmation.yes')"
      @click="saveSelection"
    />

     <q-btn
      size="22px"
      class="q-px-xl q-py-xs"
      color="red"
      :label="$t('app.confirmation.no')"
      @click="saveSelection"
       />
    </div>
    <div class="col">
      <h6 class="row group_header justify-center wrap q-mb-none">{{$t('app.confirmation.post')}}</h6>
    <editor-posticks ></editor-posticks>
    </div>

  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import DashboardToolbar from "components/DashboardToolbar.vue";
import EditorPosticks from "../components/basic/EditorPosticks.vue";

export default defineComponent({
  name: "Trainee",
  data() {
    return {
      trainingData: {
        time: "16:00",
        date: "2021-11-15",
        location: "Tel Aviv",
      },
    };
  },
  methods:{
    saveSelection(){
      alert("תודה רבה, בחירתך נשמרה!")
    }
  },
  components: {
    DashboardToolbar,
    EditorPosticks,
  },
});
</script>


