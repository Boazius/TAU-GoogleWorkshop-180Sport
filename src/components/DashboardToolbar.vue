<template>
  <div class="row justify-center q-gutter-x-md items-center bg-grey-2 q-pa-md">
    <p class="q-ma-none">{{ $t("dashboard.closest") }}</p>
    <p class="q-ma-none">{{ $t("dashboard.date") }}</p>
    <q-input v-model="date" type="date" />
    <p class="q-ma-none">{{ $t("dashboard.time") }}</p>
    <q-input v-model="time" type="time" />
    <p class="q-ma-none">{{ $t("dashboard.location") }}</p>
    <q-input v-model="location" type="text" />
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "Trainee",
  props: ["trainingData"],
  data() {
    return {
      time: this.trainingData.time,
      date: this.trainingData.date,
      location: this.trainingData.location,
    };
  },
});
</script>
