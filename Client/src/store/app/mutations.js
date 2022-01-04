//
// Mutations: Set
//
export const set = (state, data) => {
  Object.assign(state, data);
};

export const setMainMenu = (state, data) => {
  state.mainMenu = data;
};

export const resetState = (state) => {
  state.mainMenu = [
    {
      title: 'login',
      icon: "login",
      link: "/login",
    },
  ];
};
