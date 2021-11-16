<template>
  <q-page>
    <user-login-carousel />
  </q-page>
</template>

<script>
import UserLoginCarousel from "components/login/UserLoginCarousel.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserLogin",
  components: {
    UserLoginCarousel,
  },
});
</script>

<style lang="scss" scoped></style>
