<template>
  <q-page> success </q-page>
</template>

<script>
export default {
  name: "SuccessPage",
  beforeMount() {
    const urlParams = new URLSearchParams(window.location.search);
    let id_token = urlParams.get("id_token");
  },
};
</script>

<style lang="scss" scoped></style>
