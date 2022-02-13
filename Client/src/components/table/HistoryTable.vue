<template>
  <div class="q-pa-md">
    <q-table
      :rows="trainingHistory"
      :columns="columns"
      row-key="date"
      v-if="trainingHistory"
    >
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th auto-width />
          <q-th v-for="col in props.cols" :key="col.name" :props="props">
            {{ $t(col.label) }}
          </q-th>
        </q-tr>
      </template>

      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td auto-width>
            <q-btn
              size="sm"
              color="accent"
              round
              dense
              @click="props.expand = !props.expand"
              :icon="props.expand ? 'remove' : 'add'"
            />
          </q-td>
          <q-td v-for="col in props.cols" :key="col.name" :props="props">
            {{ col.value }}
          </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props">
          <q-td colspan="100%">
            <q-list separator dense>
              <q-item v-for="user in props.row.attendance_users" :key="user">
                <q-item-section
                  ><span>{{ user[2] }}</span>
                  <span :class="computeColor(user[0])">{{
                    user[0] == 1
                      ? $t("group.history.attendedSingle")
                      : $t("group.history.attendedSingle")
                  }}</span></q-item-section
                >
              </q-item>
            </q-list>
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "HistoryTable",
  props: ["trainingHistory"],
  data() {
    return {
      columns: [
        {
          name: "date",
          label: "group.history.date",
          align: "left",
          field: (row) => this.formatDate(row.date),
          // format: (val) => `${val}`,
          sortable: true,
        },
        {
          name: "time",
          label: "group.history.time",
          align: "left",
          field: (row) => row.time,
        },
        {
          name: "attended",
          label: "group.history.attended",
          align: "left",
          field: (row) => this.attendanceCompute(row.attendance_users, 1),
          sortable: true,
        },
        {
          name: "not_attended",
          label: "group.history.notAttended",
          align: "left",
          field: (row) => this.attendanceCompute(row.attendance_users, 2),
          sortable: true,
        },
        {
          name: "is_happened",
          label: "group.history.isHappened",
          align: "left",
          field: (row) => (row.is_happened ? "V" : "X"),
        },
      ],
    };
  },
  methods: {
    formatDate(date) {
      var myDate = new Date(date);
      var dd = myDate.getDate();
      var mm = myDate.getMonth() + 1;
      var yyyy = myDate.getFullYear();
      if (dd < 10) {
        dd = "0" + dd;
      }
      if (mm < 10) {
        mm = "0" + mm;
      }
      return yyyy + "-" + mm + "-" + dd;
    },
    attendanceCompute(users, attendanceCode) {
      let result = Object.keys(users);
      let count = 0;
      for (const key of result) {
        if (Number.parseInt(users[key][0]) === attendanceCode) {
          count++;
        }
      }
      return count;
    },
    computeColor(code) {
      return code == 1 ? "text-positive" : "text-negative";
    },
  },
});
</script>