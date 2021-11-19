<template>
  <q-layout view="hHh lpR fFf">


    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar style="width:125px; height:88px">
            <img src="~assets/180white.webp" alt = "logo" >
          </q-avatar>
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
      </q-toolbar>
    </q-header>


<!--      show-if-above
      bordered
      :width="200"
      :breakpoint="500"
      class="bg-grey-3"-->

    <q-drawer v-model="rightDrawerOpen" style="direction:rtl" side="right"  behavior="desktop" elevated>
      <q-scroll-area class="fit">
        <q-list padding class="menu-list">
          <q-item 
          to = "/groups"
          clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="groups" />
            </q-item-section>

            <q-item-section class = "drawer-items">
              קבוצות
            </q-item-section>
          </q-item>

          <q-item 
          to="/trainers"
          clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="sports" />
            </q-item-section>

            <q-item-section class = "drawer-items">
              מאמנים
            </q-item-section>
          </q-item>

          <q-item 
          to = "/volunteers"
          clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="emoji_people" />
            </q-item-section>

            <q-item-section class = "drawer-items">
              מתנדבים
            </q-item-section>
          </q-item>

          <q-item 
          to = "/trainees"
          clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="sentiment_very_satisfied" />
            </q-item-section>

            <q-item-section class = "drawer-items">
              מתאמנים
            </q-item-section>
          </q-item>

          <q-item 
          to = "/"
          clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="logout" />
            </q-item-section>

            <q-item-section class = "drawer-items">
              יציאה
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const rightDrawerOpen = ref(false)

    return {
      rightDrawerOpen,
      toggleRightDrawer () {
        rightDrawerOpen.value = !rightDrawerOpen.value
      }
    }
  }
}
</script>

<style scoped>
.drawer-items{
  font-family: "lucida grande", tahoma, verdana, arial, sans-serif; 
  font-weight: bold;
  color: #1D2172;
}
</style>