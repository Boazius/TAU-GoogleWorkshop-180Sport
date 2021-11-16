<template>
  <q-page padding>
    <dashboard-toolbar :trainingData="trainingData"></dashboard-toolbar>
    <h3 class="text-h5 text-center">{{ $t('app.confirmation.areYouComing') }}</h3>
    <div class="row justify-center q-gutter-md q-pa-md">
       <q-btn
      size="22px"
      class="q-px-xl q-py-xs"
      color="green"
      :label="$t('app.confirmation.yes')"
    />

     <q-btn
      size="22px"
      class="q-px-xl q-py-xs"
      color="red"
      :label="$t('app.confirmation.no')"
    />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import DashboardToolbar from "components/DashboardToolbar.vue";

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
  components: {
    DashboardToolbar,
  },
});
</script>
