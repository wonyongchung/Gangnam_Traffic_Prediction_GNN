import encodings
from os import link
import geopandas as gpd
import pandas as pd

# link_df = gpd.read_file('data\[2022-09-05]NODELINKDATA\MOCT_LINK.shp')
# node_df = gpd.read_file('data\[2022-09-05]NODELINKDATA\MOCT_NODE.shp')

realspeeddata = pd.read_csv("data/202207speed.csv")
linkIDlist = realspeeddata["링크아이디"]
startlist = realspeeddata["시점명"]
endlist = realspeeddata["종점명"]
print(realspeeddata.head())
print(len(linkIDlist))
linkIDlist = list(set(linkIDlist.to_list()))
startlist = list(set(startlist.to_list()))
endlist = list(set(endlist.to_list()))
print("link : ",len(linkIDlist))
print("start : ",len(startlist))
print("end : ",len(endlist))


# linkIDlist = list(map(str, linkIDlist))




# small_link_df = link_df.loc[:,["LINK_ID", "F_NODE", "T_NODE"]]
# print(len(small_link_df))
# print("============")
# # print(small_link_df.head())
# link_df = link_df.loc[link_df.LINK_ID.isin(linkIDlist), :]
# print(len(link_df)) #링크수
# print(link_df.head())


# node_f = link_df["F_NODE"].to_list()
# node_t = link_df["T_NODE"].to_list()
# nodelist = list(set(node_f) | set(node_t))
# print(len(nodelist))
# # print(link_df.head())
# # print("------------------")
# # print(node_df.head())

# # gdf.crs= "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"
# # gdf.to_file('D:/GEODATA/df_sp.shp', driver='ESRI Shapefile')


# #linkIDlist에 있는 link가 진짜 계산되야하는애들
# link_df.to_file("data/needdata/linkdata.shp")

