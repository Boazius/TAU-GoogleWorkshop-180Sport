<template>
  <div class="row  q-gutter-x-md items-center bg-grey-2 q-pa-md">
    <q-list separator class="list-items">

        <q-item>
                <q-item-label>{{$t("table.name")}}
                  <q-input class="list-items" v-model="name" type="text" />
            </q-item-label>
      </q-item>
              <q-item>
                <q-item-label>{{$t("table.phone")}}
                  <q-input class="list-items" v-model="phone" type="text" />
            </q-item-label>
      </q-item>
              <q-item>
                <q-item-label>{{$t("table.groups")}}
                  <q-input class="list-items" v-model="groups" type="text" />
            </q-item-label>
      </q-item>

        <q-btn class="q-ml-sm" color="primary" :disable="loading" :label="$t('user.delete')" no-caps />

    </q-list>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserCredentialsList",
  props: ["userData"],
  data() {
    return {
      name: this.userData.name,
      phone: this.userData.phone,
      groups: [this.userData.groups],
      livingArea: this.userData.area,
    };
  },
});
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css"
</style>
