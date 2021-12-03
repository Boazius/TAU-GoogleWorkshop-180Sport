<template>
  <div class="q-pa-md">
    <h3 class="table_header wrap q-mb-none">{{$t('table.title.trainees')}}</h3>
    <q-table

      :rows="rows"
      :columns="columns"
      row-key="id"
      v-model:pagination="pagination"
      :loading="loading"
      :filter="filter"
      @request="onRequest"
      binary-state-sort
    > <template v-slot:body="props">
        <q-tr :props="props">

          <q-td key="name" :props="props">
            {{ props.row.name }}
            <q-popup-edit v-model="props.row.name"  :title="$t('table.editName')" :validate="val => val.length > 0">
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

            </q-popup-edit>
          </q-td>
          <q-td key="phone" :props="props">
            {{ props.row.phone }}
            <q-popup-edit v-model="props.row.phone" :title="$t('table.editPhone')" :validate="val => (val.length == 10 || val.length == 9) && Number(val) !=NaN">
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

            </q-popup-edit>
          </q-td>
          <q-td key="group" :props="props">{{ props.row.group }}
            <q-popup-edit v-model="props.row.group" :title="$t('table.editGroups')" >
              <q-input v-model="props.row.group" dense autofocus hint="ניתן להוסיף כמה קבוצות" />
            </q-popup-edit>
          </q-td>
          <q-td key="area" :props="props">{{ props.row.area }}
            <q-popup-edit v-model="props.row.area" :title="$t('table.editLivingArea')" >
              <q-input v-model="props.row.area" />
            </q-popup-edit>
          </q-td>

          <q-td key="message" :props="props">{{ props.row.groups }}
            <q-icon name="message" color="primary" />

            <q-popup-proxy v-model="label" >

              <q-banner class="bg-primary text-white">
                היי, לצערי לא אוכל להגיע לשיעור
                <template v-slot:action>
                  <q-btn flat color="white" :label="$t('table.markAsRead')" v-close-popup/>
                  <q-btn flat color="white" :label="$t('table.post')" v-close-popup/>
                </template>
              </q-banner>
            </q-popup-proxy>

          </q-td>
          <q-td key="comment" :props="props">
            <q-badge color="primary"  align="middle" rounded transparent>
              <q-icon name="edit" color="white" />
            <div v-html="props.row.comment"></div>
            <q-popup-edit
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
            </q-popup-edit>
            </q-badge>

          </q-td>
        </q-tr>
      </template>
      <template v-slot:top>
        <q-btn class="q-ml-sm" color="primary" :disable="loading" :label="$t('table.add')" no-caps @click="addRow" />
        <q-btn class="q-ml-sm" color="primary" :disable="loading" :label="$t('table.delete')" no-caps @click="removeRow" />
        <q-btn class="q-ml-sm" color="primary" :disable="loading" icon-right="archive" :label="$t('table.export')" no-caps @click="exportTable" />
        <q-space />
        <q-input
          borderless
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
    </q-table>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { exportFile, useQuasar } from 'quasar';

const columns = [
  { name: 'name',
    required: true,
    label: "שם",
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
    {
    name: "phone",
    label: "טלפון",
    field: "phone",
    sortable: true,
    align:'center'
  },
    {
    name: "group",
    label: "קבוצה",
    field: "group",
    sortable: true,
    align:'center'
    },
      {
    name: "area",
    label: "איזור מגורים",
    field: "area",
    sortable: true,
    align:'left'
    },
  {
    name: "message",
    label: "הודעות חדשות",
    field: "message",
    align:'left'
    },
    {
    name: "comment",
    label: "פרסם הודעה למשתמש",
    field: "comment",
    align:'left'
    },
];

const originalRows = [
  {
    id: 1,
    name: "תומר פיזון",
    phone: "0526831999",
    group: 1,
    area: "תל אביב",
    message: true,
  },
  {
    id: 2,
    name: "מאיה קימל",
    phone: "054969614",
    group: 3,
    area: "הרצליה",
    message: true,

  },
  {
    id: 3,
    name: "ברק עופר",
    phone: "0526834333",
    group: 1,
    area: "תל אביב",
  },
  {
    id: 4,
        name: "נינט לוי",
    phone: "0526831999",
    group: 1,
    area: "תל אביב",
    message: true,
  },
  {
    id: 5,
        name: "איתי שרון",
    phone: "0526544599",
    group: 1,
    area: "תל אביב",
  },
  {
        name: "עומר אדם",
    phone: "0526831999",
    group: 2,
    area: "רמת גן",
  },
  {
    id: 7,
    name: "אליהו ענבי",
    phone: "0527766455",
    group: 3,
    area: "הרצליה",
  },
  {
    id: 8,
    name: "דני דנקר",
    phone: "0526831455",
    group: 3,
    area: "הרצליה",
  },
  {
    id: 9,
    name: "קרן פידרמן",
    phone: "054696989",
    group: 1,
    area: "תל אביב",
  },
  {
    id: 10,
    name: "אופק גלר",
    phone: "0521211999",
    group: 2,
    area: "רמת גן",
  }
]

function wrapCsvValue (val, formatFn) {
  let formatted = formatFn !== void 0
    ? formatFn(val)
    : val

  formatted = formatted === void 0 || formatted === null
    ? ''
    : String(formatted)

  formatted = formatted.split('"').join('""')
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`
}

export default {
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
    const rowCount = ref(10)
    const $q = useQuasar()


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

      exportTable () {
        // naive encoding to csv format
        const content = [columns.map(col => wrapCsvValue(col.label))].concat(
          rows.value.map(row => columns.map(col => wrapCsvValue(
            typeof col.field === 'function'
              ? col.field(row)
              : row[ col.field === void 0 ? col.name : col.field ],
            col.format
          )).join(','))
        ).join('\r\n')

        const status = exportFile(
          'table-export.csv',
          content,
          'text/csv'
        )

        if (status !== true) {
          $q.notify({
            message: 'Browser denied file download...',
            color: 'negative',
            icon: 'warning'
          })
        }
      },

      addRow () {
        loading.value = true
        setTimeout(() => {
          const
            index = Math.floor(Math.random() * (rows.value.length + 1)),
            row = originalRows[ Math.floor(Math.random() * originalRows.length) ]

          if (rows.value.length === 0) {
            rowCount.value = 0
          }

          row.id = ++rowCount.value
          const newRow = { ...row } // extend({}, row, { name: `${row.name} (${row.__count})` })
          rows.value = [ ...rows.value.slice(0, index), newRow, ...rows.value.slice(index) ]
          loading.value = false
        }, 500)
      },

      removeRow () {
        loading.value = true
        setTimeout(() => {
          const index = Math.floor(Math.random() * rows.value.length)
          rows.value = [ ...rows.value.slice(0, index), ...rows.value.slice(index + 1) ]
          loading.value = false
        }, 500)
      }
    };
  },
};
</script>
<style>
.q-table th {
    font-weight: bold;

}

.table_header {
  font-weight: bold;
}
</style>
