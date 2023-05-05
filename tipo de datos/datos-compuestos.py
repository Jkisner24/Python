#Tupla: No modificable los valores#
tupla = ("texto", "texto2", True, 45)
print(tupla[1])

#Lista modificable#
lista = ["texto", "texto2", True, 45]
print(lista)

print(lista[1])

#Set: Modificable, no se puede acceder por indice, se accede por bucles#
conjunto = {"texto", "texto2", True, 45}

#igual a json en javascript
diccionario = {
    "nombre": "Julian",
    "edad": 28,
    "direccion": "Av. Alem 534"
}

print(diccionario["nombre"])
