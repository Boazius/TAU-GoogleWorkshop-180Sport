<template>
  <q-table
    :rows="rows"
    :columns="columns"
    row-key="id"
    :pagination="pagination"
    :loading="loading"
    :filter="filter"
    @request="onRequest"
    binary-state-sort
    v-if="everthingIsReady"
  >
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td
          key="full_name"
          :props="props"

          class="cursor-pointer"
        >
          <q-item 
          v-if="userType == 1"          
          @click="goToUserPage(props.row)"
          clickable
          v-ripple 
          style="display: table-cell; vertical-align: end"> 
            {{ props.row.full_name }}
          </q-item>

          <q-item 
          v-if="userType == 2" 
          style="display: table-cell; vertical-align: end"> 
            {{ props.row.full_name }}
          </q-item>
        </q-td>
        <q-td key="user_type" :props="props" v-text="props.row.user_type == 3 ? $t('table.trainee') : $t('table.volunteer')" >
        </q-td>
        <q-td key="phone_number" :props="props" >
          {{ props.row.phone_number }}
        </q-td>
        <q-td key="group_ids" style="white-space: pre;" :props="props"
          >{{ getNames(props.row.group_ids) }}
        </q-td>
        <q-td key="email" :props="props"
          >{{ props.row.email }}
        </q-td>

      </q-tr>
    </template>
    <template v-slot:top>
      <table-top-buttons
        :tableType="this.tableType"
        v-if="!fromGroupPage"
        :rows="rows"
        :rowCount="rowCount"
        :loading="loading"
      ></table-top-buttons>
      <q-space />
      <q-input
        borderless
        dense
        debounce="300"
        color="primary"
        v-model="filter"
        outlined
        :placeholder="$t('table.search')"
      >
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </template>
  </q-table>
</template>

<script>
import { ref ,onMounted, defineComponent ,onUpdated} from "vue";
import { useQuasar } from "quasar";
import { userColumns , groupColumns} from "components/table/TableColumns.js";
import TableTopButtons from "components/table/TableTopButtons.vue";
import axios from "axios";
const serverUrl = "http://127.0.0.1:5000";
const id_token = localStorage.getItem("id_token");


export default defineComponent({
  name: "userTable",
  components: { TableTopButtons },
  props:["table_data", "fromGroupPage", "tableType"],



  methods: {
    goToUserPage(row) {
      const user ={id: row.id};
      localStorage.setItem('user', JSON.stringify(user));      
      this.$router.push(`/user/${user.id}`);

      // const user = JSON.parse(JSON.stringify(row));
      // this.$store.dispatch("authentication/setEditedUser", user);
    },
    // saveUser(row) {
    //   user = JSON.stringify(row);
    //   localStorage.setItem("userdata", user);
    // },
  },
  setup(props) {
    const userType = ref(1);
    const rows = ref([]);
    const filter = ref("");
    const loading = ref(false);
    const pagination = ref({
      sortBy: "desc",
      descending: false,
      page: 1,
      rowsPerPage: 10,
      rowsNumber: props.table_data.length,
    });
    const rowCount = ref(props.table_data.length);
    const $q = useQuasar();
    const columns = ref(props.fromGroupPage ? groupColumns : userColumns);
    const groupNames=ref();
    const everthingIsReady = ref(false);

    // emulate ajax call
    // SELECT * FROM ... WHERE...LIMIT...
    function fetchFromServer(startRow, count, filter, sortBy, descending) {
      //userType.value = getUserType(); // default val is 1 for admin, waiting for data in store in order to implement*/
      const data = filter
        ?props.table_data.filter((row) => row.full_name.includes(filter))
        :props.table_data.slice();

      // handle sortBy
      if (sortBy) {

        const sortFn =
          sortBy === "desc"
            ? descending
              ? (a, b) => (a.name > b.name ? -1 : a.name < b.name ? 1 : 0)
              : (a, b) => (a.name > b.name ? 1 : a.name < b.name ? -1 : 0)
            : descending
            ? (a, b) => parseFloat(b[sortBy]) - parseFloat(a[sortBy])
            : (a, b) => parseFloat(a[sortBy]) - parseFloat(b[sortBy]);
        data.sort(sortFn);
      }

      return data.slice(startRow, startRow + count);
    }
    async function getUserType(){
        //implement with api or get from store
    }

    // emulate 'SELECT count(*) FROM ...WHERE...'
     function getRowsNumberCount(filter) {
      if (!filter) {
        return props.table_data.length;
      }
      let count = 0;
      props.table_data.forEach((treat) => {
        if (treat.full_name.includes(filter)) {
          ++count;
        }
      });
     return count;
    }

    function onRequest(props) {
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      const filter = props.filter;
      loading.value = true;
      // emulate server
      setTimeout(() => {
        // update rowsCount with appropriate value
        pagination.value.rowsNumber = getRowsNumberCount(filter);
        

        // get all rows if "All" (0) is selected
        const fetchCount =
          rowsPerPage === 0 ? pagination.value.rowsNumber : rowsPerPage;

        // calculate starting row of data
        const startRow = (page - 1) * rowsPerPage;

        // fetch data from "server"
        const returnedData = fetchFromServer(
          startRow,
          fetchCount,
          filter,
          sortBy,
          descending
        );

        // clear out existing data and add new
        rows.value.splice(0, rows.value.length, ...returnedData);

        // don't forget to update local pagination object
        pagination.value.page = page;
        pagination.value.rowsPerPage = rowsPerPage;
        pagination.value.sortBy = sortBy;
        pagination.value.descending = descending;

        // ...and turn of loading indicator
        loading.value = false;
      }, 500);
    }
    async function getGroupsNames(){
          //get groups data from server
      const response = await axios.get(`${serverUrl}/admin/get_all_groups/`,{
          headers: { 
              'x-access-token': id_token,
          },
        })
        .then((res)=> res.data)
        .catch((error)=>{
            console.log(error);
            return error;
        });
      
      const groups =JSON.parse(JSON.stringify(response["list of group"]));
      groupNames.value = [groups.length+1]
      for (let i=0; i<groups.length; i++){
        groupNames.value[groups[i].id] = groups[i].day+"- "+groups[i].meeting_place+" "+groups[i].time
      }
      everthingIsReady.value=true;
    }



  function getNames(group_ids){
    const id_array = (group_ids+"").split(/,/)
    var str = "";
    for (let i=0; i<id_array.length; i++){
      str +=groupNames.value[parseInt(id_array[i])]+"";
      if(i!=id_array.length -1){
        str +="\n" 
      }
    }
    return str;
  }


    onMounted(() => {
      getGroupsNames();
      // get initial data from server (1st page)
      onRequest({
        pagination: pagination.value,
        filter: undefined,
      });
    });



    return {
      filter,
      loading,
      pagination,
      columns,
      rows,
      rowCount,
      onRequest,
      userType,
      getGroupsNames,
      getNames,
      everthingIsReady,
    };
  },
});
</script>

<style scoped>
@import "assets/tableStyle.css";
</style>
