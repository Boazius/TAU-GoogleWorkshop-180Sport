<template>
  <div class="q-pa-md">
    <div class="row reverse">
      <q-btn
        class="q-ml-md"
        dense
        glossy
        ripple="center"
        round
        color="primary"
        icon="arrow_forward"
        to="/groups"
      />

      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
      >
        קבוצה 1 - תל אביב
      </q-item-section>
      <q-space />
    </div>
    <q-expansion-item
      style="direction: rtl"
      class="item justify-start"
      switch-toggle-side
      expand-separator
      label="פרטי קבוצה"
    >
      <q-expansion-item
        style="direction: rtl"
        class="item"
        switch-toggle-side
        expand-separator
        label="מתאמנים"
      >
        <q-table
          style="direction: ltr"
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
              <q-td key="comment" :props="props">
                <q-badge color="primary" align="middle" rounded transparent>
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
              <q-td key="message" :props="props"
                >{{ props.row.groups }}
                <q-icon name="message" color="primary" />

                <q-popup-proxy v-model="props.row.message">
                  <!-- <q-banner style="direction:rtl" class="bg-primary text-white">
                היי, לצערי לא אוכל להגיע לשיעור
                <template v-slot:action>
                  <q-btn flat color="white" label="סמן כנקרא" v-close-popup/>
                  <q-btn flat color="white" label="הגב" v-close-popup/>
                </template>
              </q-banner> -->
                </q-popup-proxy>
              </q-td>
              <q-td key="area" :props="props"
                >{{ props.row.area }}
                <q-popup-edit
                  v-model="props.row.area"
                  title="ערוך איזור מגורים"
                >
                  <q-input v-model="props.row.area" />
                </q-popup-edit>
              </q-td>
              <q-td key="phone" :props="props">
                {{ props.row.phone }}
                <q-popup-edit
                  v-model="props.row.phone"
                  title="ערוך טלפון"
                  :validate="
                    (val) =>
                      (val.length == 10 || val.length == 9) &&
                      Number(val) != NaN
                  "
                >
                  <template v-slot="scope">
                    <q-input
                      type="phone"
                      v-model="props.row.phone"
                      :rules="[
                        (val) =>
                          scope.validate(scope.value) || 'מספר טלפון לא תקין',
                      ]"
                    >
                      <template v-slot:after>
                        <q-btn
                          flat
                          dense
                          color="negative"
                          icon="cancel"
                          @click.stop="scope.cancel"
                        />

                        <q-btn
                          flat
                          dense
                          color="positive"
                          icon="check_circle"
                          @click.stop="scope.set"
                          :disable="
                            scope.validate(scope.value) === false ||
                            scope.initialValue === scope.value
                          "
                        />
                      </template>
                    </q-input>
                  </template>
                </q-popup-edit>
              </q-td>

              <q-td key="name" :props="props">
                {{ props.row.name }}
                <q-popup-edit
                  v-model="props.row.name"
                  title="ערוך שם"
                  :validate="(val) => val.length > 0"
                >
                  <template v-slot="scope">
                    <q-input
                      type="name"
                      v-model="props.row.name"
                      :rules="[
                        (val) => scope.validate(scope.value) || 'שם לא תקין',
                      ]"
                    >
                      <template v-slot:after>
                        <q-btn
                          flat
                          dense
                          color="negative"
                          icon="cancel"
                          @click.stop="scope.cancel"
                        />

                        <q-btn
                          flat
                          dense
                          color="positive"
                          icon="check_circle"
                          @click.stop="scope.set"
                          :disable="
                            scope.validate(scope.value) === false ||
                            scope.initialValue === scope.value
                          "
                        />
                      </template>
                    </q-input>
                  </template>
                </q-popup-edit>
              </q-td>
            </q-tr>
          </template>
          <template v-slot:top>
            <q-btn
              class="q-ml-sm"
              color="primary"
              :disable="loading"
              label="ערוך"
              @click="addRow"
            />
            <q-btn
              class="q-ml-sm"
              color="primary"
              :disable="loading"
              icon-right="archive"
              label="יצא טבלה"
              no-caps
              @click="exportTable"
            />
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
      </q-expansion-item>
      <q-expansion-item
        style="direction: rtl"
        class="item"
        switch-toggle-side
        expand-separator
        :header-inset-level="1"
        label="מתנדבים"
      >
        <q-table
          style="direction: ltr"
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
              <q-td key="comment" :props="props">
                <q-badge color="primary" align="middle" rounded transparent>
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
              <q-td key="message" :props="props"
                >{{ props.row.groups }}
                <q-icon name="message" color="primary" />

                <q-popup-proxy v-model="props.row.message">
                  <!-- <q-banner style="direction:rtl" class="bg-primary text-white">
                היי, לצערי לא אוכל להגיע לשיעור
                <template v-slot:action>
                  <q-btn flat color="white" label="סמן כנקרא" v-close-popup/>
                  <q-btn flat color="white" label="הגב" v-close-popup/>
                </template>
              </q-banner> -->
                </q-popup-proxy>
              </q-td>
              <q-td key="area" :props="props"
                >{{ props.row.area }}
                <q-popup-edit
                  v-model="props.row.area"
                  title="ערוך איזור מגורים"
                >
                  <q-input v-model="props.row.area" />
                </q-popup-edit>
              </q-td>
              <q-td key="phone" :props="props">
                {{ props.row.phone }}
                <q-popup-edit
                  v-model="props.row.phone"
                  title="ערוך טלפון"
                  :validate="
                    (val) =>
                      (val.length == 10 || val.length == 9) &&
                      Number(val) != NaN
                  "
                >
                  <template v-slot="scope">
                    <q-input
                      type="phone"
                      v-model="props.row.phone"
                      :rules="[
                        (val) =>
                          scope.validate(scope.value) || 'מספר טלפון לא תקין',
                      ]"
                    >
                      <template v-slot:after>
                        <q-btn
                          flat
                          dense
                          color="negative"
                          icon="cancel"
                          @click.stop="scope.cancel"
                        />

                        <q-btn
                          flat
                          dense
                          color="positive"
                          icon="check_circle"
                          @click.stop="scope.set"
                          :disable="
                            scope.validate(scope.value) === false ||
                            scope.initialValue === scope.value
                          "
                        />
                      </template>
                    </q-input>
                  </template>
                </q-popup-edit>
              </q-td>

              <q-td key="name" :props="props">
                {{ props.row.name }}
                <q-popup-edit
                  v-model="props.row.name"
                  title="ערוך שם"
                  :validate="(val) => val.length > 0"
                >
                  <template v-slot="scope">
                    <q-input
                      type="name"
                      v-model="props.row.name"
                      :rules="[
                        (val) => scope.validate(scope.value) || 'שם לא תקין',
                      ]"
                    >
                      <template v-slot:after>
                        <q-btn
                          flat
                          dense
                          color="negative"
                          icon="cancel"
                          @click.stop="scope.cancel"
                        />

                        <q-btn
                          flat
                          dense
                          color="positive"
                          icon="check_circle"
                          @click.stop="scope.set"
                          :disable="
                            scope.validate(scope.value) === false ||
                            scope.initialValue === scope.value
                          "
                        />
                      </template>
                    </q-input>
                  </template>
                </q-popup-edit>
              </q-td>
            </q-tr>
          </template>
          <template v-slot:top>
            <q-btn
              class="q-ml-sm"
              color="primary"
              :disable="loading"
              label="ערוך"
              @click="addRow"
            />
            <q-btn
              class="q-ml-sm"
              color="primary"
              :disable="loading"
              icon-right="archive"
              label="יצא טבלה"
              no-caps
              @click="exportTable"
            />
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
      </q-expansion-item>

      <q-expansion-item
        style="direction: rtl"
        class="item"
        switch-toggle-side
        expand-separator
        :header-inset-level="1"
        label="מאמנים"
      >
        <q-table
          style="direction: ltr"
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
              <q-td key="comment" :props="props">
                <q-badge color="primary" align="middle" rounded transparent>
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
              <q-td key="message" :props="props"
                >{{ props.row.groups }}
                <q-icon name="message" color="primary" />

                <q-popup-proxy v-model="props.row.message">
                  <!-- <q-banner style="direction:rtl" class="bg-primary text-white">
                היי, לצערי לא אוכל להגיע לשיעור
                <template v-slot:action>
                  <q-btn flat color="white" label="סמן כנקרא" v-close-popup/>
                  <q-btn flat color="white" label="הגב" v-close-popup/>
                </template>
              </q-banner> -->
                </q-popup-proxy>
              </q-td>
              <q-td key="area" :props="props"
                >{{ props.row.area }}
                <q-popup-edit
                  v-model="props.row.area"
                  title="ערוך איזור מגורים"
                >
                  <q-input v-model="props.row.area" />
                </q-popup-edit>
              </q-td>
              <q-td key="phone" :props="props">
                {{ props.row.phone }}
                <q-popup-edit
                  v-model="props.row.phone"
                  title="ערוך טלפון"
                  :validate="
                    (val) =>
                      (val.length == 10 || val.length == 9) &&
                      Number(val) != NaN
                  "
                >
                  <template v-slot="scope">
                    <q-input
                      type="phone"
                      v-model="props.row.phone"
                      :rules="[
                        (val) =>
                          scope.validate(scope.value) || 'מספר טלפון לא תקין',
                      ]"
                    >
                      <template v-slot:after>
                        <q-btn
                          flat
                          dense
                          color="negative"
                          icon="cancel"
                          @click.stop="scope.cancel"
                        />

                        <q-btn
                          flat
                          dense
                          color="positive"
                          icon="check_circle"
                          @click.stop="scope.set"
                          :disable="
                            scope.validate(scope.value) === false ||
                            scope.initialValue === scope.value
                          "
                        />
                      </template>
                    </q-input>
                  </template>
                </q-popup-edit>
              </q-td>

              <q-td key="name" :props="props">
                {{ props.row.name }}
                <q-popup-edit
                  v-model="props.row.name"
                  title="ערוך שם"
                  :validate="(val) => val.length > 0"
                >
                  <template v-slot="scope">
                    <q-input
                      type="name"
                      v-model="props.row.name"
                      :rules="[
                        (val) => scope.validate(scope.value) || 'שם לא תקין',
                      ]"
                    >
                      <template v-slot:after>
                        <q-btn
                          flat
                          dense
                          color="negative"
                          icon="cancel"
                          @click.stop="scope.cancel"
                        />

                        <q-btn
                          flat
                          dense
                          color="positive"
                          icon="check_circle"
                          @click.stop="scope.set"
                          :disable="
                            scope.validate(scope.value) === false ||
                            scope.initialValue === scope.value
                          "
                        />
                      </template>
                    </q-input>
                  </template>
                </q-popup-edit>
              </q-td>
            </q-tr>
          </template>
          <template v-slot:top>
            <q-btn
              class="q-ml-sm"
              color="primary"
              :disable="loading"
              label="ערוך"
              @click="addRow"
            />
            <q-btn
              class="q-ml-sm"
              color="primary"
              :disable="loading"
              icon-right="archive"
              label="יצא טבלה"
              no-caps
              @click="exportTable"
            />
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
      </q-expansion-item>
    </q-expansion-item>

    <q-expansion-item
      style="direction: rtl"
      class="item"
      expand-separator
      switch-toggle-side
      label="פרטי האימון קרוב"
    >
      <q-list bordered class="rounded-borders" style="max-width: 600px">
        <q-item-label header
          >18.11.20
          <q-btn
            class="q-ml-sm q-mr-md"
            color="primary"
            :disable="loading"
            glossy
            push
            padding="sm"
            icon="print"
            no-caps
          />
        </q-item-label>
        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">תומר פיזון</span>
            </q-item-label>
          </q-item-section>
          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs"></div>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">ברק עופר</span>
            </q-item-label>
          </q-item-section>

          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs"></div>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">נינט לוי</span>
            </q-item-label>
          </q-item-section>

          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs"></div>
          </q-item-section>
        </q-item>

        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">קרן פידרמן</span>
            </q-item-label>
          </q-item-section>

          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs"></div>
          </q-item-section>
        </q-item>
      </q-list>
    </q-expansion-item>
    <q-expansion-item
      style="direction: rtl"
      class="item"
      switch-toggle-side
      expand-separator
      label="פרטי האימון האחרון"
    >
      <q-list bordered class="rounded-borders" style="max-width: 600px">
        <q-item-label header>תאריך: 11.11.20</q-item-label>
        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">תומר פיזון</span>
            </q-item-label>
          </q-item-section>
          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs">
              <q-btn
                class="gt-xs"
                size="12px"
                flat
                dense
                round
                label="לא נכח"
                icon="close"
              />
            </div>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">ברק עופר</span>
            </q-item-label>
          </q-item-section>

          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs">
              <q-btn
                class="gt-xs"
                size="12px"
                flat
                dense
                round
                label="לא נכח"
                icon="close"
              />
            </div>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">נינט לוי</span>
            </q-item-label>
          </q-item-section>

          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs">
              <q-btn
                class="gt-xs"
                size="12px"
                flat
                dense
                round
                label="לא נכח"
                icon="close"
              />
            </div>
          </q-item-section>
        </q-item>

        <q-separator spaced />
        <q-item>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">קרן פידרמן</span>
            </q-item-label>
          </q-item-section>

          <q-item-section top side>
            <div class="text-grey-8 q-gutter-xs">
              <q-btn
                class="gt-xs"
                size="12px"
                flat
                dense
                round
                label="לא נכח"
                icon="close"
              />
            </div>
          </q-item-section>
        </q-item>
      </q-list>
    </q-expansion-item>
  </div>
