//
//  Getters: Error
//
export function error(state) {
  const { error } = state;
  return {
    has: error.show,
    message: error.message
  };
}
