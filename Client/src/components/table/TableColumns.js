export const userColumns = [
  { 
    name: 'full_name',
    required: true,
    label: "שם",
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
    {
    name: "phone_number",
    label: "טלפון",
    field: "phone_number",
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
    {
      name: "email",
      label: "מייל",
      field: "email",
      sortable: false,
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