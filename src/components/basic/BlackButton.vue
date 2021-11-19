<template>
  <q-btn
    no-caps
    class="text-no-wrap"
    padding="6px 10px"
    :color="color || 'black'"
    :type="type"
    :outline="outline || false"
    :flat="flat || false"
    :disable="disable"
    :loading="loading"
    @click="$emit('clicked', true)"
  >
    <slot></slot>
  </q-btn>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "BlackButton",
  props: ["type", "loading", "disable", "outline", "color", "flat"],
});
</script>
