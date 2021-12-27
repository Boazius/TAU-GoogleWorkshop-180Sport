<template>
<q-page>
  <div class="q-pa-md" style="max-width: 355px">
    <h3 class="group_header  q-mb-none">{{$t('app.groups')}}</h3>
    <q-list bordered separator class="list-items">
      <q-item v-for="group in groups" v-bind:key='group'  class="column">
        <q-btn 
        class="list-items"
        v-ripple
        unelevated 
         :label="$t('groups.name')+group.number+' - '+group.location"
         style="font-size:30px" 
        @click="goToGroupPage(group)"
        />
        

            <q-expansion-item
      class="item"
      expand-separator
      switch-toggle-side
      :label="$t('group.closest')"
    >
    <closest-training-list></closest-training-list>
    </q-expansion-item>
      </q-item>
    </q-list>
  </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import closestTrainingList from 'components/list/closestTrainingList.vue'

export default defineComponent({
  name: "groupList",
   components: { closestTrainingList},
data(){
  return {
    groups: [
    {number: 1, location: "תל אביב"},
    {number: 2, location: "הרצליה"},
    {number: 3, location: "רמת גן"},        
    ]
  }
},
  methods:{
    goToGroupPage(group){
      const groupdata = JSON.stringify(group);
      localStorage.setItem('groupdata', groupdata);      
      this.$router.push('/groups/:id'); 
    },  
    saveUser(group){
      groupdata = JSON.stringify(group);
      localStorage.setItem('groupdata', groupdata);
    },
  },
});
</script>



<style scoped lang="scss">
@import "assets/groupStyle.css"
</style>

