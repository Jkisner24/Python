diccionario = {
    "nombre" : 'Julian',
    "apellido" : 'Kisner',
    "subs" : 545455
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

print(claves)

#obteniendo un elemento con get() (si no encuentra nada el programa continùa)
valor_de_nombre= diccionario.get("nombre")

print("hola, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
