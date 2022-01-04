const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/Index.vue"),
        meta: { access: 0 },
      },
      {
        path: "/groups",
        component: () => import("pages/admin/AllGroups.vue"),
        meta: { access: 1 },
      },
      {
        path: "/group",
        component: () => import("pages/admin/Group.vue"), //TODO
        meta: { access: 2 },
      },
      {
        path: "/group/details",
        component: () => import("pages/admin/GroupDetails.vue"),
        meta: { access: 1 },
      },
      {
        path: "/trainers",
        component: () => import("pages/admin/Trainers.vue"),
        meta: { access: 1 },
      },
      {
        path: "/volunteers",
        component: () => import("pages/admin/Volunteers.vue"),
        meta: { access: 1 },
      },
      {
        path: "/trainees",
        component: () => import("pages/admin/Trainees.vue"),
        meta: { access: 1 },
      },
      {
        path: "/trainer-groups",
        component: () => import("pages/Trainer.vue"),
        meta: { access: 2 },
      },
      {
        path: "/next-training/",
        component: () => import("pages/Trainee.vue"),
        meta: { access: 3 },
      },
      {
        path: "/details",
        component: () => import("pages/TraineeDetails.vue"),
        meta: { access: 0 },
      },
      { path: "/login", component: () => import("pages/login/UserLogin.vue") },

      {
        path: "/login_success",
        component: () => import("pages/login/SuccessPage.vue"),
      },
      {
        path: "/user/:id",
        component: () => import("pages/admin/UserPage.vue"),
        meta: { access: 1 },
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;
