<template>
<q-page>
  <div class="q-pa-md" style="max-width: 355px">
    <h3 class="group_header  q-mb-none">{{$t('app.groups')}}</h3>
    <q-list bordered separator class="list-items">
      <q-item v-for="group in groups" v-bind:key='group' to="/groups/id" :props="group" clickable v-ripple>
        <q-item-section>
          <q-item-label>{{$t('groups.name')+group.number}}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "groupList",
data(){
  return {
    groups: [
    {number: 1, location: "תל אביב"},
    {number: 2, location: "הרצליה"},
    {number: 3, location: "רמת גן"},        
    ]
  }
}
});
</script>



<style scoped lang="scss">
@import "assets/groupStyle.css"
</style>

