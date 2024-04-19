# this script will overwrite the webmap made in 'WebMap.py' but have made this separate as it shows you how you can import data from a text file
# and use it on your map where as 'WebMap.py' just uses stuff within python and teaches you the bare bones

import folium
import pandas

themap = folium.Map(location=[36.20,-112.16], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "Marker Layer")
fg1 = folium.FeatureGroup(name = "Polygon Layer")

df1 = pandas.read_csv("Volcanoes.txt")

# df1(volcanoes file) has two columns called lat and lon which have latitude and longitude in them respectively, we want them as lists individually

Lat = list(df1["LAT"])
Long = list(df1["LON"])
elev = list(df1["ELEV"])


def Elevation_colour(elv):
    if elv < 2000:
        return 'green'
    elif 2000 <= elv < 3000:
        return 'orange'
    else:
        return 'red'

# above function determines colour of the marker of the volcano based off its elevation

for lt,lg,el in zip(Lat,Long,elev):
    fg.add_child(folium.Marker(location = [lt,lg], popup = str(el) + "m", icon = folium.Icon(color = Elevation_colour(el))))
    
fg1.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) 


themap.add_child(fg)
themap.add_child(fg1)

themap.add_child(folium.LayerControl())

themap.save("webmap.html")
