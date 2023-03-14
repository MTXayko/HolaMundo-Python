# 1. TAREA: imprime "Hola, mundo"

print("Hola, mundo")
"""Se imprime: Hola, mundo"""

# 2. imprime "Hola, Noelle" con el nombre en una variable#
name = "Noelle"
print("Hola, Noelle")	# con una coma#
print( "hola, " + name)	# con un +#

"""Se imprime: Hola, Noelle"""

# 3. imprimir "Hola 42!" con el número en una variable#
name = 42
print("Hola,",str(name),"!")	# con una coma#
print("Hola, " + str (name) + "!" )	# con una +	-- este debería arrojar un error! #
"""Se imprime: Hola, 42!"""



# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables#
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}" .format (fave_food1, fave_food2)) # con .format()#
print(f"Amo comer {fave_food1} y {fave_food2}" ) # con una cadena f#

"""Se imprime: amo comer sushi y pizza"""


"""Extra tarea"""

print("Hola, Matias")
"""Se imprime: Hola, Matias"""

name = "Matias"
print("¡hola, ",str(name), "!")
"""Se imprime: ¡Hola, Matias!"""

name = "Matias"
print("¡hola, "+str(name), "!")
"""Se imprime: ¡Hola, Matias!"""

name = 87
print("¡Hola,",(name), "!")
"""Se imprime: ¡Hola, 87!"""

"""Bonus Ninja"""

eat_1 = "lasaña"
eat_2 = "empanadas"
print("Amo comer {} y {}" .format(eat_1 , eat_2))
print(f"Amo comer {eat_1} y {eat_2}")
"""Se imprime: Amo comer lasaña y empanadas"""