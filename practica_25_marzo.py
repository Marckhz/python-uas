import pandas as pd
'''
dic_alumnos = {"Nombre":["Marco", "Luis", "hugo"], "Edad":["21", "24", "25"]}
df = pd.DataFrame(dic_alumnos)
print(df)

df = pd.DataFrame(dic_alumnos, columns = ['Nombre', 'Edad'])
print(df)

df = pd.read_csv("municipios.csv")

print(df[['nombre','superficie']])

serie = pd.Series(df['nombre'])
print(serie)
print(type(serie))


df = df[df['poblacion']<500000]
print(df)

df = df[(df['poblacion']< 500000) &  (df['poblacion']>200000)]


df = df.loc[(df['poblacion']<500000) & (df['poblacion']>200000),['nombre']]

print(df)

peso = [30,20,15]
df = pd.DataFrame(dic_alumnos)
df['peso'] = peso
print(df)

df1 = df.drop(labels='peso', axis=1)
print(df1)


df1 = df.drop(labels=[1], axis = 0)
df1.reset_index()
print(df1)
'''

df = pd.read_csv('municipios.csv')
#muestra los primeros 3 elementos
print(df.head(3))
#muestra los ultimos dos
print(df.tail(2))