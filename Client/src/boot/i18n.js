import { createI18n } from "vue-i18n/index";
import messages from "src/i18n";

export default ({ app }) => {
  const i18n = createI18n({
    locale: "he",
    fallbackLocale: "he",
    messages,
  });

  Object.assign(app, { i18n });
  app.use(i18n);
};
