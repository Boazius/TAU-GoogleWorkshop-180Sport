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
    name: "group",
    label: "קבוצה",
    field: "group",
    sortable: true,
    align:'center'
    },
      {
    name: "area",
    label: "איזור מגורים",
    field: "area",
    sortable: true,
    align:'left'
    },
  {
    name: "message",
    label: "הודעות חדשות",
    field: "message",
    align:'left'
    },
    {
    name: "comment",
    label: "פרסם הודעה למשתמש",
    field: "comment",
    align:'left'
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