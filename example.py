print("Datos del producto")
# Para obtener una cadena de caracteres se utiliza la función input junto con variables
# diferentes por lo tanto, se le permite al usuario que ingrese los datos por teclado.
nombre1 = input("Ingrese nombre del producto:")
# En la siguiente línea se ingresa un valor y se transforma en entero y se acumula ese
# valor en la variable precio1
precio1 = int(input("Ingrese un precio:"))
# En la siguiente línea se ingresa un valor y se acumula en la variable nombre2
nombre2 = input("Ingrese nombre del producto:")
# En la siguiente línea se ingresa un valor y se transforma en entero y se acumula ese
# valor en la variable precio2
precio2 = int(input("Ingrese un precio:"))
# en la siguiente línea se nombra una constante (En letras mayúsculas)
BONIFICACION = 20
# Se suman dos precios y su resultado se guarda en la variable precio_compra_total
precio_compra_total = precio1 + precio2
# En la siguiente línea se comprueba sí el precio1 es mayor o igual que el precio2 y se
# guarda en la variable comparar. Por lo tanto, el resultado es un valor booleano (true or false)
comparar = precio1 >= precio2
# ahora se utiliza un operador lógico (and) para evaluar los precios y se guardan en la
# variable logico; por lo tanto, el resultado es un valor booleano (true or false) pero tiene que
# cumplirse las dos condiciones para que el resultado sea true
logico = (precio1 < precio2 and precio1 == precio2)
# en el siguiente bloque se va a concatenar texto y se procede de la siguiente manera:
cabecera = "resultados del producto {0} y del producto {1} es: "
# en la siguiente línea se concatena el texto con la función format
print(cabecera.format(nombre1, nombre2))
print("El precio del primer valor es mayor o igual a el precio del segundo valor")
# Otra forma de concatenar es con el signo más (+) y en la variable la propiedad str
print("La suma de los productos es: $ " + str(precio_compra_total))
print("El precio1 < precio2 and precio1 == precio2")
print(logico)
# En la siguiente línea se tiene un operador de asignación
precio_compra_total += BONIFICACION
print("al precio total se le incrementa su valor que tiene la constante: " +
      str(precio_compra_total))
# Como nota se puede ejecutar directamente en una terminal de este archivo directamente.
