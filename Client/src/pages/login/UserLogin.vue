<template>
  <q-page>
  <div class="q-pa-md flex flex-center" >
    <img
      src="~assets/images/loginpic.png"
      style="width: 980px; height: auto"
    >
    </div>
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
