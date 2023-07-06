import folium
import pandas

data = pandas.read_excel("iit_data.xlsx",sheet_name=0)

iit_ranking = list(data["IIT Ranking"])
college_name = list(data["IIT College"])
Nirf_score = list(data["NIRF Score"])
lat = list(data["Latitude"])
lon = list(data["Longitude"])
pic = list(data["Image"])

# parent map
fg = folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(data=(open("india_states.json","r",encoding="utf-8-sig").read())))
# utf means Unicode Transformation format
# 8 is for 8-bit 
# sig means signature
# we use this because it treats file as BOM information of string

# htmlcode to use our dataset

for rank, name, score, lati, longi, im in zip(iit_ranking, college_name, Nirf_score, lat, lon, pic):
    fg.add_child(folium.Marker(location=[lati, longi], popup="<b>College Name: </b>"+str(name)+
                               "<br> <b>Rank among IIT in India: </b>"+ str(rank)+
                               "<br> <b>NIRF Score: </b>"+ str(score)+
                               "<br> <b>img src"+im+
                               "height = 145, width = 300>",icon= folium.Icon(color="red")))
map = folium.Map(location=[20.0000, 75.0000],zoom_start=4) 
# latitude and longitude when you open your file from which location it will be visible
map.add_child(fg)
map.save("final.html")
