//
//  Action:
//
export async function setMainMenu({ commit }, userType) {
  debugger;
  let menu = [
    {
      access: 1,
      title: "groups",
      icon: "groups",
      link: "/groups",
    },
    {
      access: 1,
      title: "trainers",
      icon: "sports",
      link: "/trainers",
    },
    {
      access: 1,
      title: "volunteers",
      icon: "emoji_people",
      link: "/volunteers",
    },
    {
      access: 1,
      title: "trainees",
      icon: "sentiment_very_satisfied",
      link: "/trainees",
    },
    {
      access: 2,
      title: "trainer",
      icon: "sports",
      link: "/trainers/1",
    },
    {
      access: 3,
      title: "trainee",
      icon: "sentiment_very_satisfied",
      link: "/trainees/1",
    },
    {
      access: 4,
      title: "traineeDetails",
      icon: "edit",
      link: "/trainees/1/details",
    },
    {
      access: 4,
      title: "login",
      icon: "login",
      link: "/login",
    },
    {
      access: 4,
      title: "logout",
      icon: "logout",
      link: "/logout",
    },
  ];

  const activeMenu = menu.filter((item) => userType <= item.access);
  commit("setMainMenu", activeMenu);
}
