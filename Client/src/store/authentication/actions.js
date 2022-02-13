import { Quasar } from "quasar";
import axios from "axios";

const serverUrl = "https://server-idhusddnia-ew.a.run.app";

//
//  Action: Set Active User
//
export async function setActiveUser(
  { dispatch, commit },
  { id_token, user_info }
) {
  let idToken = id_token.replace(/'/g, '"');
  idToken = JSON.parse(idToken);
  const token = idToken?.id_token;

  if (token === null) {
    return "login";
  }
  localStorage.setItem("id_token", token);

  let userInfo = user_info
    .replace(/'/g, '"')
    .replace("True", '"True"')
    .replace("False", '"False"');
  userInfo = JSON.parse(userInfo);

  localStorage.setItem("user_info", user_info);

  const userEmail = userInfo.email;

  if (userEmail) {
    const response = await axios
      .get(`${serverUrl}/user/email/${userEmail}`, {
        headers: {
          "x-access-token": token,
        },
      })
      .then((res) => res.data)
      .catch((error) => {
        console.log(error);
        return error;
      });
    if (response && response.success === true) {
      commit("setCurrentUser", response.user);
      localStorage.setItem("user_data", JSON.stringify(response.user));
      // await dispatch("setLanguage", userInfo.locale);
      return true;
    }
  }

  return false;
}

export function setPageToRedirectTo({ state }) {
  const currentUser = state.user.currentUser;
  const { user_type } = currentUser;
  switch (user_type) {
    case 1:
      return "groups";
    case 2:
      return "trainer-groups";
    case 3:
    case 4:
      return "next-training";
  }
}

//
//  Action: Set current edited user
//
export async function setEditedUser({ commit }, payload) {
  commit("setEditedUser", payload);
}

//
//  Action: Set error message
//
export async function setError({ commit }, payload) {
  commit("setError", payload);
}

//
//  Action: Update user
//
export async function updateUserData({ commit }, payload) {}

//
//  Action: Set Language
//
function languageHelper(lang) {
  if (lang == "en" || lang == "en-GB") {
    lang = "en-US";
  }
  if (lang == "he-IL") {
    lang = "he";
  }
  localStorage.setItem("user_lang", lang);
  return lang;
}

export async function setLanguage({ commit }, lang = "") {
  if (lang) {
    lang = languageHelper(lang);
  } else {
    const local = localStorage.getItem("user_lang");
    if (local) {
      lang = local;
    } else {
      lang = Quasar.lang.getLocale();
      lang = languageHelper(lang);
    }
  }

  commit("setLanguage", lang);
  const iso = await import("quasar/lang/" + lang);

  Quasar.lang.set(iso.default);
  return lang;
}

//
//  Action: Check user login
//
export async function checkLogin({ state, commit, dispatch }) {
  // Check if user authenticated
  if (state.user.authenticated === true) {
    return true;
  }

  // Check if has jwt token
  const hasToken = localStorage.getItem("id_token");
  if (!hasToken) {
    return false;
  }

  //TODO: if not, try to use token & user_info to validate again
  let userData = localStorage.getItem("user_data");

  if (userData) {
    commit("setCurrentUser", JSON.parse(userData));
    return true;
  }

  return false;
}

//
// Action: logout
//
export async function logout({ commit }) {
  localStorage.clear();
  commit("resetState");
  commit("app/resetState", null, { root: true });
}
