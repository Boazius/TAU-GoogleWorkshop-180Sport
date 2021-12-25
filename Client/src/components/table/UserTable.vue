<template>
  <q-table
    :rows="rows"
    :columns="columns"
    row-key="id"
    :pagination="pagination"
    :loading="loading"
    :filter="filter"
    @request="onRequest"
    binary-state-sort
  >
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td
          key="full_name"
          :props="props"
          @click="goToUserPage(props.row)"
          clickable
          v-ripple
          class="cursor-pointer"
        >
          <q-item style="display: table-cell; vertical-align: end"> <!--   put clickble name in order to go to user pagee and edit from there. now redirected to groups for no reason     -->

            {{ props.row.full_name }}

          </q-item>
        </q-td>

        <q-td key="phone_number" :props="props">
          {{ props.row.phone_number }}
        </q-td>
        <q-td key="groups" :props="props"
          >{{ props.row.groups }}
        </q-td>
        <q-td key="email" :props="props"
          >{{ props.row.email }}
        </q-td>

      </q-tr>
    </template>
    <template v-slot:top>
      <table-top-buttons
        :rows="rows"
        :rowCount="rowCount"
        :loading="loading"
      ></table-top-buttons>
      <q-space />
      <q-input
        borderless
        dense
        debounce="300"
        color="primary"
        v-model="filter"
        outlined
        :placeholder="$t('table.search')"
      >
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </template>
  </q-table>
</template>

<script>
import { ref, onMounted, defineComponent } from "vue";
import { useQuasar } from "quasar";
import { userColumns } from "components/table/TableColumns.js";
import { mockRows } from "./mockdata.js";
import TableTopButtons from "components/table/TableTopButtons.vue";

//const table_data = mockRows; //temporary for mock data until fetch from server is implemented
const columns = userColumns;

export default defineComponent({
  name: "userTable",
  components: { TableTopButtons },
  props:["table_data"],
  data(){
    return {
      tableData :  this.table_data
    }
  },


  methods: {
    goToUserPage(row) {
      const user = JSON.parse(JSON.stringify(row));
      this.$store.dispatch("authentication/setEditedUser", user);
      this.$router.push(`/user/${user.id}`);
    },
    saveUser(row) {
      user = JSON.stringify(row);
      localStorage.setItem("userdata", user);
    },
  },
  setup() {
    const rows = ref([]);
    const filter = ref("");
    const loading = ref(false);
    const pagination = ref({
      sortBy: "desc",
      descending: false,
      page: 1,
      rowsPerPage: 7,
      rowsNumber: 10,
    });
    const rowCount = ref(10);
    const $q = useQuasar();

    // emulate ajax call
    // SELECT * FROM ... WHERE...LIMIT...
    function fetchFromServer(startRow, count, filter, sortBy, descending) {
      // console.log(1);
      const data = filter
        ?this.tableData.filter((row) => row.name.includes(filter))
        :this.tableData.slice();

      // handle sortBy
      if (sortBy) {
        // console.log(2);

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
      // console.log(3);

      if (!filter) {
        // console.log(4);

        return this.tableData.length;
      }
      let count = 0;
      // console.log(5);

      this.tableData.forEach((treat) => {
        if (treat.name.includes(filter)) {
          // console.log(6);

          ++count;
        }
      });
      return count;
    }

    function onRequest(props) {
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      const filter = props.filter;
      // console.log(7);

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
      }, 500);
    }

    onMounted(() => {
      // console.log(8);

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
      rowCount,
      onRequest,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
