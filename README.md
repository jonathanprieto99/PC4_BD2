# Base de Datos II: PC4
## Experimento 1
### Implementación
El procesamiento de las imágenes fue realizado con la librería externa `face_recognition`. Utilizando el método `load_image_file` se obtuvieron los objetos asociados a las imágenes, y utilizando el método `face_encodings` se obtuvieron sus vectores característicos. Para implementar la búsqueda KNN, se tomaron dos heurísticas para calcular la distancia: distancia euclidiana y de Manhattan. Estas se calcularon entre el vector característico de la foto de entrada y los vectores característicos de cada imagen de la colección. Para no repetir el proceso de procesamiento cada vez que se realiza una consulta, se guardaron los vectores de la colección en memoria secundaria, en el archivo `photo_index.json`. Toda la implementación se encuentra en el archivo `backend.py`
### Resultados
| Precision | ED | MD |
| --------- | -- | -- |
| K = 4     |  1 |  1 |
| K = 8     |  1 |  1 |
| K = 16    |  1 |  1 |

Para cada heurística se realizaron busquedas con tres fotos externas de tres personas diferentes. En este caso, tomamos a tres de las personas cuya colección de fotos era grande: Arnold Schwarzenegger, Andre Agassi y Atal Bihari. Luego se promediaron los resultados de las tres. Estos indican una precisión de 1 para todos los casos, lo cual puede deberse a dos factores: La colección de imágenes fue relativamente pequeña debido al tiempo de ejecución elevado para colecciones muy grandes, y la librería externa `face_recognition` es bastante eficaz, proporcionando data muy precisa. Por otro lado, cabe resaltar que varios estudios muestran que la distancia de Manhattan es más efectiva para la recuperación basada en contenido, y que la distancia euclidiana pierde precisión a medida que aumenta la cantidad de dimensiones.
## Experimento 2
### Implementación
### Resultados
Para los resultados no tomamos en cuenta el tiempo de proesamiento de las imagágenes y la obtención de sus vectores característicos. Se tomó únicamente en cuenta el tiempo de la obtención de los k elementos más cercanos. Estas pruebas se hicieron localmente y no sobre el código fuente de la aplicación web, ya que Heroku nos limitaba bastante. Para las mediciones del KNN'Secuencial, se agregó una variable N que definía la cantidad de fotos a tomar de la colección total. Luego, se usó la librería externa `time` y el método `time` para obtener el tiempo antes y después de la medición, y con estos calcular el tiempo de ejecución.
| Tiempo    | KNN-RTree | KNN-Secuencial |
| --------- | --------- | -------------- |
| N = 100   | 0.000447s |  0.36s         |
| N = 200   | 0.000919s |  0.39s         |
| N = 400   | 0.001824s |  0.42s         |
| N = 800   | 0.005463s |  0.50s         |
| N = 1600  |  1        |  0.61s         |
| N = 3200  |  1        |  1.16s         |
| N = 6400  |  1        |  1.66s         |
| N = 12800 |  1        |  1             |
