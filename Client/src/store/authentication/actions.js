import i18n from "src/boot/i18n";
import { Quasar } from "quasar";
import axios from "axios";

const serverUrl = "http://127.0.0.1:5000";

//
//  Action: Google login
//
export async function login({}) {
  const response = await axios
    .post(`${serverUrl}/user/5`)
    .then((res) => res.data)
    .catch((error) => {
      console.log(error);
      return error;
    });
  return response;
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
    localStorage.setItem("user_lang", lang);
  } else {
    const local = localStorage.getItem("user_lang");
    if (local) {
      lang = local;
    } else {
      localStorage.setItem("user_lang", lang);
      lang = i18n.locale;
    }
  }
  commit("setLanguage", lang);
  await import("quasar/lang/" + lang).then((lang) => {
    Quasar.lang.set(lang.default);
  });

  i18n.locale = lang;
}
