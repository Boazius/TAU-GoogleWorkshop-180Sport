export const userColumns = [
  { 
    name: 'full_name',
    required: true,
    label: "שם",
    align: 'left',
    field: row => row.full_name,
    format: val => `${val}`,
    sortable: true
  },
    {
    name: "phone_number",
    required: true,
    label: "טלפון",
    field: "phone_number",
    sortable: true,
    align:'left'
  },
    {
    name: "group_ids",
    required: true,
    label: "קבוצה",
    field: "group_ids",
    sortable: true,
    align:'left'
    },
    {
      name: "email",
      required: true,
      label: "מייל",
      field: "email",
      sortable: false,
      align:'left'
      },


];
export const groupColumns = [
  { 
    name: 'full_name',
    required: true,
    label: "שם",
    align: 'left',
    field: row => row.full_name,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: "user_type",
    label: "מתאמן/מתנדב",
    field: "user_type",
    sortable: false,
    align:'left'
    },
    {
    name: "phone_number",
    required: true,
    label: "טלפון",
    field: "phone_number",
    sortable: true,
    align:'left'
  },
    {
    name: "group_ids",
    required: true,
    label: "קבוצה",
    field: "group_ids",
    sortable: true,
    align:'left'
    },
    {
      name: "email",
      required: true,
      label: "מייל",
      field: "email",
      sortable: false,
      align:'left'
      },
];