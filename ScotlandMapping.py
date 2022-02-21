# Piece of code that is used to extract information from the shapefile
# and manipulate it for showing us only the required information going forward
import geopandas as gpd
import pandas as pd

shp = gpd.read_file(r"D:\Year 2 UOL\Software Engineering Project Mapping Cities in Python\Code\roads.shp")
print (shp.columns)
#To check the road network map created by obtained shapefile
shp.plot()
#To obtain the types of unique defined roads in file
print (shp['type'].unique())

#To extract the only required road networks to display
test = shp.get(shp['type']=='primary')
test2 = shp.get(shp['type']=='motorway')
test3 = shp.get(shp['type']=='minor')

# Used to test to see if we are able to extract more detailed Roads
# print (shp['maxspeed'].unique())
# test4 = shp.get(shp['maxspeed']>=8)

#Merging extracted types of roads needed and plotting them
merged = gpd.GeoDataFrame(pd.concat([test,test2,test3]))
merged.plot()

