<template>
  <div class="row justify-center q-gutter-x-md items-center bg-grey-2 q-pa-lg " >
    <p class="q-my-none q-mr-md item">{{ $t("dashboard.closest")+":" }}</p>
   
   <div class="q-my-none  items-center row">
    <q-icon name="today"/>
    <p class="q-my-none q-ml-xs items-center item">{{ $t("dashboard.date") }}</p>
    <p class="q-my-none q-ml-sm q-mr-md item2">{{ date }}</p>
   </div>
   
  <div class="q-my-none  items-center  row">
    <q-icon name="light_mode"/>
    <p class="q-my-none  q-ml-xs items-center item">{{ $t("dashboard.day") }}</p>
    <p class="q-my-none q-ml-sm q-mr-md item2">{{ $t(day)}}</p>
  </div>
    
  <div class="q-my-none  items-center  row">
    <q-icon name="schedule"/>
    <p class="q-my-none q-ml-xs items-center item">{{ $t("dashboard.time") }}</p>
    <p class="q-my-none q-ml-sm q-mr-md item2">{{ time }}</p>
  </div>
   
  <div class="q-my-none  items-center row">
    <q-icon name="place"/>
    <p class="q-my-none q-ml-xs items-center item">{{ $t("dashboard.location") }}</p>
    <p class="q-my-none q-ml-sm item2">{{ meeting_place }}</p>
  </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "Trainee",
  props: ["trainingData", "isReady"],
  data() {
    return {
      date: this.trainingData.date,
      day: this.trainingData.day,
      time: this.trainingData.time,
      meeting_place: this.trainingData.meeting_place,
    };
  },
});
</script>
<style scoped>
@import "assets/groupStyle.css";
</style>
