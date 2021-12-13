<template>
<q-list bordered class="rounded-borders" style="max-width: 600px">
        <q-item-label header
          >16.12.21

        </q-item-label>
        <q-separator spaced />
        <q-item v-for="item in closestList" :key="item">
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">{{item.name}}</span>
            </q-item-label>
          </q-item-section>

          <q-item-section side>
            <div class="column">
            <q-icon v-if='item.postick != ""' name="message" size="sm" color="primary"/>
            <q-menu icon="message" color="primary">
            <next-training-posticks :postick="item.postick"></next-training-posticks>
            </q-menu >
           </div>
          </q-item-section>
                    <q-item-section side>
          <div class="column">

            <q-chip
            dense
            style='width:60px;'
            class="text-center"
            text-color="white"
            :color="item.attendance==0 ? 'grey darken-1': item.attendance==1 ? 'green' : 'red' " 
            >
            <div  
 
            class="text-center full-width">
            {{item.attendance==0 ? $t('user.unknown'): item.attendance==1 ? $t('user.yes') : $t('user.no')}}
            </div>
            </q-chip>
          </div>
          </q-item-section>
        </q-item>
      </q-list>
</template>



<script>
import { defineComponent } from 'vue'
import { ref, onMounted } from "vue";
import {mockRows} from 'components/table/mockdata.js';
import NextTrainingPosticks from '../basic/NextTrainingPosticks.vue';
const closestList = mockRows;

export default defineComponent({
  components: { NextTrainingPosticks },
    name:"closestTrainingList",
   setup() {
    const loading = ref(false);
    
    function onRequest() {
      loading.value = true;
      setTimeout(() => {
          loading.value = false;
      }, 1500);
    }

    onMounted(() => {
       onRequest({ });
    });

    return {
      loading,
      closestList,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>