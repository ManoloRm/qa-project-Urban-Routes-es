Urban Routes pruebas automaticas

Requisitos para replicar las pruebas.
  tener instalado pycharm que es donde se ejecutaran dichas pruebas
  instalar selenium y pytest para pycharm esto se puede hacer desde el mismo pycharm
  corroborar que el servidor este listo para actualizar la url

Pasos para repolicar las preubas
    Abriri los archivos
    abrir la pagina web de la app
    en el archivo data es necesario actualizar la url del servidor que es la url de la pag web
    ejecutar la o las pruebas deseadas
Ejecutar
  
Es necesario actualizar la url del sitio para que las preubas funcionen, dicha url esta en el archivo data ya que se uso la estructura POM no se teiene que declarar 
ninguna variable o busqueda de algun elemento de la app en el archiuvo main, todas las funciones y/o elementos estan en el archicvo pages, al igual se uso selenium para 
poder interactuar con la pagina web simulando la inteccion de un usuario para generear acciones de parte de la aplicaicón web.

En el caso de que la instalación de los driver para el controlador web para selenium no sea exitoso, se puede importar la paqueteria desde pycharm para no tener problemas
al momento de ejecutar codigo de selenium.
