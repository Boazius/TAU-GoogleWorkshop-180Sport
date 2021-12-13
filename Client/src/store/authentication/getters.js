//
//  Getters: Error
//
export function error(state) {
  const { error } = state;
  return {
    has: error.show,
    message: error.message,
  };
}

export function getEditedUser(state) {
  console.log("getters", state.editedUser);
  return state.editedUser;
}
