#creando diccionarios con dict()
diccionario = dict(nombre="Julian",apellido="Kisner")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario2 = {frozenset(["Julian","key"]):"valor1"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario3 = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "nuevo valor"
diccionario4 = dict.fromkeys(["nombre","apellido"],"Nuevo valor")

print(diccionario4)