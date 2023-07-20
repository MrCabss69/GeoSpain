# Geospain


Esta librería proporciona una forma sencilla de acceder y visualizar los datos geográficos de España a nivel de comunidades autónomas, provincias y municipios utilizando la librería GeoPandas.



## Funcionalidades



La librería proporciona las siguientes funcionalidades principales:



- **Filtrado de datos**: Permite filtrar los datos geográficos por comunidades autónomas, provincias y municipios.

- **Obtención de listados**: Ofrece la posibilidad de obtener listados de todas las comunidades autónomas, provincias y municipios de España.

- **Visualización de datos geográficos**: Ofrece la posibilidad de dibujar mapas de cualquier comunidad autónoma, provincia y municipio. También puede dibujar un mapa completo de España mostrando varias comunidades autónomas, provincias y municipios en colores distintos.


## Instalación



Antes de usar esta librería, necesitas instalar las dependencias necesarias. Puedes hacerlo con pip:

      
      pip install geopandas pandas matplotlib






Después, puedes instalar la librería de forma manual, descargando el código del repositorio, situándote en la carpeta y ejecutando 

      pip install -e .

Nota: debes asegurarte que la carpeta del repositorio que te has descargado, sea accesible desde el python path.



## Uso

Importa las clase en tu script:



      from geospain.geo import GeoData, GeoVisual



Crea una instancia de la clase `GeoData` para acceder a los datos geográficos:

      geodata = GeoData()



Para obtener un listado de todas las comunidades autónomas, provincias o municipios, puedes usar los métodos correspondientes:
      
      comunidades = geodata.obtener_comunidades_autonomas()
      provincias = geodata.obtener_provincias("Cataluña")
      municipios = geodata.obtener_municipios("Barcelona")



También puedes utilizar la clase `GeoVisual` para dibujar mapas. Por ejemplo, para dibujar un mapa de Cataluña, puedes hacer lo siguiente:

    
      geovisual = GeoVisual(geodata)
      geovisual.dibujar_comunidad_autonoma("Cataluña")



Para dibujar un mapa completo de España mostrando varias entidades, puedes utilizar el método `dibujar_mapa`:



    
      geovisual.dibujar_mapa(comunidades_autonomas=["Cataluña"], provincias=["Madrid"], municipios=["Valencia"])




## Aplicaciones



Esta librería puede ser de utilidad en múltiples contextos:



- **Análisis geoespacial**: Para el análisis geoespacial en contextos como la planificación urbanística, la gestión de recursos naturales o la investigación en geografía y ciencias ambientales.

- **Visualización de datos**: Para visualizar datos geoespaciales en proyectos de ciencia de datos y machine learning. Por ejemplo, se puede utilizar para visualizar el resultado de un modelo de predicción de precios inmobiliarios a nivel de municipio.

- **Educación**: Como recurso educativo para enseñar geografía, ciencias de la tierra, o programación con Python. Los docentes pueden usarlo para ilustrar las diferencias geográficas entre distintas regiones de España.

