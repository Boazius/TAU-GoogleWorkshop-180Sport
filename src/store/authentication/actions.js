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
      // lang = i18n.locale;
    }
  }

  commit('setLanguage', lang);
  const iso = await import('quasar/lang/' + lang);
  // Quasar.lang.set(lang);
  Quasar.lang.set(iso.default);

  i18n.locale = lang;
}
