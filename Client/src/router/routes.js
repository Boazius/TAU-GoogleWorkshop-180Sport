
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/groups', component: () => import('pages/admin/AllGroups.vue') },
      { path: '/groups/:id', component: () => import('pages/admin/Group.vue') },
      { path: '/trainers', component: () => import('pages/admin/Trainers.vue') },
      { path: '/trainers/:id', component: () => import('pages/Trainer.vue'), },
      { path: '/volunteers', component: () => import('pages/admin/Volunteers.vue') },
      { path: '/trainees', component: () => import('pages/admin/Trainees.vue'), },
      { path: '/trainees/:id', component: () => import('pages/Trainee.vue')},
      { path: '/trainees/:id/details', component: () => import('pages/TraineeDetails.vue')},
      { path: '/login', component: () => import('pages/login/UserLogin.vue') },
      { path: '/user/:id', component: () => import('pages/admin/UserPage.vue'), },

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
