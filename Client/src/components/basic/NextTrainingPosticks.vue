<template>
  <div class="justify-center row align-center q-pa-md q-gutter-sm">
    <q-banner class="bg-primary text-white">
            {{postick}}
                <template v-slot:action>
        </template>
        </q-banner>
    
    
        <q-menu anchor="bottom start" v-model="label" >
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
    <q-btn flat color="white" :label="$t('app.confirmation.close')" v-close-popup/>
      
    </q-menu>

</div>
</template>

<script>
import { ref } from 'vue'

export default {
    name:"NextTrainingPosticks",
    props:['postick'],
    
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