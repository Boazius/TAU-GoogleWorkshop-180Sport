<template>
  <q-dialog :model-value="dialog" position="top">
    <q-banner inline-actions class="text-white bg-red">
      {{ $t(errorMessage) }}
      <template v-slot:action>
        <q-btn flat color="white" label="OK" @click="$emit('onClose', false)" />
      </template>
    </q-banner>
  </q-dialog>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ErrorMessagePopup",
  props: ["dialog", "errorMessage"],
  computed: {
    isDialog() {
      return this.dialog;
    },
  },
});
</script>

<style lang="scss" scoped>
.heading {
  font-size: 2em;
  max-width: 70vw;
}
</style>
