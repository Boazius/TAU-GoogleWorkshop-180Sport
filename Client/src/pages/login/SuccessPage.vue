<template>
  <q-page></q-page>
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
      this.$store.dispatch("authentication/setError", {
        show: true,
        message: "app.loginErrorMessage",
      });
    } else {
      const result = await this.$store.dispatch(
        "authentication/setActiveUser",
        {
          id_token,
          user_info,
        }
      );
      if (result) {
        const pageToRedirectTo = await this.$store.dispatch(
          "authentication/setPageToRedirectTo"
        );
        this.$router.push(`/${pageToRedirectTo}`);
      } else {
        this.$router.push("/login");
      }
    }
  },
};
</script>

<style lang="scss" scoped></style>
