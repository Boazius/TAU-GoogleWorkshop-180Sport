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

        <!-- <q-toolbar-title >{{ $t("app.mainHeading") }} </q-toolbar-title> -->
        <!-- <q-avatar style="width: 125px; height: 88px">
          <img src="~assets/images/logo-white-big.webp" alt="logo" clickable/>
        </q-avatar> -->
        <q-toolbar-title > </q-toolbar-title>
        <toolbar-routes-buttons></toolbar-routes-buttons>
        <!-- <a :href="'http://www.180sport.org'" target="_blank">
          <q-btn dense unelevated >
            <q-avatar square style="width: 50px; height: auto">
              <img src="~assets/images/logo-white-big2.webp" alt="logo" />
            </q-avatar>
          </q-btn>
        </a> -->

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
        <q-item clickable @click="onLogout" v-if="isAuthenticated">
          <q-item-section avatar>
            <q-icon name="logout" />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ $t("app.menu.logout") }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
      <switch-language
        @onChangeLanguage="onChangeLanguage($event)"
      ></switch-language>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink.vue";
import SwitchLanguage from "components/basic/SwitchLanguage.vue";
import toolbarRoutesButtons from "components/header/ToolbarRoutesButtons.vue"
import { computed, onBeforeMount } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { defineComponent, ref } from "vue";
import { useI18n } from "vue-i18n";

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
    SwitchLanguage,
    toolbarRoutesButtons,
  },
  setup() {
    const leftDrawerOpen = ref(false);
    const store = useStore();
    const router = useRouter();
    const { locale } = useI18n({ useScope: "global" });
    const isAuthenticated = computed(
      () => store.getters["authentication/isAuthenticated"]
    );

    const onLogout = async () => {
      await store.dispatch("authentication/logout");
      router.push({
        path: "/login",
      });
    };

    const onChangeLanguage = (lang) => {
      locale.value = lang;
      store.dispatch("authentication/setLanguage", lang);
    };

    onBeforeMount(async () => {
      locale.value = await store.dispatch("authentication/setLanguage");
    });

    return {
      locale,
      onBeforeMount,
      store,
      onLogout,
      onChangeLanguage,
      isAuthenticated,
      menuLinks: computed(() => store.getters["app/getMenu"]),
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
