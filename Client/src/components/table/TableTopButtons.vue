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
import { defineComponent, ref } from "vue";


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

  },
});
</script>
