<template>
  <q-page>
    <login />
  </q-page>
</template>

<script>
import Login from "components/login/Login.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserLogin",
  components: {
    Login,
  },
});
</script>

<style lang="scss" scoped></style>
