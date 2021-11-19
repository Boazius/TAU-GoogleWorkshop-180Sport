
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/admin_login.vue') },
      { path: '/groups', component: () => import('pages/admin_groups.vue') },
      { path: '/groups/id', component: () => import('pages/admin_group_page.vue') },

      { path: '/trainers', component: () => import('pages/admin_trainers.vue') },
      { path: '/volunteers', component: () => import('pages/admin_volunteers.vue') },
      { path: '/trainees', component: () => import('pages/admin_trainees.vue') }

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
