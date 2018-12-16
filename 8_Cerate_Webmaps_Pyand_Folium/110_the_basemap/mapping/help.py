# pip install folium

# pip install jinja2

import folium
dir(folium)
help(folium.Map)

map =  folium.Map(location=[80,-100])
map.save("Map1.html")

map = folium.Map(location=[37.05681,28.3248053], zoom_start=6)
map.save("Map1.html")
