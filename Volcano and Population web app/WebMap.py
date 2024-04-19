import folium

themap = folium.Map(location=[51.55,-0.091], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "First Layer")

for coordinates in [[51.55,-0.091],[52.55,-0.091]]:
    fg.add_child(folium.Marker(location = coordinates, popup = "Will's London flat", icon = folium.Icon(color = 'orange')))

themap.add_child(fg)


themap.save("webmap.html")

# run this and you will get the map in css, java and html format which can be viewed in a browser
# everytime you run the above, it will override the current map that you have 