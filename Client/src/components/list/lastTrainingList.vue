<template>
    <q-list bordered class="rounded-borders" style="max-width: 600px">
        <q-item-label header>תאריך: 9.12.21</q-item-label>
        <attendance-fix-list :header="$t('group.notPresent')" :attendance="2"></attendance-fix-list>
        <attendance-fix-list :header="$t('group.present')" :attendance="1"></attendance-fix-list>
        <attendance-fix-list :header="$t('group.unknown')" :attendance="0"></attendance-fix-list>
      </q-list>
</template>

<script>
import { defineComponent } from 'vue'
import { ref, onMounted } from "vue";
import {mockRows} from 'components/table/mockdata.js';
import attendanceFixList from './attendanceFixList.vue';
const lastList = mockRows;

export default defineComponent({
  components: { attendanceFixList },
    name:"lastTrainingList",
   setup() {
    const loading = ref(false);
    
    function onRequest() {
      loading.value = true;
      setTimeout(() => {
          loading.value = false;
      }, 1500);
    }

    onMounted(() => {
       onRequest({ });
    });

    return {
      loading,
      lastList,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>