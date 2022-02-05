<template>
  <button type="button" size="xl" class="login-with-google-btn" @click="onSignIn">
    <img src="~/assets/images/google.svg" /> {{ $t("authentication.signin") }}
  </button>
</template>

<script>
export default {
  name: "Google Signin",
  methods: {
    onSignIn() {
      window.location.href = "http://127.0.0.1:5000/login";
    },
  },
};
</script>

<style lang="scss" scoped>
.login-with-google-btn {
  transition: background-color 0.3s, box-shadow 0.3s;
  cursor: pointer;
  padding: 24px;
  border: none;
  border-radius: 6px;
  box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 1px 1px rgba(0, 0, 0, 0.25);

  color: #757575;
  font-size: 20px;
  font-weight: 500;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
  background-color: white;

  img {
    height: 22px;
    width: 22px;
    margin-bottom: -4px;
    margin-right: 4px;
  }

  &:hover {
    box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 2px 4px rgba(0, 0, 0, 0.25);
  }

  &:active {
    background-color: #eeeeee;
  }

  &:focus {
    outline: none;
    box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 2px 4px rgba(0, 0, 0, 0.25),
      0 0 0 3px #c8dafc;
  }

  &:disabled {
    filter: grayscale(100%);
    background-color: #ebebeb;
    box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 1px 1px rgba(0, 0, 0, 0.25);
    cursor: not-allowed;
  }
}
</style>
