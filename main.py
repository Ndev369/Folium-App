import pandas as pd
import folium

data=pd.read_excel('prueba.xlsx')
data.isnull()
data.dropna()


def color_producer(actividad):
    if actividad == 'VIVIENDA':
        return 'red'
    elif actividad == 'COLMADO':
        return 'blue'
    elif actividad == 'APARTAMENTO':
        return 'green'
    elif actividad == 'ENVASADORA DE AGUA':
            return 'cyan'

 

map = folium.Map(location=[18.483376, -69.893507], zoom_start=10, tiles="openstreetmap")


fgt = folium.FeatureGroup(name= "Colmado")

data = data.fillna('')
act = data[data['actividades_tipo'].str.contains('COLMADO')]

lat = list(act["y"])
lon = list(act["x"])
tip = list(act["tipo"])
acti = list(act["actividades_tipo"])


for lt, ln,tp, at in zip(lat,lon, tip, acti):
        
        fgt.add_child(folium.CircleMarker(location=[lt,ln], radius=4, popup=str(tp+"\n"+at),fill_color = color_producer(at), color = color_producer(at), fill_opacity=0.7))


fg = folium.FeatureGroup(name= "Vivienda")

data = data.fillna('')
tipo = data[data['tipo'].str.contains('VIVIENDA')]

lat = list(tipo["y"])
lon = list(tipo["x"])
tip = list(tipo["tipo"])
acti = list(tipo["actividades_tipo"])

for lt, ln,tp, at in zip(lat,lon, tip, acti):
        
        fg.add_child(folium.CircleMarker(location=[lt,ln], radius=4, popup=str(tp+"\n"+at),fill_color = color_producer(at), color = color_producer(at), fill_opacity=0.7))

        
fga = folium.FeatureGroup(name= "Apartamento")

data = data.fillna('')
tipo = data[data['tipo'].str.contains('APARTAMENTO')]

lat = list(tipo["y"])
lon = list(tipo["x"])
tip = list(tipo["tipo"])
acti = list(tipo["actividades_tipo"])

for lt, ln,tp, at in zip(lat,lon, tip, acti):
        
        fga.add_child(folium.CircleMarker(location=[lt,ln], radius=4, popup=str(tp+"\n"+at),fill_color = color_producer(at), color = color_producer(at), fill_opacity=0.7))


fgv = folium.FeatureGroup(name= "Envasadora de Agua")

data = data.fillna('')
act = data[data['actividades_tipo'].str.contains('ENVASADORA DE AGUA')]

lat = list(act["y"])
lon = list(act["x"])
tip = list(act["tipo"])
acti = list(act["actividades_tipo"])


for lt, ln,tp, at in zip(lat,lon, tip, acti):
        
        fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=4, popup=str(tp+"\n"+at),fill_color = color_producer(at), color = color_producer(at), fill_opacity=0.7))



map.add_child(fgt)
map.add_child(fga)
map.add_child(fg)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Max.html")
 