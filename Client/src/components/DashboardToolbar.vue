<template>
  <div class="row justify-center q-gutter-x-md items-center bg-grey-2 q-pa-lg " >
    <p class="q-my-none q-mr-md item">{{ $t("dashboard.closest")+":" }}</p>
   
    <p class="q-my-none item">{{ $t("dashboard.date") }}</p>
    <p class="q-my-none q-ml-sm q-mr-md item2">{{ date }}</p>
   
    <p class="q-my-none  item">{{ $t("dashboard.day") }}</p>
    <p class="q-my-none q-ml-sm q-mr-md item2">{{ day }}</p>
    
    <p class="q-my-none  item">{{ $t("dashboard.time") }}</p>
    <p class="q-my-none q-ml-sm q-mr-md item2">{{ time }}</p>
   
    <p class="q-my-none item">{{ $t("dashboard.location") }}</p>
    <p class="q-my-none q-ml-sm item2">{{ meeting_place }}</p>

  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "Trainee",
  props: ["trainingData","everthingIsReady"],
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