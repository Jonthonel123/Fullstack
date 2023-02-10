var express = require("express");

// creando un aplicacion en express
var app = express();

// rutas
app.get("/", function (req, res) {
  res.send("Hola mundo con express");
});

app.get("/login", function (req, res) {
  res.send("Esta en la ventana de login");
});

// servidor de escucha, que desplegara las rutas en el el protocolo http

app.listen(3000, function () {
  console.log("La aplicacion esta en el puerto 3000");
});
