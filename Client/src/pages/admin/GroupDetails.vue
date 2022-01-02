<template>
  <q-page padding>
    <div class="row">
      <div>
        <q-btn
          size="sm"
        class="q-mr-md q-mt-sm"
          padding="sm"
          
          glossy
          ripple="center"
          color="primary"
          icon="arrow_forward"
          @click="onGoBack"

        />
      </div>
      <q-item-section v-if="isNew"
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
        >{{ $t("groups.add") }}
      </q-item-section>
      <q-item-section v-if="!isNew"
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
        >{{ $t("groups.edit") }}
      </q-item-section>
      <q-space />
    </div>
    <group-credentials-list :isNew="isNew" ></group-credentials-list>
  </q-page>
</template>

<script>
import GroupCredentialsList from 'components/list/GroupCredentialsList.vue';

export default {
  name: "NewGroupPage",
  computed:{
    isNew(){
      return (JSON.parse(localStorage.getItem("groupId")).id) == 0;
    }
  },
  methods: {
    // handler() {
    //   window.localStorage.removeItem('userdata');
    // },
    onGoBack() {
      this.$router.go(-1);
    }
  },
  components: {
    GroupCredentialsList,
  },
};
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
