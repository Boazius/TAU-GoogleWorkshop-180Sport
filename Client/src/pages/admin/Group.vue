<template>
  <div class="q-pa-md">
    <div class="row">
      <div>
      <q-btn
        size="sm"
        class="q-ml-md"
        padding="sm"
        round
        glossy
        ripple="center"
        color="primary"
        icon="arrow_forward"
        to="/groups"
      />
      </div>
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
      >{{$t('groups.name')+groupdata.number+" - "+groupdata.location}}
      </q-item-section>
      <q-space />
    </div>
    <q-expansion-item
      class="item"
      switch-toggle-side
      expand-separator
      :label="$t('group.groupDetails')"
    >
      <q-expansion-item
        class="item"
        switch-toggle-side
        :header-inset-level="1"
        expand-separator
        :label="$t('table.title.trainees')"
      >
        <user-table></user-table>
        </q-expansion-item>
      <q-expansion-item
        class="item"
        switch-toggle-side
        expand-separator
        :header-inset-level="1"
        :label="$t('table.title.volunteers')"
      >
      <user-table></user-table>
      </q-expansion-item>

      <q-expansion-item
        class="item"
        switch-toggle-side
        expand-separator
        :header-inset-level="1"
        :label="$t('table.title.trainers')"
      >
        <trainer-table></trainer-table>
        </q-expansion-item>
    </q-expansion-item>

    <q-expansion-item
      class="item"
      expand-separator
      switch-toggle-side
      :label="$t('group.closest')"
    >
    <closest-training-list></closest-training-list>
    </q-expansion-item>
    <q-expansion-item
      class="item"
      switch-toggle-side
      expand-separator
      :label="$t('group.prior')"
    >
    <last-training-list></last-training-list>
    </q-expansion-item>
  </div>
</template>
<script>
import { ref, onMounted } from "vue";
import UserTable from 'components/table/UserTable.vue';
import TrainerTable from 'components/table/TrainerTable.vue'
import closestTrainingList from 'components/list/closestTrainingList.vue'
import lastTrainingList from 'components/list/lastTrainingList.vue'



export default {
  components: { UserTable, TrainerTable,closestTrainingList, lastTrainingList},
  created() {
    if(localStorage.getItem("groupdata")){
        this.groupdata = JSON.parse(localStorage.getItem("groupdata"));
   }
},

data() {
    return {
        groupdata: undefined
    };
  },
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
    };
  },
};
</script>
<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";

</style>