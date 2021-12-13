export const userColumns = [
  { 
    name: 'name',
    required: true,
    label: "שם",
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
    {
    name: "phone",
    label: "טלפון",
    field: "phone",
    sortable: true,
    align:'center'
  },
    {
    name: "groups",
    label: "קבוצה",
    field: "groups",
    sortable: true,
    align:'center'
    },


];
export const trainerColumns = [
  { name: 'name',
    required: true,
    label: "שם",
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: "phone",
    label: "טלפון",
    field: "phone",
    sortable: false,
    align:'center'

  },
    {
    name: "groups",
    label: "קבוצות",
    field: "groups",
    sortable: false,
    align:'left'
  },
];