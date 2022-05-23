var nombreUsuario = document.getElementById("registerUsername");
var clave = document.getElementById("registerPassword");
var claveRepetir = document.getElementById("registerRepeatPassword");
var correo = document.getElementById("registerEmail");
var checkBox = document.getElementById("registerCheck");
// Get the output text

const form = document.getElementById("forma-registro");
var mensaje = document.getElementById("warnings");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let mensajesMostrar = "";
  let entrar = false;
  let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
  let regexPassword = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
  let mensajeResgistrado = "";
  if (nombreUsuario.value.length < 4 || nombreUsuario.value.length > 12) {
    mensajesMostrar +=
      "<div class='alert alert-danger'> <strong>El nombre de usuario no es válido (＃`Д´) !</strong> </div>";
    entrar = true;
  }

  if (!regexEmail.test(correo.value)) {
    mensajesMostrar +=
      "<div class='alert alert-danger'> <strong>El correo no es válido ((╬◣﹏◢)) !</strong> </div>";
    entrar = true;
  }

  if (!regexPassword.test(clave.value)) {
    mensajesMostrar +=
      "<div class='alert alert-danger'> <strong>La contraseña debe ser mayor a 8 caracteres y debe tener almenos un numero, una letra mayuscula y una minuscula ＼(º □ º l|l)/ !</strong> </div>";
    entrar = true;
  }

  if (clave.value != claveRepetir.value) {
    mensajesMostrar +=
      "<div class='alert alert-danger'> <strong>Las contraseñas no coinciden ٩(╬ʘ益ʘ╬)۶ !</strong> </div>";
    entrar = true;
  }
  if (checkBox.checked == false) {
    mensajesMostrar +=
      "<div class='alert alert-danger'> <strong>Debes aceptar los terminos y condiciones de BakaNeko (｡•́︿•̀｡) </strong> </div>";
    entrar = true;
  }
  if (entrar) {
    mensaje.innerHTML = mensajesMostrar;
  } else {
    mensaje.innerHTML = mensajeResgistrado +=
      "<div class='alert alert-success'> <strong>Teregistraste correctamente, felicidades (っ˘ω˘ς ) !</strong> </div> <br>";
  }
});
