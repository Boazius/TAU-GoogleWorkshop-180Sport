//
//  Mutations: Set Language
//
export const setLanguage = (state, payload) => {
  state.user.language = payload;
};

export const setEditedUser = (state, payload) => {
  state.editedUser = JSON.parse(JSON.stringify(payload));
};
