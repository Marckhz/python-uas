import pandas as pd
import numpy as np

df  = pd.read_csv("paises.csv")

#print(df.head())

df_1 = pd.read_csv("ciudades.csv")



#population_country = df['Population'].mean()
#life_span = df['LifeExpectancy'].mean()
surface_are = df['SurfaceArea'].var()
print(surface_are)

#print(population_country)
#print(life_span)
#print(surface_are)

def filter_city(code):

	this_df = [df_1['Population']
	
filter_city("AFG")

df= pd.read_csv("municipios.csv")
df= df.loc[(df['poblacion']<500000) & (df['poblacion']>200000),["nombre"]]
#print(df)