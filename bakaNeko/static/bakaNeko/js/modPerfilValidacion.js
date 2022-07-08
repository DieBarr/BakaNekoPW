var modifnombre = document.getElementById("modifnombre");
var mensaje = document.getElementById("warnings");
var regexnombre = /^\s+$/;
const validar2 = (event)  => {
    event.preventDefault();
  
    let mensajesMostrar = "";
    let entrar = false;

    let mensajeResgistrado = "";
    //Condicional para que el Asunto no tenga más de 100 caracteres
    if (regexnombre.test(modifnombre.value)){
      mensajesMostrar +=
        "<br><div class='alert alert-danger' role='alert'>Error: El nombre no puede contener solo espacios (╬ Ò﹏Ó)!</div>";
  
      entrar = true;
    }
    if (modifnombre.value.length > 16) {
   mensajesMostrar +=
        "<br><div class='alert alert-danger' role='alert'>Error: El nombre es muy largo (╬ Ò﹏Ó)!</div>";
  
      entrar = true;
    }
  if (modifnombre.value.length < 4) {
   mensajesMostrar +=
        "<br><div class='alert alert-danger' role='alert'>Error: El nombre es muy corto (╬ Ò﹏Ó)!</div>";
  
      entrar = true;
    }
    

  if (entrar) {
      mensaje.innerHTML = mensajesMostrar;
    }
    else {
  
      mensaje.innerHTML = mensajeResgistrado +=
        "<br><div class='alert alert-success' role='alert'>Tu nombre ha sido cambiado con éxito ☆*:.｡.o(≧▽≦)o.｡.:*☆!</div>";
  
      document.getElementById('forma-perfil').submit();  }
  };