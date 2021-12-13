<template v-slot:top>
  <section>
    <q-btn class="q-ml-sm" color="primary" :loading="loading" :label="$t('table.add')" no-caps @click="addUser"  to="/user/:id" />
    <!-- <q-btn class="q-ml-sm" color="primary" :disable="loading" :label="$t('table.delete')" no-caps @click="removeRow" />
    <q-btn class="q-ml-sm" color="primary" :disable="loading" icon-right="archive" :label="$t('table.export')" no-caps @click="exportTable" /> -->
  </section>
</template>



 <script > 

import { defineComponent } from "vue";

// }     
export default 
defineComponent({
  name: "TableTopButtons",
  props:["type"],
  data(){
    return{
      loading: false
    };
  },

  methods: {
    addUser (){
      this.loading = true
      setTimeout(() => {
        
        this.loading = false
      }, 500)
      // if (type == 2){
      //  const user = JSON.stringify({id, name: "", phone: "", groups, postick: "", attendance,userType:type});

      // }
      // else if(type == 3| type == 4){
      // const user = JSON.stringify({id, name: "", phone: "", groups,area:"", postick: "", attendance,userType:type});

      // }
      // else {
      //   const user = {};
      // }
      // localStorage.setItem('userdata', user);      
      // this.$router.push('/user/:id'); 
  },

    },   
 
});
</script>



