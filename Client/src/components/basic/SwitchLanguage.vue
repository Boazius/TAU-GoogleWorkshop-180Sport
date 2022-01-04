<template>
  <div class="column q-pa-sm full-width">
    <h5 class="text-grey-7 text-18 q-ma-sm">
      {{ $t("app.languageHeading") }}
    </h5>
    <q-list>
      <q-item
        clickable
        v-ripple
        :class="{ 'bg-grey-2 text-bold': language == 'he' }"
        @click="onChangeLanguage('he')"
        class="switcher-button text-body-1 q-px-sm"
      >
        <q-item-section avatar>
          <q-icon
            v-if="language === 'he'"
            size="20px"
            name="done"
            color="primary"
          />
        </q-item-section>
        <q-item-section>עברית</q-item-section>
      </q-item>
      <q-item
        clickable
        v-ripple
        class="switcher-button text-body-1 q-px-sm"
        :class="{ 'active-button bg-grey-2 text-bold': language == 'en-US' }"
        @click="onChangeLanguage('en-US')"
      >
        <q-item-section avatar>
          <q-icon
            v-if="language === 'en-US'"
            size="20px"
            name="done"
            color="primary"
          />
        </q-item-section>
        <q-item-section>English</q-item-section>
      </q-item>
    </q-list>
  </div>
</template>


<script>
import { mapState } from "vuex";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SwitchLanguage",
  props: ["showChangeLang"],

  computed: {
    ...mapState({
      language: (state) => state.authentication.user.language,
    }),
  },
  methods: {
    onChangeLanguage(lang) {
      this.$emit('onChangeLanguage',lang);
      // this.$store.dispatch("authentication/setLanguage", lang);
    },
  },
});
</script>

<style lang="scss" scoped>
.switcher-button {
  border-top: 1.5px solid #ededed;
  border-bottom: 1.5px solid rgba(0, 0, 0, 0.1);
  letter-spacing: 0.5px;
}
.active-button {
  border-bottom: none;
  border-top: none;
}
</style>
