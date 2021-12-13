<template>
  <div class="justify-center row align-center q-pa-md q-gutter-sm">
    <q-editor 
      v-model="editor"
      flat
      content-class="bg-amber-3"
      toolbar-text-color="white"
      toolbar-toggle-color="yellow-8"
      toolbar-bg="primary"
      :toolbar="[
        ['bold', 'italic', 'underline'],
        [{
          label: $q.lang.editor.formatting,
          icon: $q.iconSet.editor.formatting,
          list: 'no-icons',
          options: ['p', 'h3', 'h4', 'h5', 'h6', 'code']
        }]
      ]"
    />
    <q-btn
      size="22px"
      style="height:10px;"
      class="e-caret-up item-small q-px-md q-py-xs wrap"
      :label="$t('table.posticks')" >
        <q-icon name="message" size="lg" color="primary"/>
        <q-menu anchor="bottom start" v-model="label" >

        <q-banner class="bg-primary text-white">
            {{$t('app.confirmation.noNewPosts')}}
                <template v-slot:action>
    <q-btn flat color="white" :label="$t('app.confirmation.close')" v-close-popup/>
        </template>
        </q-banner>
    </q-menu>
    </q-btn>

</div>
</template>

<script>
import { ref } from 'vue'

export default {
    name:"EditorPosticks",
  setup () {
    return {
      editor: ref("")
    }
  }
}
</script>

<style scoped>
@import "assets/groupStyle.css";
</style>