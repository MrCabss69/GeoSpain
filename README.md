# Librería GeoPandas España



Esta librería proporciona una forma sencilla de acceder y visualizar los datos geográficos de España a nivel de comunidades autónomas, provincias y municipios utilizando la librería GeoPandas.



## Funcionalidades



La librería proporciona las siguientes funcionalidades principales:



- **Filtrado de datos**: Permite filtrar los datos geográficos por comunidades autónomas, provincias y municipios.

- **Obtención de listados**: Ofrece la posibilidad de obtener listados de todas las comunidades autónomas, provincias y municipios de España.

- **Visualización de datos geográficos**: Ofrece la posibilidad de dibujar mapas de cualquier comunidad autónoma, provincia y municipio. También puede dibujar un mapa completo de España mostrando varias comunidades autónomas, provincias y municipios en colores distintos.



## Aplicaciones



Esta librería puede ser de utilidad en múltiples contextos:



- **Análisis geoespacial**: Para el análisis geoespacial en contextos como la planificación urbanística, la gestión de recursos naturales o la investigación en geografía y ciencias ambientales.

- **Visualización de datos**: Para visualizar datos geoespaciales en proyectos de ciencia de datos y machine learning. Por ejemplo, se puede utilizar para visualizar el resultado de un modelo de predicción de precios inmobiliarios a nivel de municipio.

- **Educación**: Como recurso educativo para enseñar geografía, ciencias de la tierra, o programación con Python. Los docentes pueden usarlo para ilustrar las diferencias geográficas entre distintas regiones de España.



## Instalación



Antes de usar esta librería, necesitas instalar las dependencias necesarias. Puedes hacerlo con pip:



\```

pip install geopandas pandas matplotlib

\```



## Uso



Primero, puedes importar la librería en tu script de Python:



\```python

import os

import geopandas as gpd

import matplotlib.pyplot as plt

import pandas as pd

\```



Luego, puedes crear una instancia de la clase `GeoData` para acceder a los datos geográficos:



\```python

limites_espana = os.path.join(os.path.dirname(__file__), 'recursos', 'gadm41_ESP_0.shp')

limites_municipios = os.path.join(os.path.dirname(__file__), 'recursos', 'gadm41_ESP_4.shp')



geodata = GeoData()

\```



Para obtener un listado de todas las comunidades autónomas, provincias o municipios, puedes usar los métodos correspondientes:



\```python

comunidades = geodata.obtener_comunidades_autonomas()

provincias = geodata.obtener_provincias("Cataluña")

municipios = geodata.obtener_municipios("Barcelona")

\```



Finalmente, puedes utilizar la clase `GeoVisual` para dibujar mapas. Por ejemplo, para dibujar un mapa de Cataluña, puedes hacer lo siguiente:



\```python

geovisual = GeoVisual(geodata)

geovisual.dibujar_comunidad_autonoma("Cataluña")

\```



Para dibujar un mapa completo de España mostrando varias entidades, puedes utilizar el método `dibujar_mapa`:



\```python

geovisual.dibujar_mapa(comunidades_autonomas=["Cataluña"], provincias=["Madrid"], municipios=["Valencia"])

\```
