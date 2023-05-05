# if-else
contraseña_almacenada = "Ejemplo"
contraseña_escrita = '''Ejemplo1'''

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESIÒN...")
else: 
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")    

#elif

ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("Tenes deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Normal")
    else:
        print("Limite")
    
elif ingreso_mensual > 1000:
    print("Ok latinoamèrica")
    
elif ingreso_mensual > 500:
    print("Ok en argentina")
       
else: 
    print("No cubris gastos")