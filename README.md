Este proyecto ayuda con la tarea repetitiva de ajustar la estructura de los archivos json para transmitir mediante la API de ministerio de salud, funciona para los archivos json cuya estructura esta ajustada para la transmisión mediante el validador local del ministerio 
ya que estos dentro no cuentan con las propiedades "xmlFevFile","codigoUnicoValidacion" y la propiedad "rips" el cual es un arreglo que contiene la información de los servicios prestados por cada usuario.

Este proyecto procesa el archivo json y adiciona las propiedades mencionadas asi como encripta en base 64 el archivo xml de la factura para almacenarlo dentro de su respectiva propiedad, lo cual lo hace útil para tareas repetitivas dentro de las cuales se debe de hacer manualmente
cada uno de estos pasos para poder realizar transmisión de la información y aun más importante poner en riesgo la información que se desea codificar en páginas dentro de las cuales se desconoce su Código.

¿Cómo pueden comenzar los usuarios con el proyecto?

Para usar este proyecto se necesita tener instalado Python en el equipo y ejecutar el archivo creado, este comenzara creado la respectiva carpeta dentro de la cual se deben almacenar los archivos xml y json a ajustar y posteriormente continuar el proceso para que el programa
concatene el contenido en un archivo json nuevo.
