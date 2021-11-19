import i18n from 'src/boot/i18n';
import { Quasar } from 'quasar';

//
//  Action: Set Language
//
export async function setLanguage({ commit }, payload) {
  let lang = '';
  if (payload) {
    lang = payload;
    localStorage.setItem('user_lang', lang);
  } else {
    const local = localStorage.getItem('user_lang');
    if (local) {
      lang = local;
    } else {
      localStorage.setItem('user_lang', lang);
      lang = i18n.locale;
    }
  }
  commit('setLanguage', lang);
  await import(
    'quasar/lang/' + lang
    )
    .then(lang => {
      Quasar.lang.set(lang.default)
    })

  i18n.locale = lang;
}
