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
          key="name"
          :props="props"
          @click="goToUserPage(props.row)"
          clickable
          v-ripple
          class="cursor-pointer"
        >
          <q-item style="display: table-cell; vertical-align: end">
            <!--   put clickble name in order to go to user pagee and edit from there. now redirected to groups for no reason     -->

            {{ props.row.name }}
            <!-- <q-popup-edit v-model="props.row.name"  :title="$t('table.editName')" :validate="val => val.length > 0">
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
          <!-- <q-popup-edit v-model="props.row.phone" :title="$t('table.editPhone')" :validate="val => (val.length == 10 || val.length == 9) && Number(val) !=NaN">
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
        <q-td key="group" :props="props"
          >{{ props.row.group }}
          <!-- <q-popup-edit v-model="props.row.group" :title="$t('table.editGroups')" >
              <q-input v-model="props.row.group" dense autofocus hint="ניתן להוסיף כמה קבוצות" />
            </q-popup-edit> -->
        </q-td>
        <q-td key="area" :props="props"
          >{{ props.row.area }}
          <!-- <q-popup-edit v-model="props.row.area" :title="$t('table.editLivingArea')" >
              <q-input v-model="props.row.area" />
            </q-popup-edit> -->
        </q-td>

        <q-td key="message" :props="props"
          >{{ props.row.groups }}
          <q-icon name="message" color="primary" />

          <!-- <q-popup-proxy v-model="label" >

              <q-banner class="bg-primary text-white">
                היי, לצערי לא אוכל להגיע לשיעור
                <template v-slot:action>
                  <q-btn flat color="white" :label="$t('table.markAsRead')" v-close-popup/>
                  <q-btn flat color="white" :label="$t('table.post')" v-close-popup/>
                </template>
              </q-banner>
            </q-popup-proxy> -->
        </q-td>
        <q-td key="comment" :props="props">
          <q-badge color="primary" align="middle" rounded transparent>
            <q-icon name="edit" color="white" />
            <div v-html="props.row.comment"></div>
            <!-- <q-popup-edit
              buttons
              v-model="props.row.comment"
              v-slot="scope"
            >
              <q-editor
                v-model="scope.value"
                min-height="5rem"
                autofocus
                @keyup.enter.stop
              />
            </q-popup-edit> -->
          </q-badge>
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

const originalRows = mockRows; //temporary for mock data until fetch from server is implemented
const columns = userColumns;

export default defineComponent({
  name: "userTable",
  components: { TableTopButtons },

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
        ? originalRows.filter((row) => row.name.includes(filter))
        : originalRows.slice();

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

        return originalRows.length;
      }
      let count = 0;
      // console.log(5);

      originalRows.forEach((treat) => {
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
