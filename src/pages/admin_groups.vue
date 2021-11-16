<template>
  <div class="q-pa-md float-right" style="max-width: 350px">
    <h3 class="group_header  q-mb-none">קבוצות</h3>
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


    <!-- <q-list bordered class="rounded-borders reverse row  ">
      <q-expansion-item
        expand-separator
        label="קבוצה 1"
      >
        <q-card>
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-expansion-item
        expand-separator
        label="קבוצה 2"
      >
        <q-card>
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-expansion-item
        expand-separator
        icon="drafts"
        label="קבוצה 3"
      >
        <q-card>
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>

    </q-list> -->
  </div>
</template>
<style>
.group_header,
.q-table th {
  font-weight: bold;
}

.list-items{
    font-weight: bold;
  font-size: large;
}
</style>

