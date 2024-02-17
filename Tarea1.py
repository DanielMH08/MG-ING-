import numpy as np
import pandas
import math

Den_L2 = 0

def ValorCorrecto():
    while optimizado not in ['1','2']:
          optimizado = input("Ingrese solo 1 o 2: ")
    return optimizado
 
basedatos = pandas.read_csv(r'c:\Users\DANIEL MURCIA\Desktop\UAM\Magister\Primer Semestre\Programación para ingeniería\Actividad 1\base.csv', delimiter=';', index_col="Col1") 

print("Ingrese el desplazamiento del mecanismo...")
desplazamiento = int(input())

print("Ingrese el porcentaje de ciclo del mecanismo...")
porcentaje = int(input())

print("Escriba 1 si el mecanismo es optimizado por rectitud, o escriba 2 si es optimizado por velocidad...")
optimizado = int(input())

while optimizado not in [1, 2]:
      optimizado = int(input("Valor inválido, ingrese solo 1 o 2: "))

print()
print(f"El valor del desplazamiento ingresado es {desplazamiento}")
print(f"El valor del porcentaje ingresado es {porcentaje}")
print(f"El método de optimización ingresado es {optimizado}")
print()


if porcentaje in basedatos.index:
       if optimizado == 2:
        Den_L2 = (basedatos.loc[porcentaje]["Col15"])
        Den_L1 = (basedatos.loc[porcentaje]["Col13"])
        Den_L3 = (basedatos.loc[porcentaje]["Col14"])

       if optimizado == 1:
         Den_L2 = (basedatos.loc[porcentaje]["Col9"])
         Den_L1 = (basedatos.loc[porcentaje]["Col7"])
         Den_L3 = (basedatos.loc[porcentaje]["Col8"])
else:
    basedatos.loc[porcentaje] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    baseimpar = (basedatos.sort_index().interpolate())
    
    if optimizado == 1:
       Den_L2 = (baseimpar.loc[porcentaje]["Col9"])
       Den_L1 = (baseimpar.loc[porcentaje]["Col7"])
       Den_L3 = (baseimpar.loc[porcentaje]["Col8"])

    if optimizado == 2:
       Den_L2 = (baseimpar.loc[porcentaje]["Col15"])
       Den_L1 = (baseimpar.loc[porcentaje]["Col13"])
       Den_L3 = (baseimpar.loc[porcentaje]["Col14"])
       

L2 = desplazamiento / Den_L2
str_L2 = str(L2)

L1 = Den_L1*L2
str_L1 = str(L1)

L3 = Den_L3*L2 
str_L3 = str(L3)

L4 = L3
str_L4 = str(L4)

print()
print("El valor de L1 es " + str_L1)
print("El valor de L2 es " + str_L2)
print("El valor de L3 es " + str_L3)
print("El valor de L4 es " + str_L4)
print()



