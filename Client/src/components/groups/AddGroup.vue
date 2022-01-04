<template v-slot:bottom>
  <section class="q-pr-xl">
    <q-btn
    size="22px"
      class="q-ml-sm "
      color="primary"
      :loading="loading"
      :label="$t('groups.add')"
      no-caps
      @click="addGroup"
    />
    <!-- <q-btn class="q-ml-sm" color="primary" :disable="loading" :label="$t('table.delete')" no-caps @click="removeRow" />
    <q-btn class="q-ml-sm" color="primary" :disable="loading" icon-right="archive" :label="$t('table.export')" no-caps @click="exportTable" /> -->
  </section>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "AddGroup",
  data() {
    return {
      loading: false,
    };
  },

  methods: {
    addGroup() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
        localStorage.setItem('groupId', JSON.stringify({id:0}));      
        this.$router.push({
          path: "/group/details",
        });
      }, 500);
    },

  },
});
</script>
