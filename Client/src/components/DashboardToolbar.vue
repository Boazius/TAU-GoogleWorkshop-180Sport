<template>
  <div class="row justify-center q-gutter-x-md items-center bg-grey-2 q-pa-lg item" >
    <p class="q-ma-none">{{ $t("dashboard.closest")+":" }}</p>
   
    <p class="q-ma-none">{{ $t("dashboard.date") }}</p>
    <q-input readonly  class="item" v-model="date" type="date" dense/>
   
    <p class="q-ma-none">{{ $t("dashboard.day") }}</p>
    <q-input readonly  class="item" v-model="day" type="day" dense/>
    
    <p class="q-ma-none">{{ $t("dashboard.time") }}</p>
    <q-input readonly  class="item" v-model="time" type="time" dense/>
   
    <p class="q-ma-none">{{ $t("dashboard.location") }}</p>
    <q-input readonly  class="item" v-model="meeting_place" type="text" dense/>
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