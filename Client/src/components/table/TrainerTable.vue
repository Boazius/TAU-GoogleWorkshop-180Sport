<template>
    <q-table
      :rows="rows"
      :columns="columns"
      row-key="id"
      v-model:pagination="pagination"
      :loading="loading"
      :filter="filter"
      @request="onRequest"
      binary-state-sort
      >
      <template v-slot:body="props">
        <q-tr :props="props">
           <q-td key="full_name" :props="props">
            <q-item @click="goToUserPage(props.row)" clickable v-ripple style="display: table-cell; vertical-align: end;">    <!--   put clickble name in order to go to user pagee and edit from there. now redirected to groups for no reason     -->
            {{ props.row.full_name }}
            </q-item>

          </q-td>
          <q-td key="phone_number" :props="props">
            {{ props.row.phone_number }}
          </q-td>
           <q-td key="group_ids" :props="props">{{ props.row.group_ids }}
          </q-td>
          <q-td key="email" :props="props"
          >{{ props.row.email }}
        </q-td>
        </q-tr>
      </template>
      <template v-slot:top>
        <table-top-buttons 
        v-if="!fromGroupPage"
      :rows="rows"
      :rowCount="rowCount"
      :loading="loading"></table-top-buttons>
        <q-space />
    <q-input  borderless dense debounce="300" color="primary" v-model="filter" outlined placeholder="Search">
        <template v-slot:append>
            <q-icon name="search" />
        </template>
    </q-input>          </template>
    </q-table>
</template>

<script>
import { ref, onMounted,defineComponent } from "vue";
import { userColumns  } from "components/table/TableColumns.js";
import TableTopButtons from 'components/table/TableTopButtons.vue';


const columns = userColumns;
//const originalRows = mockTrainers; //temporary for mock data until fetch from server is implemented

export default defineComponent({
  name:'TrainerTable',
  components: { TableTopButtons },
  props:["table_data","fromGroupPage"],

   methods:{
    goToUserPage(row){
      const user = JSON.stringify(row);
      localStorage.setItem('userdata', user);      
      this.$router.push('/user/:id'); 
    },  

  },
  setup(props) {
    const tableData = ref([])
    const rows = ref([]);
    const filter = ref("");
    const loading = ref(false);
    const rowCount = ref(10)

    const pagination = ref({
      sortBy: "desc",
      descending: false,
      page: 1,
      rowsPerPage: 5,
      rowsNumber: 10,
    });

    // emulate ajax call
    // SELECT * FROM ... WHERE...LIMIT...
    function fetchFromServer(startRow, count, filter, sortBy, descending) {
      tableData.value = props.table_data;
      const data = filter
        ? tableData.value.filter((row) => row.full_name.includes(filter))
        : tableData.value.slice();

      // handle sortBy
      if (sortBy) {
        const sortFn =
          sortBy === "desc"
            ? descending
              ? (a, b) => (a.name > b.name ? -1 : a.name < b.name ? 1 : 0)
              : (a, b) => (a.name > b.name ? 1 : a.name < b.name ? -1 : 0)
            : descending
            ? (a, b) => parseFloat(b[sortBy]) - parseFloat(a[sortBy])
            : (a, b) => parseFloat(a[sortBy]) - parseFloat(b[sortBy]);
        data.sort(sortFn);
      }

      return data.slice(startRow, startRow + count);
    }

    // emulate 'SELECT count(*) FROM ...WHERE...'
    function getRowsNumberCount(filter) {
      if (!filter) {
        return tableData.value.length;
      }
      let count = 0;
      tableData.value.forEach((treat) => {
        if (treat.full_name.includes(filter)) {
          ++count;
        }
      });
      return count;
    }

    function onRequest(props) {
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      const filter = props.filter;

      loading.value = true;

      // emulate server
      setTimeout(() => {
        // update rowsCount with appropriate value
        pagination.value.rowsNumber = getRowsNumberCount(filter);

        // get all rows if "All" (0) is selected
        const fetchCount =
          rowsPerPage === 0 ? pagination.value.rowsNumber : rowsPerPage;

        // calculate starting row of data
        const startRow = (page - 1) * rowsPerPage;

        // fetch data from "server"
        const returnedData = fetchFromServer(
          startRow,
          fetchCount,
          filter,
          sortBy,
          descending
        );

        // clear out existing data and add new
        rows.value.splice(0, rows.value.length, ...returnedData);

        // don't forget to update local pagination object
        pagination.value.page = page;
        pagination.value.rowsPerPage = rowsPerPage;
        pagination.value.sortBy = sortBy;
        pagination.value.descending = descending;

        // ...and turn of loading indicator
        loading.value = false;
      }, 1500);
    }

    onMounted(() => {
      // get initial data from server (1st page)
      onRequest({
        pagination: pagination.value,
        filter: undefined,
      });
    });

    return {
      filter,
      loading,
      pagination,
      columns,
      rows,
      tableData,
      onRequest,
     
    };
  },
});
</script>
<style scoped>
@import "assets/tableStyle.css";

</style>
