# Proyecto Final Grafos y Algoritmos

En este repositorio se encontrarán los códigos utilizados para las distintas opciones de modelos que se propusieron en el proyecto final del curso de Grafos y Algoritmos. Estos códigos, pueden ser ejecutados directamente en IBM CPLEX Optimization Studio, o en cualquier software de optimización con el debido cambio de lenguaje al del software a utilizar.

## Instrucciones de instalación.

Para el proyecto final, se utilizó el software de IBM CPLEX Optimization Studio, el cual puede ser descargado desde el siguiente [link](https://community.ibm.com/community/user/datascience/blogs/xavier-nodet1/2020/07/09/cplex-free-for-students). Se debe registrar con el correo de la universidad y se enviarán correos para confirmar que eres estudiante. Finalmente, ellos envían un correo con el URL que permite descargar el sofware que descarga el CPLEX y posteriormente realizar los pasos de la instalación.

Por otro lado, para buscar la distancia que hay entre dos puntos geográficos se utilizó la imagen del backend de [Project OSRM](https://github.com/Project-OSRM/osrm-backend) en docker. Las instrucciones de instalación están dentro de su repositorio en GitHub. Además, para poder obtener las calles de santiago, utilizamos una imagen de OpenStreetMap, la cual puede ser descargada desde [aquí](https://download.geofabrik.de/south-america/chile-latest.osm.pbf).

## Archivos

Dentro de este repositorio, existen 3 archivos:
1. colegios.csv
2. cuadras_maipu.csv
3. distances.csv

El primer archivo contiene las coordenadas y nombres de los 63 colegios que utilizamos como centros de votación en la comuna de Maipú. El segundo archivo contiene las coordenadas de los centroides de todas las cuadras de la comuna de Maipú junto a la cantidad de personas que viven en cada cuadra. El tercer archivo, es el resultado obtenido de **Project OSRM**, que corresponde a la distancia que hay entre cada cuadra y los 63 puntos de votación.
