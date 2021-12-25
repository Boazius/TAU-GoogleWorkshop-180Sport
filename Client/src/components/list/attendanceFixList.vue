<template>
    <q-list bordered class="rounded-borders" style="max-width: 600px">
        <q-item-label header>{{header}}</q-item-label>
          <template v-for="item in lastList">
          <q-item v-if='item.attendance==attendance' :key='item'>
          <q-item-section top>
            <q-item-label lines="1">
              <span class="item-small">{{item.full_name}}</span>
            </q-item-label>
          </q-item-section>
          <q-item-section side>
          <div class="text-grey-8 q-gutter-xs" >
              <q-btn v-if="attendance==0||attendance==2"
                color="green"
                outlined
                class="gt-xs"
                size="12px"
                flat
                dense
                label="סמן שנכח"
                icon="check"
              />
              <q-btn v-if="attendance==0||attendance==1"
                color="red"
                class="gt-xs"
                size="12px"
                flat
                dense
                label="סמן שלא נכח"
                icon="close"
              />
              </div>
          </q-item-section>
          </q-item>
        </template>
        </q-list>
</template>



<script>
import { defineComponent } from 'vue'
import { ref, onMounted } from "vue";
import {mockRows} from 'components/table/mockdata.js';
const lastList = mockRows;

export default defineComponent({
    name:"attendanceFixList",
    props:["header","attendance"],
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
      lastList,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
@import "assets/groupStyle.css";
</style>
