import { Quasar } from "quasar";
import axios from "axios";

const serverUrl = "http://127.0.0.1:5000";

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
      await dispatch("setLanguage", userInfo.locale);
      return "groups";
    }
  }

  return "login";
}

//
//  Action: Set current edited user
//
export async function setEditedUser({ commit }, payload) {
  commit("setEditedUser", payload);
}

//
//  Action: Update user
//
export async function updateUserData({ commit }, payload) {}

//
//  Action: Set Language
//
export async function setLanguage({ commit }, payload) {
  let lang = "";
  if (payload) {
    lang = payload;
    if (lang == "en") {
      lang = "en-US";
    }
    if (lang == "he-IL") {
      lang = "he";
    }
    localStorage.setItem("user_lang", lang);
  } else {
    const local = localStorage.getItem("user_lang");
    if (local) {
      lang = local;
    } else {
      lang = Quasar.lang.getLocale();
      localStorage.setItem("user_lang", lang);
    }
  }
  if (lang == "en") {
    lang = "en-US";
  }
  if (lang == "he-IL") {
    lang = "he";
  }
  commit("setLanguage", lang);
  const iso = await import("quasar/lang/" + lang);

  Quasar.lang.set(iso.default);
  
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
