<template>
  <q-page> success </q-page>
</template>

<script>
export default {
  name: "SuccessPage",
  async beforeMount() {
    const urlParams = new URLSearchParams(window.location.search);
    let id = urlParams.get("id_token");
    let user_info = urlParams.get("user_info");
    let id_token = id.split(",").find((x) => x.includes("id_token"));
    id_token = id_token
      .replace(/\s/g, "")
      .replace(/["']/g, "")
      .replace("id_token:", "");
    if (id_token !== "") {
      localStorage.setItem("id_token", id_token);
      const pageToRedirectTo = await this.$store.dispatch(
        "authentication/setActiveUser",
        id_token
      );
      this.$router.push(`/${pageToRedirectTo}`);
    } else {
      this.$router.push("/login");
    }
  },
};
</script>

<style lang="scss" scoped></style>
