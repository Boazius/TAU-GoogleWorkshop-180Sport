<template>
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">{{$t('table.title.trainers')}}</h3>
      <trainer-table></trainer-table>
    </div>
  </q-page>
</template>

<script>
import TrainerTable from 'components/table/TrainerTable.vue';

export default {
  components: { 
    TrainerTable
    },
 };
</script>