</template>
<script>
import { ref, onMounted } from "vue";
import { exportFile, useQuasar } from "quasar";

const columns = [
  {
    name: "comment",
    label: "פרסם הודעה למשתמש",
    field: "comment",
  },
  {
    name: "message",
    label: "הודעות חדשות",
    field: "message",
  },
  {
    name: "area",
    label: "איזור מגורים",
    field: "area",
    sortable: true,
  },
  {
    name: "phone",
    label: "טלפון",
    field: "phone",
    sortable: true,
  },
  {
    name: "name",
    required: true,
    label: "שם",
    align: "right",
    field: (row) => row.name,
    format: (val) => `${val}`,
    sortable: true,
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
    id: 9,
    name: "קרן פידרמן",
    phone: "054696989",
    group: 1,
    area: "תל אביב",
  },
];

function wrapCsvValue(val, formatFn) {
  let formatted = formatFn !== void 0 ? formatFn(val) : val;

  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);

  formatted = formatted.split('"').join('""');
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`;
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
    const rowCount = ref(10);
    const $q = useQuasar();

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

      exportTable() {
        // naive encoding to csv format
        const content = [columns.map((col) => wrapCsvValue(col.label))]
          .concat(
            rows.value.map((row) =>
              columns
                .map((col) =>
                  wrapCsvValue(
                    typeof col.field === "function"
                      ? col.field(row)
                      : row[col.field === void 0 ? col.name : col.field],
                    col.format
                  )
                )
                .join(",")
            )
          )
          .join("\r\n");

        const status = exportFile("table-export.csv", content, "text/csv");

        if (status !== true) {
          $q.notify({
            message: "Browser denied file download...",
            color: "negative",
            icon: "warning",
          });
        }
      },

      addRow() {
        loading.value = true;
        setTimeout(() => {
          const index = Math.floor(Math.random() * (rows.value.length + 1)),
            row = originalRows[Math.floor(Math.random() * originalRows.length)];

          if (rows.value.length === 0) {
            rowCount.value = 0;
          }

          row.id = ++rowCount.value;
          const newRow = { ...row }; // extend({}, row, { name: `${row.name} (${row.__count})` })
          rows.value = [
            ...rows.value.slice(0, index),
            newRow,
            ...rows.value.slice(index),
          ];
          loading.value = false;
        }, 500);
      },

      removeRow() {
        loading.value = true;
        setTimeout(() => {
          const index = Math.floor(Math.random() * rows.value.length);
          rows.value = [
            ...rows.value.slice(0, index),
            ...rows.value.slice(index + 1),
          ];
          loading.value = false;
        }, 500);
      },
    };
  },
};
</script>
<style>
.q-table th {
  text-align: right;
  font-family: "lucida grande", tahoma, verdana, arial, sans-serif;
  font-weight: bold;
  color: #1d2172;
}

.q-table td {
  text-align: right;
  font-family: "lucida grande", tahoma, verdana, arial, sans-serif;

  color: #1d2172;
}
.table_header {
  text-align: right;
  font-weight: bold;
  font-family: "lucida grande", tahoma, verdana, arial, sans-serif;

  color: #1d2172;
}
.item {
  text-align: right;
  font-family: "lucida grande", tahoma, verdana, arial, sans-serif;
  font-weight: bold;
  font-size: large;
  color: #1d2172;
}
.item-small {
  text-align: right;
  font-family: "lucida grande", tahoma, verdana, arial, sans-serif;
  font-weight: bold;
  font-size: medium;
  color: #1d2172;
}
</style>
