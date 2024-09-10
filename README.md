# Final
Presentacion de Sistema Web para registro de patentes

La aplicación es un servidor web que administra el seguimiento de autos a través de su patente para poder llevar el control medido y cobrarle.
 
El usuario sube una imagen de la patente por medio de su teléfono al sitio, donde se procede a sacarle los metadatos a las fotos y se obtiene la patente del vehículo y su ubicación guardándose en una base de datos. Luego empieza a correr el tiempo hasta que la persona se vaya del lugar y donde se corta y se le genera el ticket con lo que tiene que pagar.

Por otra lado se quiere agregar más módulos para el mismo sistema por ejemplo que se pueda hacer un seguimiento de esa patente usando sus ubicaciones. De esta manera si se pudiera escalar se podría llegar a hacer un sistema de seguimiento en áreas más grandes como una ciudad en caso de un auto robado o seguimiento por otras razones.

Arquitectura

![Arquitectura1](https://github.com/user-attachments/assets/ba5ae3fc-3a2c-478d-a956-5721583feca4)
![Arquitectura2](https://github.com/user-attachments/assets/0653fc59-361e-443b-bd9d-fe5c915ba628)

Cumplimientos:

Uso de Sockets con conexión de clientes múltiples de manera concurrente:
	-Está utilizando aiohttp, que es una biblioteca para construir servidores HTTP que maneja múltiples conexiones concurrentes de manera asíncrona.

Uso de mecanismos de IPC (Inter-Process Communication):
	-Está utilizando multiprocessing.Queue para comunicarte entre procesos. En el código, image_queue es una cola que se usa para enviar rutas de imágenes entre el proceso principal y el proceso hijo (patente_worker)

Uso de asincronismo de I/O:
	-Está utilizando async y await con aiohttp para manejar las solicitudes HTTP de manera asíncrona. Además, aiofiles se utiliza para la lectura asíncrona de archivos

Uso de cola de tareas distribuidas:
	-Aunque estoy usando una cola (image_queue) para gestionar las tareas entre procesos, no utilizo  una cola de tareas distribuida como Celery o RQ. La cola es local a un solo proceso de Python y no está diseñada para distribuir tareas entre múltiples servidores o procesos en diferentes máquinas.

Parseo de argumentos por línea de comandos
	-Está utilizando argparse para parsear el puerto desde la línea de comandos.

 Manejo de SSL/TLS
  -Se utiliza certificados para conexiones seguras

  Fuente del lector de patente 
  https://github.com/ankandrew/fast-plate-ocr

  Uso de Docker
    -La Aplicacion se encuentra dockerizada para correr directamente

  Uso de Base de datos
    -Todos los registros se guardan en una base de datos relacional de MySQL

