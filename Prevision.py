import numpy as np #Libreria que usé para crear los arreglos de los números
from numpy.core.numeric import array_equal, indices
from numpy.lib.function_base import append

#Leer archivo
direccion = 'archivo/Pruebas.in' #se agrega una variable para asignar la direccion donde está el archivo a revisar
with open(direccion) as file_obj:
    lineas = file_obj.readlines() #Con este comando nos es posible asignar dentro de una variale cada linea del documento
arreglo_cantidad = int(lineas[0]) #Esta variable es para saber cuantos números son los que contiene el archivo
arreglo = np.array(lineas) #Aqui se crea un arreglo con cada valor dentro de las lineas
arreglo_pro = [] #Se crea un arreglo vacio
for i in range(1, arreglo_cantidad+1):
    arreglo_pro.append(int(arreglo[i])) #Rellenamos el arreglo con puros enteros
arreglo_pro.sort() #Ordenamos el arreglo de menor a mayor
arreglo_ordenad = arreglo_pro #Lo ponemos en otra variable para mejor entendimiento
arreglo_indices=[]
for i in range(1,arreglo_cantidad+1):
    valor = int(arreglo_ordenad[i-1]) # se considera en el valor que esta como el valor a comparar
    for j in range(1,arreglo_cantidad+1):
        if(valor==int(arreglo[j])):
            arreglo_indices.append(j) #aqui es donde se recupera el indice en el que esta cada valor 
arr_final=[] #Este arreglo contendrá el resultado final, es decir, el arreglo con mas valores
maximo=0 #Esta variable es para asignar cuantos valores tiene el mejor arreglo, se inicializa en 0 
for i in range(0,arreglo_cantidad):
    valor= int(arreglo_indices[i])
    arr_prueba=[]#Este arreglo contendrá el arreglo a comprara con el mejor
    for j in range(i,arreglo_cantidad):
        if(int(arreglo_indices[j])>=valor):
            arr_prueba.append(arreglo_indices[j])#aqui se rellena el arreglo por ese ciclo
            valor=int(arreglo_indices[j]) #Se considera un nuevo valor para cada nuevo indice
    if(len(arr_prueba)>=maximo):
        arr_final=arr_prueba #Se actualiza el mejor arreglo dependiendo de la ultima cantidad de valores del mejor arreglo.
        maximo=len(arr_prueba) #Se actualiza la cantidad de numeros que tiene el mejor arreglo
print("Arreglo final = ",arr_final) #Esta linea es para comprobar el resultado, desarrollado antes de enviarlo al archivo
Archivo_salida = open("archivo/Prueba.out","w") #Esta srrá la variable donde contenga la direccion y el modo de apertura
Archivo_salida.write(str(len(arr_final))) #Aqui se escribe en el archivo la cantidad de numeros que tiene el mejor arreglo 
for i in range(0,len(arr_final)):
    Archivo_salida.write('\n'+ str(arr_final[i])) #Se escribe uno a uno el mejor arreglo, respetando su salto de linea
Archivo_salida.close() #Se cierra el archivo para que el programa no espera mas escritura.
