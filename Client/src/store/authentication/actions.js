import i18n from "src/boot/i18n";
import { Quasar } from "quasar";
import axios from "axios";

const serverUrl = "http://127.0.0.1:5000";

//
//  Action: Set Active User
//
export async function setActiveUser(id_token) {
  const response = await axios
    .get(`${serverUrl}/user_by_email/felix.yakubov91@gmail.com`, {
      headers: {
        "x-access-token": id_token,
      },
    })
    .then((res) => res.data)
    .catch((error) => {
      console.log(error);
      return error;
    });
  return "groups";
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
