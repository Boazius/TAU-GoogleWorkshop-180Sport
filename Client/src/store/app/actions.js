//
//  Action:
//
export async function setMainMenu({ commit }, userType) {
  // userType = 1;
  if (userType == 4) { //volunteer and trainee is same
    userType = 3;
  }

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
      link: "/trainer-groups",
    },
    {
      access: 3,
      title: "trainee",
      icon: "sentiment_very_satisfied",
      link: "/next-training",
    },
    {
      access: 0,
      title: "details",
      icon: "edit",
      link: "/details",
    },
  ];
  let activeMenu = menu.filter(
    (item) => item.access === userType || item.access === 0
  );

  commit("setMainMenu", activeMenu);
}
