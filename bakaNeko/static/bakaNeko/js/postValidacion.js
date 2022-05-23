//Declarando de variables
var asunto = document.getElementById("asunto");
var imagen = document.getElementById("imagen_adj");
var desc = document.getElementById("desc_post");
var mensaje = document.getElementById("mensaje");

//Declarando variable del formulario
const post_form = document.getElementById("post_form");

//Accion al pulsar submit
post_form.addEventListener("submit", (e) => {
  e.preventDefault();
  let mostrarMsg = "";
  //Condicional para que el Asunto no tenga más de 100 caracteres
  if (asunto.value.length > 100) {
    mensaje.innerHTML =
      "<br><div class='alert alert-danger' role='alert'>Error: El Asunto no puede tener más de 100 caracteres (╬ Ò﹏Ó)!</div>";
  } else {
    mensaje.innerHTML =
      "<br><div class='alert alert-success' role='alert'>Post creado correctamente felicidades ☆*:.｡.o(≧▽≦)o.｡.:*☆!</div>";
  }
});
