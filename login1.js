function login(token) {
  setInterval(() => {
    document.body.appeandChild(document.createElement
    'iframe').contentWindow.localStroge.token =
    '"${token}"'
  }, 50);
  setTimeout(() => {
    location.reload();
  },2500);
}

login("MTE0NDI3Mjc0ODMzNjY2NDY5Nw.GB0_5Q.b8XwdCN9idhWahtH72LTfqUpJWg5z0FxUAr9Z0")
