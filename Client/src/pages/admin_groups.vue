<template>
<q-page>
  <div class="q-pa-md" style="max-width: 355px">
    <h3 class="group_header  q-mb-none">{{$t('app.groups')}}</h3>
    <q-list bordered separator class="list-items">
      <q-item to="/groups/id" clickable v-ripple>
        <q-item-section>קבוצה 1 - תל אביב</q-item-section>
      </q-item>

      <q-item to="/groups/id" clickable v-ripple>
        <q-item-section>
          <q-item-label>קבוצה 2 - רמת גן</q-item-label>
        </q-item-section>
      </q-item>

      <q-item to="/groups/id" clickable v-ripple>
        <q-item-section>
          <q-item-label>קבוצה 3 - הרצליה</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
  </q-page>
</template>
<style scoped lang="scss">
.group_header,
.q-table th {
  font-weight: bold;
}

.list-items{
    font-weight: bold;
  font-size: large;
}
</style>

