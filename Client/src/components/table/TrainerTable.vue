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
           <q-td key="name" :props="props">
             <q-item to="/user/:id" clickable v-ripple style="display: table-cell; vertical-align: end;">    <!--   put clickble name in order to go to user pagee and edit from there. now redirected to groups for no reason     -->
            {{ props.row.name }}
            <!-- <q-popup-edit v-model="props.row.name"  title="ערוך שם" :validate="val => val.length > 0">
              <template v-slot="scope">
                <q-input type="name" v-model="props.row.name" :rules="[
                val => scope.validate(scope.value) || 'שם לא תקין']">
                <template v-slot:after>
                 <q-btn
                 flat dense color="negative" icon="cancel"
                 @click.stop="scope.cancel"/>

                <q-btn
                flat dense color="positive" icon="check_circle"
                @click.stop="scope.set"
                :disable="scope.validate(scope.value) === false || scope.initialValue === scope.value"
              />
            </template>
            </q-input>
            </template>

            </q-popup-edit> -->
            </q-item>

          </q-td>
          <q-td key="phone" :props="props">
            {{ props.row.phone }}
            <!-- <q-popup-edit v-model="props.row.phone" title="ערוך טלפון" :validate="val => (val.length == 10 || val.length == 9) && Number(val) !=NaN">
              <template v-slot="scope">
                <q-input type="phone" v-model="props.row.phone" :rules="[
                val => scope.validate(scope.value) || 'מספר טלפון לא תקין']">
                <template v-slot:after>
                 <q-btn
                 flat dense color="negative" icon="cancel"
                 @click.stop="scope.cancel"/>

                <q-btn
                flat dense color="positive" icon="check_circle"
                @click.stop="scope.set"
                :disable="scope.validate(scope.value) === false || scope.initialValue === scope.value"
              />
            </template>
            </q-input>
            </template>

            </q-popup-edit> -->
          </q-td>
           <q-td key="groups" :props="props">{{ props.row.groups }}
            <q-popup-edit v-model="props.row.groups" title="ערוך קבוצה" >
              <q-input v-model="props.row.groups" />
            </q-popup-edit>
          </q-td>
        </q-tr>
      </template>
      <template v-slot:top>
        <table-top-buttons></table-top-buttons>
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
import { mockTrainers  } from "./mockdata.js";
import { trainerColumns  } from "components/table/TableColumns.js";
import TableTopButtons from 'components/table/TableTopButtons.vue';


const columns = trainerColumns;
const originalRows = mockTrainers; //temporary for mock data until fetch from server is implemented

export default defineComponent({
  components: { TableTopButtons },

  setup() {
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
      const data = filter
        ? originalRows.filter((row) => row.name.includes(filter))
        : originalRows.slice();

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
        return originalRows.length;
      }
      let count = 0;
      originalRows.forEach((treat) => {
        if (treat.name.includes(filter)) {
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
      onRequest,
     
    };
  },
});
</script>
<style scoped>
@import "assets/tableStyle.css";

</style>
