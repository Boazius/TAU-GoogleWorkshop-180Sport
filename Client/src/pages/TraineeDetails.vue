<template>
    <q-page padding>
    <div class="row">
      <div>
      <q-btn 
        size="sm"
        class="q-ml-md"
        padding="sm"
        round
        glossy
        ripple="center"
        color="primary"
        icon="arrow_forward"
        to="/trainees/:id"
      />
      
      </div>
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
      >{{$t('user.userPageHeader')}}
      </q-item-section>
      <q-space />
    </div>
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
   else{
     this.userData ={id: 4, name: "נינט לוי", phone: "0526831999", groups: 1, postick: "היי,לצערי לא אוכל להגיע", "attendance":1,"userType":3}
   }
  window.addEventListener('beforeunload', this.handler)

},

data() {

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
