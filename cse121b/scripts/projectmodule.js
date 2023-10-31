export function alertMessage(message, duration = 10000) {
    const alert = document.createElement("p");
    alert.innerHTML = message;
    alert.setAttribute(
      "style",
      "background-color:lightpink; border: 1px solid red; position:absolute; top:0; left:0; right:0; padding: 1em;"
    );
    document.body.prepend(alert);
    setTimeout(function () {
      document.body.removeChild(alert);
    }, duration);
  }