## Se incluten las liberías necesarias para hacer el manejo de matrices y operaciones matemáticas 
import numpy as np
import pandas
import math

Den_L2 = 0

# Por facilidad en manejo de la información, se importa tabla de datos desde un archivo CSV. LA ruta debe cambiarse para ejecutar el programa, se adjunta el archivo.
# Se indica que el separador es ";" y que la primera columna recibe el valor o ubicación 1

basedatos = pandas.read_csv(r'c:\Users\DANIEL MURCIA\Desktop\UAM\Magister\Primer Semestre\Programación para ingeniería\Actividad 1\base.csv', delimiter=';', index_col="Col1") 

# Interfaz con el usuario para solicitar los datos que determina el problema
print("Ingrese el desplazamiento del mecanismo...")
desplazamiento = int(input())

print("Ingrese el porcentaje de ciclo del mecanismo...")
porcentaje = int(input())

print("Escriba 1 si el mecanismo es optimizado por rectitud, o escriba 2 si es optimizado por velocidad...")
optimizado = int(input())

# Función que verifica ingreso adecuado de datos
while optimizado not in [1, 2]:
      optimizado = int(input("Valor inválido, ingrese solo 1 o 2: "))

# Confirmación al usuario de los datos que ingresó en el paso anterior 
print()
print(f"El valor del desplazamiento ingresado es {desplazamiento}")
print(f"El valor del porcentaje ingresado es {porcentaje}")
print(f"El método de optimización ingresado es {optimizado}")
print()

# Condicionales para la ubicarse en la tabla de datos y extraer los números 
# Primer IF (Ln 35 - 45) Si el porcentaje ingresado se encuentra en la tabla, y dependiendo de cuál haya sido el método seleccionado (1 o 2) se ubica en determinadas columnas para obtener los datos

if porcentaje in basedatos.index:
       if optimizado == 2:
        Den_L2 = (basedatos.loc[porcentaje]["Col15"])
        Den_L1 = (basedatos.loc[porcentaje]["Col13"])
        Den_L3 = (basedatos.loc[porcentaje]["Col14"])

       if optimizado == 1:
         Den_L2 = (basedatos.loc[porcentaje]["Col9"])
         Den_L1 = (basedatos.loc[porcentaje]["Col7"])
         Den_L3 = (basedatos.loc[porcentaje]["Col8"])

# Si el valor ingresado no se encuentra en la tabla, procede lo siguiente         
else:
    # Primer punto, crear una fila para albergar los nuevos valores que resultan de la interpolación, se crean espacios Not A Number
    basedatos.loc[porcentaje] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

    # Se crea una variable con una nueva tabla de datos, donde ya se ha ubicado el nuevo valor con las respectivas interpolaciones en su fila 
    baseimpar = (basedatos.sort_index().interpolate())
    
    # Se evalúa el método seleccionado (1 o 2) y se ubica la columna para tomar los datos necesarios para realizar los cálculos 
    if optimizado == 1:
       Den_L2 = (baseimpar.loc[porcentaje]["Col9"])
       Den_L1 = (baseimpar.loc[porcentaje]["Col7"])
       Den_L3 = (baseimpar.loc[porcentaje]["Col8"])

    if optimizado == 2:
       Den_L2 = (baseimpar.loc[porcentaje]["Col15"])
       Den_L1 = (baseimpar.loc[porcentaje]["Col13"])
       Den_L3 = (baseimpar.loc[porcentaje]["Col14"])
       

# Se realizan las operaciones para conocer los datos de los eslabones, las variables se extraen del paso anterior
L2 = desplazamiento / Den_L2
str_L2 = str(L2)

L1 = Den_L1*L2
str_L1 = str(L1)

L3 = Den_L3*L2 
str_L3 = str(L3)

L4 = L3
str_L4 = str(L4)

# Se le entrega al usuario los valores esperados de los eslabones para su mecanismo de Hoeken 
print()
print("El valor de L1 es " + str_L1)
print("El valor de L2 es " + str_L2)
print("El valor de L3 es " + str_L3)
print("El valor de L4 es " + str_L4)
print()



