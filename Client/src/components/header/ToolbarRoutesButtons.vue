<template>
<div class="row justify-start ">

    <a href="http://www.instagram.com/180sport" target="_blank" icon="instagram">
        <q-btn dense unelevated size="xl" class="q-mr-sm ">
        <i class="fab fa-instagram"  style="color: white;" ></i>
        </q-btn>
    </a>
    <a href="https://www.facebook.com/180sport/" target="_blank" icon="facebook">
        <q-btn dense unelevated size="xl"  class="q-mr-sm ">
        <i class="fab fa-facebook-f"  style="color: white;" ></i>
        </q-btn>
    </a>
    <a href='http://www.180sport.org' target="_blank">
        <q-btn dense unelevated >
            <q-avatar square style="width: 50px; height: auto">
                <img src="~assets/images/logo-white-big2.webp" alt="logo" />
            </q-avatar>
        </q-btn>
    </a>
</div>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "toolbarRoutesButtons",
});
</script>