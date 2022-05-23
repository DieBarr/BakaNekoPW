$(document).ready(function () {
  $.get(
    "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/japan?unitGroup=metric&include=current&key=R4RLJV5TR6V7E44NPWVZMGVZ5&lang=es&contentType=json",
    function (data) {
      $("#clima").append(
        "<div class='col-12'><img src='../resources/bakaNeko2.svg' width='15%'><h1>BakaWeather</h1>El clima donde vive tu waifu (´,,•ω•,,)♡ ahorita es: <br><h1>  " +
          /*Propuesta, anadir condicional de temperatura, Ej: si hacen menos de 15C anadir al final "Enviale un chalequito pa que no pase frio („ಡωಡ„)"*/
          data.currentConditions.temp +
          "°C</h1>" +
          data.currentConditions.conditions +
          "<br>" +
          data.timezone +
          "<br>Temp Max: " +
          data.days[0].tempmax +
          "°<br>Temp Min: " +
          data.days[0].tempmin +
          "°</div>"
      );
    }
  );
});
