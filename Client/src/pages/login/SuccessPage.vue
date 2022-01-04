<template>
  <q-page> success </q-page>
</template>

<script>
export default {
  name: "SuccessPage",
  async beforeMount() {
    const urlParams = new URLSearchParams(window.location.search);
    const id_token = urlParams.get("id_token");
    const user_info = urlParams.get("user_info");

    if (id_token === null || user_info === null) {
      this.$router.push("/login");
      //TODO: add local storage error to avoid infinite loop
    } else {
      const pageToRedirectTo = await this.$store.dispatch(
        "authentication/setActiveUser",
        {
          id_token,
          user_info,
        }
      );
      this.$router.push(`/${pageToRedirectTo}`);
    }
  },
};
</script>

<style lang="scss" scoped></style>
