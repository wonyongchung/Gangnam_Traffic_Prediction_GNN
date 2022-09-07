import geopandas as gpd
import pandas as pd
import numpy as np
node_data = gpd.read_file('./data/[2022-09-05]NODELINKDATA/MOCT_NODE.shp')
link_data = gpd.read_file('./data/[2022-09-05]NODELINKDATA/MOCT_LINK.shp')
 
print(node_data.head())
print(link_data.head())