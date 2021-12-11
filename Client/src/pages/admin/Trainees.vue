<template>
  <q-page>
    <div class="q-pa-md">
      <h3 class="table_header wrap q-mb-none">{{$t('table.title.trainees')}}</h3>
      <user-table></user-table>
    </div>
  </q-page>
</template>

<script>
import userTable from 'components/table/UserTable.vue';

export default {
  components: { 
    userTable
    },
 };
</script>

