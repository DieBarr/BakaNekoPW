//En trabajo
//Activar pills desde el menu de la navbar
function triggerPill(registrarse) {
  if (registrarse) {
    document.getElementById("tab-register").click();
  } else {
    document.getElementById("tab-login").click();
  }
}
