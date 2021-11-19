# 180Sport (180sport)

#Sport without borders

# A Project for the TAU Google workshop course.
# A Web app by Boaz, Gal, Dana, and Danielle for 180Sport: to schedule and manage an Attendence sheet of trainers, trainees, and volunteers

This web app has four different kinds of users:

Trainees:
  -will know who their trainers are in each group they are in
  -will know when and where is the next training session
  -will be able to mark their planned attendance: are they coming to the next training session or not.
  
Volunteers:
  -will be able to do the same things trainees do,
  -will also be able to see all trainees and volunteers in their groups.

Trainers:
  -will be able to do the same things volunteers do,
  -will also be able to mark attendance once the session starts
  -will be able to add notes about each trainee in their groups.
  -will be able to edit group session informaton: time and place, as well as any misc notes about it.
  
 Admins:
  -will be able to see every group and every user in it
  -will be able to add, edit, and remove users, and change their user type.
  -will be able to create new groups and delete/edit existing ones.
  
  
every user must login using google login/ email+password when entering the app, and then will be redirected to the corresponding page for them.


# Code Documentation:

This project was programmed using quasar.dev , Vue 3.
Source in Src folder.

* assets folder: images used for the website
* boot folder: for Vue Options API form, and other internal files.
* Components folder - for all quasar components used, such us buttons and headers.
* 



Google workshop website:
https://sites.google.com/view/cloudweb21a/Home
+ Week 5   - 17/11/2021       -  Milestone 1 (Proof Of Concept - Flow Demo)
+ Week 6   - 24/11/2021       -  UX Research
+ Week 7   -  1/12/2021        -  TBD
+ Week 8   - 15/12/2021       - Milestone 2 (Backend and prepratation for Mileston 3)
+ Week 9   - 5/1/2021           -   Milestone 3 (Final Presentations) 




##Usage instructions:

## Install the dependencies
```bash
yarn
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```

### Lint the files
```bash
yarn run lint
```

### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.conf.js](https://quasar.dev/quasar-cli/quasar-conf-js).
