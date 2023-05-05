#Pedirle al usuario que diga cualquier texto real y: 
#-calcular cuanto tardaria en decir esa frase 
#-cuantas palabras dijo ? 

frase_corta = "Lorem ipsum dolor"
frase = "Cualquier frase real que se te ocurra"   


long_frase = len(frase)
print(long_frase)

cant_espacios = frase.count(" ")
print(cant_espacios)

palabras = cant_espacios + 1
print(palabras)

tiempo_frase = palabras * 0.5
print(tiempo_frase)


#si se tarda mas de 1 min, emitir una alerta 

if(tiempo_frase > 60): print("Excediste el limite")

# X habla un 30% más rapido, ¿cuanto tardaria en decirlo?

x = 0.7

tiempo_frase_X = tiempo_frase * x 
print(tiempo_frase_X)


