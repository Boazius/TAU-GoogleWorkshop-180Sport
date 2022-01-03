<template v-slot:top>
  <section>
    <q-btn
      class="q-ml-sm"
      color="primary"
      :loading="loading"
      :label="$t('table.add')"
      no-caps
      @click="addUser"
    />
    <!-- <q-btn class="q-ml-sm" color="primary" :disable="loading" :label="$t('table.delete')" no-caps @click="removeRow" />
    <q-btn class="q-ml-sm" color="primary" :disable="loading" icon-right="archive" :label="$t('table.export')" no-caps @click="exportTable" /> -->
  </section>
</template>

<script>
// import { exportFile, useQuasar } from "quasar";
import { defineComponent, ref } from "vue";

// function wrapCsvValue (val, formatFn) {
//   let formatted = formatFn !== void 0
//     ? formatFn(val)
//     : val

//   formatted = formatted === void 0 || formatted === null
//     ? ''
//     : String(formatted)

//   formatted = formatted.split('"').join('""')
//   /**
//    * Excel accepts \n and \r in strings, but some other CSV parsers do not
//    * Uncomment the next two lines to escape new lines
//    */
//   // .split('\n').join('\\n')
//   // .split('\r').join('\\r')

//   return `"${formatted}"`
// }
export default defineComponent({
  name: "TableTopButtons",
  props: ["type", "tableType"],
  data() {
    return {
      loading: false,
    };
  },

  methods: {
    addUser() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
      }, 500);
      const user = {
        id: 0,
        type: this.tableType
        };
      localStorage.setItem('user', JSON.stringify(user));      
      this.$router.push(`/user/${user.id}`);
    },

    // removeRow () {
    //   loading.value = true
    //   setTimeout(() => {
    //     const index = Math.floor(Math.random() * rows.value.length)
    //     rows.value = [ ...rows.value.slice(0, index), ...rows.value.slice(index + 1) ]
    //     loading.value = false
    //   }, 500)
    // }
  },
});
</script>
