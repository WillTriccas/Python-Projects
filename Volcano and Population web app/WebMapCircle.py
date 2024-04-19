# this is the same as Webmapimport HOWEVER, the markers are circles and code differs slightly for colouring the markers for example

import folium
import pandas

themap = folium.Map(location=[36.20,-112.16], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "First Layer")

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

# check out dir(folium) for CircleMarker and help(folium.CircleMarker) for the parameters. (it doesnt actually say in python help about fill color and color and opacity
# but instead says 'kwargs' because of this, you have to look in online documentation for full list of arguments that you can pass for this function CircleMarker)

#CircleMarker inherits attributes from a class 'Path' so every attribute 'Path' defines, is also defined by CircleMarker

for lt,lg,el in zip(Lat,Long,elev):
    fg.add_child(folium.CircleMarker(location = [lt,lg], radius = 8 ,popup = str(el) + "m", fill_color = Elevation_colour(el),
    color = 'grey', fill = True))
    
    

themap.add_child(fg)


themap.save("webmap.html")
