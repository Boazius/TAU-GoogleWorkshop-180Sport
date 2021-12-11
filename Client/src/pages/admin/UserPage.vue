<template>
    <q-page padding>
        <h3 class="table_header">{{$t('user.userPageHeader')}}</h3>
         <user-credentials-list :userData="userData"></user-credentials-list> 
    </q-page>
</template>

<script>
import { defineComponent } from "vue";
import UserCredentialsList from "components/list/UserCredentialsList.vue";


export default defineComponent({
  name: "userPage",
created() {
    if(localStorage.getItem("userdata")){
        this.userData = JSON.parse(localStorage.getItem("userdata"));
   }
},

data() {
    console.log(8);

    return {
        userData: undefined
    };
  },
  components: {
    UserCredentialsList
  },
});
</script> 


<style scoped>
@import "assets/tableStyle.css";
</style>
