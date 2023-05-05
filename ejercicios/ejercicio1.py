# Diferencia en porcentaje entre el curso actual y : 
#1-el mas rapido de otros cursos 
#2-el mas lento de otros cursos
#3-el promedio de los cursos 

curso_actual= 1.5 
curso_mas_rapido= 2.5
curso_mas_lento= 7
curso_promedio = 4

difMax = 100 - (curso_actual/curso_mas_rapido*100)
print(difMax)

difMin = 100 - (curso_actual/curso_mas_lento*100)
print(difMin)

promedio = 100 - (curso_actual/curso_promedio*100)
print(promedio)

#Porcentaje de material inservible que se reduce en: 
# el promedio de los cursos 
# el curso actual (este curso

crudo_actual = 3.5
crudo_prom = 5 

mat_inservible = (crudo_prom - curso_promedio)/crudo_prom
print(mat_inservible)

mat_inservible_actual = (crudo_actual-curso_actual)/crudo_actual
print(mat_inservible_actual)

#Ver 10hs de este curso a cuantas de otros cursos equivale 

equivalencia = (10*curso_promedio)/curso_actual
print(equivalencia)

equivalencia_otros = (10*curso_actual)/curso_promedio
print(equivalencia_otros)