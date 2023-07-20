import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import os

limites_espana = os.path.join(os.path.dirname(__file__), 'recursos', 'gadm41_ESP_0.shp')
limites_municipios = os.path.join(os.path.dirname(__file__), 'recursos', 'gadm41_ESP_4.shp')

class GeoData:
    def __init__(self):
        self.datos_espana = gpd.read_file(limites_espana)
        self.datos = gpd.read_file(limites_municipios)

    def filtrar_datos(self, column_name, name_list):
        if name_list:
            return self.datos[self.datos[column_name].isin(name_list)]
        else:
            return pd.DataFrame()

    def obtener_datos(self):
        return self.datos

    def obtener_comunidades_autonomas(self):
        return sorted(self.datos['NAME_1'].unique())

    def obtener_provincias(self, comunidad_autonoma):
        datos_ca = self.datos[self.datos['NAME_1'] == comunidad_autonoma]
        return sorted(datos_ca['NAME_2'].unique())

    def obtener_municipios(self, provincia):
        datos_provincia = self.datos[self.datos['NAME_2'] == provincia]
        return sorted(datos_provincia['NAME_4'].unique())

    def obtener_municipio(self, municipio):
        return self.datos[self.datos['NAME_4'] == municipio]

    def obtener_limites(self, comunidad_autonoma=None, provincia=None, municipio=None):
        if municipio is not None:
            datos = self.datos[self.datos['NAME_4'] == municipio]
        elif provincia is not None:
            datos = self.datos[self.datos['NAME_2'] == provincia]
        elif comunidad_autonoma is not None:
            datos = self.datos[self.datos['NAME_1'] == comunidad_autonoma]
        else:
            return None

        if not datos.empty:
            return datos.geometry.bounds
        else:
            return None


class GeoVisual:
    def __init__(self, geodata):
        self.geodata = geodata

    def dibujar_comunidad_autonoma(self, comunidad_autonoma):
        datos_ca = self.geodata.datos[self.geodata.datos['NAME_1']
                                      == comunidad_autonoma]
        if datos_ca.empty:
            print(
                f"No hay datos disponibles para la comunidad autónoma: {comunidad_autonoma}")
        else:
            datos_ca.boundary.plot()
            plt.show()

    def dibujar_provincia(self, provincia):
        datos_provincia = self.geodata.datos[self.geodata.datos['NAME_2'] == provincia]
        if datos_provincia.empty:
            print(f"No hay datos disponibles para la provincia: {provincia}")
        else:
            datos_provincia.boundary.plot()
            plt.show()

    def dibujar_municipio(self, municipio):
        datos_municipio = self.geodata.datos[self.geodata.datos['NAME_4'] == municipio]
        if datos_municipio.empty:
            print(f"No hay datos disponibles para el municipio: {municipio}")
        else:
            datos_municipio.boundary.plot()
            plt.show()

    def dibujar_mapa(self, comunidades_autonomas=[], provincias=[], municipios=[]):
        fig, ax = plt.subplots(1, 1)
        
        # Dibujar contorno de España
        self.geodata.datos_espana.boundary.plot(color='black', ax=ax)
        if municipios:
            for municipio in municipios:
                datos_municipio = self.geodata.filtrar_datos('NAME_4', [municipio])
                if not datos_municipio.empty:
                    datos_municipio.plot(color='red', ax=ax)

        if provincias:
            for provincia in provincias:
                datos_provincia = self.geodata.filtrar_datos('NAME_2', [provincia])
                if not datos_provincia.empty:
                    datos_provincia.plot(color='green', ax=ax)

        if comunidades_autonomas:
            for ca in comunidades_autonomas:
                datos_ca = self.geodata.filtrar_datos('NAME_1', [ca])
                if not datos_ca.empty:
                    datos_ca.plot(color='blue', ax=ax)

        plt.show()