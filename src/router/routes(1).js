
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/groups', component: () => import('pages/admin_groups.vue') },
      { path: '/groups/:id', component: () => import('pages/admin_group_page.vue') },

      { path: '/trainers', component: () => import('pages/admin_trainers.vue') },
      { path: '/volunteers', component: () => import('pages/admin_volunteers.vue') },
      { path: '/trainees', component: () => import('pages/admin_trainees.vue'), },
      { path: '/trainees/:id', component: () => import('pages/Trainee.vue')},
      { path: '/login', component: () => import('pages/login/UserLogin.vue') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
