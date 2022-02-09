<template>
  <div class="q-pa-md max-width">
    <div class="row justify-between items-baseline">
      <h3 class="group_header q-mb-none">{{ $t("app.groups") }}</h3>
      <add-group v-if="!fromTrainer" class="q-mb-sm"></add-group>
    </div>
    <h5 v-if="noGroups" class="group_header q-mb-none">
      {{ $t("groups.noGroups") }}
    </h5>
    <q-list bordered separator class="list-items">
      <q-item
        v-for="group in groups"
        v-bind:key="group"
        class="column col-md-7"
      >
        <div class="row justify-between">
          <q-btn
            align="left"
            class="list-items"
            v-ripple
            unelevated
            style="font-size: 30px"
            @click="goToGroupPage(group)"
          >
            {{
              group.day +
              " - " +
              " " +
              group.meeting_place +
              ", " +
              $t("dashboard.time") +
              ": " +
              group.time
            }}
            <!-- {{group.day+' - '+' '+group.meeting_place}}<br>{{$t('dashboard.time')+': '+ group.time}} -->
          </q-btn>
          <q-btn
            align="right"
            icon="edit"
            v-ripple
            unelevated
            v-if="!fromTrainer"
            @click="goToGroupDataPage(group)"
          >
          </q-btn>
        </div>

        <q-expansion-item
          class="item"
          expand-separator
          switch-toggle-side
          :label="$t('group.closest')"
        >
          <closest-training-list
            :group="group"
            :user="caller"
          ></closest-training-list>
        </q-expansion-item>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import closestTrainingList from "components/list/closestTrainingList.vue";
import AddGroup from "../../components/groups/AddGroup.vue";

export default defineComponent({
  name: "groupList",
  components: { closestTrainingList, AddGroup },
  props: ["groups", "user", "fromTrainer", "noGroups"],
  data() {
    return {
      caller: this.user,
    };
  },
  methods: {
    goToGroupPage(group) {
      const groupdata = JSON.stringify(group);
      localStorage.setItem("groupdata", groupdata);
      this.$router.push("/group");
    },
    goToGroupDataPage(group) {
      localStorage.setItem("groupId", JSON.stringify({ id: group.id }));
      this.$router.push("/group/details");
    },
  },
});
</script>

<style scoped lang="scss">
@import "assets/groupStyle.css";
</style>
