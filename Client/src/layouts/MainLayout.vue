<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>{{ $t("app.mainHeading") }} </q-toolbar-title>

        <q-avatar style="width: 125px; height: 88px">
          <img src="~assets/images/logo-white-big.webp" alt="logo" />
        </q-avatar>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> {{ $t("app.menu.heading") }} </q-item-label>
        <EssentialLink
          v-for="link in menuLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
      <switch-language @onChangeLanguage="locale = $event"></switch-language>

      <!-- <q-select
          v-model="locale"
          :options="localeOptions"
          label="Quasar Language"
          dense
          borderless
          emit-value
          map-options
          options-dense
          style="min-width: 150px"
          class="q-pa-md"
        /> -->
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink.vue";
import SwitchLanguage from "components/basic/SwitchLanguage.vue";

import { computed } from "vue";
import { useStore } from "vuex";
import { defineComponent, ref } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
    SwitchLanguage,
  },
  //TODO: add watcher for lang (from getter) and set locale with it
  setup() {
    const leftDrawerOpen = ref(false);
    const store = useStore();
    const { locale } = useI18n({ useScope: "global" });

    return {
      locale,
      localeOptions: [
        { value: "en-US", label: "English" },
        { value: "he", label: "עברית" },
      ],
      menuLinks: computed(() => store.getters["app/getMenu"]),
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
  created() {
    //TODO: fix locale => how to use it in vue3?
    this.$store.dispatch("authentication/setLanguage");
  },
});
</script>
