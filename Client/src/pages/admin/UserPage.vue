<template>
<<<<<<< HEAD
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
          to="/trainees"
        />
=======
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
        to="/trainees"
      />
      
>>>>>>> origin/main
      </div>
      <q-item-section
        class="table_header wrap q-mb-sm"
        style="font-size: xx-large"
<<<<<<< HEAD
        >{{ $t("user.userPageHeader") }}
      </q-item-section>
      <q-space />
    </div>
    <user-credentials-list></user-credentials-list>
  </q-page>
=======
      >{{$t('user.userPageHeader')}}
      </q-item-section>
      <q-space />
    </div>
         <user-credentials-list :userData="userData"></user-credentials-list> 

    </q-page>
>>>>>>> origin/main
</template>

<script>
import UserCredentialsList from "components/list/UserCredentialsList.vue";

<<<<<<< HEAD
export default {
  name: "UserPage",
  data() {
    return {};
=======

export default defineComponent({
  name: "userPage",
created() {
    if(localStorage.getItem("userdata")){
        this.userData = JSON.parse(localStorage.getItem("userdata"));
   }
   else{
     this.userData ={}
   }
  window.addEventListener('beforeunload', this.handler)

},

data() {

    return {
        userData: undefined
    };
>>>>>>> origin/main
  },
  methods: {
    handler() {
      console.log(8);
      window.localStorage.removeItem('userdata');
    },
  },
  components: {
    UserCredentialsList,
  },
};
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
