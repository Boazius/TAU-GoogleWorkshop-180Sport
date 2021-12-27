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
    name: "group_ids",
    label: "קבוצה",
    field: "group_ids",
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