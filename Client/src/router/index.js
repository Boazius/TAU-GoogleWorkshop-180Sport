import { route } from "quasar/wrappers";
import {
  createRouter,
  createMemoryHistory,
  createWebHistory,
  createWebHashHistory,
} from "vue-router";
import routes from "./routes";

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default route(function ({ store } /* ssrContext */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : process.env.VUE_ROUTER_MODE === "history"
    ? createWebHistory
    : createWebHashHistory;

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(
      process.env.MODE === "ssr" ? void 0 : process.env.VUE_ROUTER_BASE
    ),
  });

  Router.beforeEach(async (to, from, next) => {
    // 404
    if (to.matched.some((match) => match.path === "/:catchAll(.*)*")) {
      next();
      return;
    }

    if (
      to.path === "/login" ||
      to.matched.some((match) => match.path.startsWith("/login_success"))
    ) {
      next();
      return;
    }

    // Get current user
    const isAuthenticated = await store.dispatch("authentication/checkLogin");

    if (!isAuthenticated) {
      next({ path: "/login" });
    } else {
      const currentUser = store.getters["authentication/getCurrentUser"];

      let { user_type } = currentUser;
      if (user_type == 4) {
        user_type = 3;
      }
      await store.dispatch("app/setMainMenu", user_type);
      const mainMenu = store.getters["app/getMenu"];

      if (to.meta.access !== user_type && to.meta.access !== 0) {
        next({ path: mainMenu[0].link });
        return;
      }

      next();
    }
  });

  return Router;
});
