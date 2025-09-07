import requests as re
import pandas as pd
import json


request = re.get("https://nrfaapps.ceh.ac.uk/nrfa/ws/station-info?station=*&format=json-object&fields=all")
# print(request)

j = json.loads(request.text)

df = pd.DataFrame(j["data"])

print("River Flow Data:")
print("###############################################################")
print(df.head())
print(df.columns)
print(df.describe())
print("###############################################################")

rainfallRequest = re.get("https://services.arcgis.com/Lq3V5RFuTBC9I7kv/arcgis/rest/services/Monthly_Precipitation_Observations_1991_2020_12km/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson")

geoJson = json.loads(rainfallRequest.text)

rainfallDf = pd.DataFrame(geoJson["features"])

print("Uk Monthly Rainfall Data:")
print("###############################################################")
print(rainfallDf.head())
print(rainfallDf.columns)
print(rainfallDf.describe())
firstRowGeometry = pd.DataFrame(rainfallDf.iloc[0]["geometry"])
print(firstRowGeometry.head())
print(firstRowGeometry.columns)
print(rainfallDf.iloc[0]["properties"])
# firstRowProperties = pd.DataFrame(rainfallDf.iloc[0]["properties"])
# print(firstRowProperties.head())
# print(firstRowProperties.columns)
print("###############################################################")