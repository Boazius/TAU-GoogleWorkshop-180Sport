export default function() {
  return {
    error: {
      show: false,
      message: ''
    },
    user: {
      authenticated: false,
      currentUser: {},
      language: '',
    },
  };
}
