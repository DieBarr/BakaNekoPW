//Declarando de variables
var asunto = document.getElementById("asunto");
var imagen = document.getElementById("imagen_adj");
var desc = document.getElementById("desc_post");
var mensaje = document.getElementById("warnings");


//Accion al pulsar submit

const validar = (event)  => {
  event.preventDefault();

  let mensajesMostrar = "";
  let entrar = false;

  let mensajeResgistrado = "";
  //Condicional para que el Asunto no tenga más de 100 caracteres
  if (asunto.value.length > 100) {
 mensajesMostrar +=
      "<br><div class='alert alert-danger' role='alert'>Error: El Asunto no puede tener más de 100 caracteres (╬ Ò﹏Ó)!</div>";

    entrar = true;
  }
if (asunto.value.length < 0) {
 mensajesMostrar +=
      "<br><div class='alert alert-danger' role='alert'>Error: El Asunto no puede quedar vacio (╬ Ò﹏Ó)!</div>";

    entrar = true;
  }

if (entrar) {
    mensaje.innerHTML = mensajesMostrar;
  }
  else {

    mensaje.innerHTML = mensajeResgistrado +=
      "<br><div class='alert alert-success' role='alert'>Post creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!</div>";

    document.getElementById('forma-post').submit();  }
};
