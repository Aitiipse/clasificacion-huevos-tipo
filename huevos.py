#Autor: Duvan Espitia

#Categorias     peso        ud      bandejas
#   A           53 <60      gr      30
#   AA          60 <67      gr      24
#   AAA         =>67         gr     12
#   BC           46 <53      gr      30

import math
import random
lista_huevos =[]
for i in range(200):
    numero = random.randint(20, 68)
    lista_huevos.append(numero)
  
# lista_huevos = [46.5, 60.8, 58.7, 49.8, 62, 12, 52, 53, 65]
    

def clasificacion_huevos(lista_huevos):
    
    tipos = {'A':[],'AA':[],'AAA':[],'BC':[]}
    
    for huevo in lista_huevos:
        if huevo >= 53 and huevo < 60 :
            tipo = 'A'
        elif huevo >= 60 and huevo < 67:
            tipo = 'AA'
        elif huevo >= 67 :
            tipo = 'AAA'
        else:
            tipo = 'BC'
            
        if tipo in tipos:
            tipos[tipo].append(huevo)
        else:
            tipos[tipo] = [huevo]
            
    return tipos


def calcular_bandejas(numero, bandejas):
        
    cantidad = numero/bandejas
        
    return cantidad

    
tipos = clasificacion_huevos(lista_huevos)
cantidad_por_bandeja= [30, 24, 12, 30]


for i, (clave, valor) in enumerate(sorted(tipos.items())):
  
   clase= str(clave)
   numero_huevos = str((len(tipos.get(clave, []))))
   numero_bandejas = str(math.ceil(calcular_bandejas((len(tipos.get(clave, []))),cantidad_por_bandeja[i])))    
    
   print("Tipo_huevos: "+ clase +", numero_huevos: "+ numero_huevos +", numero_bandejas: " +numero_bandejas)
print(sorted(tipos))
    
     