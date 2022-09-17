import pandas
from geopy.geocoders import ArcGIS
nom = ArcGIS()
#
#
# df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"])
# print(df1)
# df2 = pandas.DataFrame([{"Name":"John","Surname":"Preach"}, {"Name":"Jack"}])
# print(df2)
#
# print(type(df1))
# print(df1.mean())
# print(df1.mean().mean())
# print(df1.Price.mean())
#
#
df_csv = pandas.read_csv("supermarkets.csv")
print(df_csv)
# df_json = pandas.read_json("supermarkets.json")
# df_json.set_index("ID")
# print(df_json)
# df_excel = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
# print(df_excel)
# df_csv_comm = pandas.read_csv("supermarkets-commas.txt")
# print(df_csv_comm)
# df_csv_semi = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
# print(df_csv_semi)
#
# print(list(df_csv_semi.loc["1":"3","City":"Name"]))
# print(df_csv_semi.iloc[1:4,1:4])
#
# df_csv_semi["Continent"] = df_csv_comm.shape[0]*["North America"]
# print(df_csv_semi)
# df_csv_semi_1 = df_csv_semi.T
# print(df_csv_semi_1)
# df_csv_semi_1["My Address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
# print(df_csv_semi_1)

df_csv["Address"] = df_csv["Address"] + ", " + df_csv["City"] + ", " + df_csv["State"] + ", " + df_csv["Country"]

print(df_csv["Address"] )
df_csv["Coordinates"] = df_csv["Address"].apply(nom.geocode)
print(df_csv.Coordinates[0].latitude)

df_csv["Latitude"] = df_csv["Coordinates"].apply(lambda x: x.latitude)
df_csv["Longitude"] = df_csv["Coordinates"].apply(lambda x: x.longitude)
print(df_csv)