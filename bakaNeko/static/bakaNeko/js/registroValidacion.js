var nombreUsuario = document.getElementById("user_name");
var clave = document.getElementById("password");
var claveRepetir = document.getElementById("password2");
var correo = document.getElementById("email");
var checkBox = document.getElementById("aceptarCheck");
// Get the output text

var mensaje = document.getElementById("warnings") ;

const validar = (event)  => {

  event.preventDefault();
  let mensajesMostrar = "";
  let entrar = false;
  let regexEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g;
  let regexPassword = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
  let mensajeResgistrado = "";
  if (nombreUsuario.value.length < 4 || nombreUsuario.value.length > 20) {
    mensajesMostrar +=
      "<div class='alert alert-danger'> <strong>El nombre de usuario no es válido (＃`Д´) !</strong> </div>";
    entrar = true
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
"<div class='spinner-border text-success'></div>";
    document.getElementById('forma-registro').submit();
  }

};
