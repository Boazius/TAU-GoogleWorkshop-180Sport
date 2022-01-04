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
  return state.editedUser;
}

export function getCurrentUser(state) {
  return state.user.currentUser;
}

export function isAuthenticated(state) {
  if (state.user.currentUser !== {} && state.user.authenticated == true) {
    return true;
  }
  return false;
}
