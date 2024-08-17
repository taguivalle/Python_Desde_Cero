# **_Python DESDE CERO_**

![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=taguivalle&show_icons=true)

![Your Repository's Stats](https://github-readme-stats.vercel.app/api/top-langs/?username=taguivalle&theme=blue-green)
![GitHub Contributors Image](https://contrib.rocks/image?repo=taguivalle/Python_Desde_Cero)

## 1. Random Joke Generator

![Jokes Card](https://readme-jokes.vercel.app/api)

## 2. Profile View Counter

![Profile View Counter](https://komarev.com/ghpvc/?username=Tanu-N-Prabhu)

## 3. Repository View Counter - HITS

[![Hits](https://hits.sh/github.com/silentsoft/hits.svg)](https://hits.sh/github.com/silentsoft/hits/)

## Agradecimientos Sinceros

Es muy importante aclarar que, lo expuesto en este pequeño pero gran tutorial la mayoría de los conceptos los adquirí de la plataforma educativa [Udemy](https://www.udemy.com/mobile/ipad/) que a lo largo de los años he utilizado mucho por su variedad de información con respecto de los cursos como de sus magistrales educadores; la verdad me siento muy agredecido con esta plataforma educativa; para lo que les deseo muchos éxitos y prosperidad.

No obstante, también un agradecimiento muy especial a las diferentes páginas web que he consultado y que se referencián en este tutorial y muy especialmente a [GitHub](https://github.com/) por sus valiosos aportes en la documentación como de la orientación de diferentes usuarios de la misma.

De otra parte agradecer personalmente al Profe "**Gildardo Patiño Trillos**" quién ha sido mi mentor desde los inicios en mi Carrera como estudiante de Ingeniería de Sistemas realizado en la sagrada Universidad Cooperativa de Colombia [UCC](https://ucc.edu.co/).

## **Introducción**

inicialmente, dar un gran ¡Hola y bienvenidos al tutorial "Python desde cero"! Si alguna vez ha querido aprender a programar pero no sabía por dónde empezar, se encuentra en el lugar adecuado. Para muchos es de pleno conocimiento que, Python es un lenguaje de programación increíblemente versátil y amigable para principiantes, conocido por su sintaxis clara y su amplia aplicabilidad en el desarrollo web, la ciencia de datos, la inteligencia artificial, la automatización y muchos más temas que concierne este lenguaje de programación.

En este tutorial, se tiene un paso a paso desde los conceptos básicos hasta algunas técnicas más avanzadas. No se necesita tener ninguna experiencia previa en programación; aquí se cubre lo necesario para poder empezar a programar en Python con confianza.

## ¿Qué se puede aprender en este tutorial?

1. **_¿Qué es Python?_**, por qué es popular y cómo configurarlo en la computadora.
2. **_Sintaxis Básica_**: Cómo escribir y ejecutar tu primer programa en Python, entender variables, tipos de datos y operaciones básicas.
3. **_Control de Flujo_**: Estructuras de control como condicionales y bucles para crear programas más dinámicos.
4. **_Funciones y Módulos_**: Cómo definir y utilizar funciones, así como organizar tu código en módulos reutilizables.
5. **_Estructuras de Datos_**: Trabajar con listas, diccionarios y otras estructuras de datos para almacenar y manipular información.
6. **_Manejo de Archivos_**: Cómo leer y escribir archivos para interactuar con datos almacenados en tu sistema.
7. **_Proyectos Prácticos_**: Aplicar lo que se ha aprendido en proyectos reales y desafiantes para solidificar tus conocimientos.

A lo largo del tutorial, se encuentran ejemplos prácticos, ejercicios y consejos que pueden ser de gran ayuda a reforzar el aprendizaje de este lenguaje de programación. uno de los objetivos de este tutorial es que no solo se comprenda cómo funciona Python, sino que también sentirse cómodo y motivado para seguir explorando y creando por propia cuenta.

Es de entender que, este tutorial es un abrebocas de lo que puede llegar a ser Python; pero son unos conceptos que se han extraído en su mayor parte de la web como también muy personales; con otra forma de ver este maravilloso mundo del lenguaje de programación como lo es Python.

¡Así que agarra tu computadora, abre tu editor de texto favorito, y prepárate para sumergirte en el emocionante mundo de la programación con Python!

## 1. **¿Qué es Python?**

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general, que soporta múltiples paradigmas de programación, incluyendo programación estructurada, orientada a objetos y funcional. Fue desarrollado por [Guido van Rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum) y lanzado por primera vez en 1991. Python es conocido por su enfoque en la legibilidad del código, lo que permite a los desarrolladores expresar conceptos de manera concisa y clara.

_Ilustración 1_
![Guido Van Rossum](assets/img/Guido_van_Rossum_OSCON_2006.jpg "Guido Van Rossum")
Fuente: [Guido van rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum)

Python cuenta con un sistema de tipado dinámico y una gestión automática de memoria, lo que lo hace flexible y eficiente para una amplia gama de aplicaciones. Además, Python tiene una extensa biblioteca estándar y un ecosistema robusto de paquetes y módulos de terceros que extienden sus capacidades a áreas como desarrollo web (Django, Flask), análisis de datos (Pandas, NumPy), inteligencia artificial (TensorFlow, PyTorch), automatización, scripting y más.

El intérprete de Python puede ser ejecutado en múltiples plataformas (Windows, macOS, Linux), lo que facilita el desarrollo y la implementación de aplicaciones en diferentes entornos. Además, Python es un lenguaje interpretado, lo que significa que el código se ejecuta línea por línea, permitiendo una depuración y pruebas más rápidas, aunque con un rendimiento potencialmente inferior en comparación con los lenguajes compilados. Claro está que, lo dicho aquí no lo es un todo; solamente es un simple resumen muy personal del mundo que es **Python**.

## 2. **Instalación de Python**

Antes de empezar a programar, se necesita instalar Python en el ordenador y/o computadora.

1. **En Windows**:

    * Se visita la página oficial de Python: [Python.org](https://www.Python.org/downloads/). Por favor ver la ilustración 1.

    * Descarga la última versión de Python.

    * Durante la instalación, asegúrate de marcar la casilla **"Add Python to PATH"**. Ver la ilustración 1.

_Ilustración 2_
![Path](assets/img/PythonPath.png "add to path")

Ahora, sí siguen los pasos de instalación intuitivos que brinda el programa se puede llegar a un feliz termino de esta; seguidamente, se puede asegurar  de que todo esté correctamente configurado; escribiendo en una terminal CMD Python3 --version. Realmente los pasos son muy sencillos.

_Ilustración 3_
![Python](assets/img/InstalarPython.png "Descargar Python")
Fuente: [Python](<https://www.Python.org/downloads/>) y Propia.
2. **MacOS/Linux**:

    * Por favor ver la ilustración 3 debido ya que Python suele estar preinstalado en estos sistemas. Para esto se puede verificar abriendo una terminal o ejecutar la tecla Windows + la letra R (al mismo tiempo) dentro de esta terminal se escribe el siguiente comando: ```Python --version```

_Ilustración 4_
![Python](assets/img/PythonLinux.png "Descargar Python otras versiones")
 Fuente: [Python](<https://www.Python.org/downloads/>) y Propia.

    * Si no está instalado, se puede instalar utilizando un gestor de paquetes como brew (en macOS) o apt-get (en Ubuntu).```brew install Python```.

O en su defecto se puede escribir ```sudo apt-get install Python3```

## **3. Configurar un Entorno de Desarrollo**

Inicialmente, para escribir y ejecutar el código en Python, se necesita un entorno de desarrollo. Pare esto se tienen algunas opciones y/o sugerencias:

* [IDLE](https://docs.Python.org/3/library/idle.html) (Python's Integrated Development and Learning Environment): Este, viene con la instalación de Python. Es simple y fácil de usar para empezar.

_Ilustración 5_
![Python IDLE](assets/img/PythonIdle.png "Python Idle")
Fuente: Propia.

* [VS Code](https://code.visualstudio.com/ "VS Code"): Siendo este Un editor de texto poderoso y personalizable con soporte para Python.

_Ilustración 6_
![Vs Code](assets/img/pythonIdle.png)
Fuente: [Vs Code](https://code.visualstudio.com/ "Python IDLE") y propia.

* [PyCharm](https://www.jetbrains.com/es-es/pycharm/): Es un IDE más avanzado, con muchas herramientas para facilitar el desarrollo en Python.

_Ilustración 7_
![PyCharm](assets/img/PyCharmIDE.png "PyCharm")
Fuente: [PyCharm](https://www.jetbrains.com/es-es/pycharm/) y propia.

**NOTA**: Para este tutorial se utilizó el Editor de Texto VS Code. Pero es a discreción del usuario el editor que quiera utilizar. Otro aspecto que se debe de conocer también es ciertos aspectos relevantes para lograr a comprender un poco este tema tan apasionante como lo es Python.

## Sintaxis de Python

A continuación se presenta el tema de la sintaxis de Python; este vendría a ser la forma de empezar a usar el lenguaje Python con el objeto de ir creando y/o analizando sobre ¿Qué son las variables y estructuras de control?.

El termino [sintaxis](https://dle.rae.es/sintaxis?m=form) hace referencia al conjunto de reglas que definen las secuencias correctas de los elementos de un lenguaje de programación; de cómo se debe de escribir el código en un determinado lenguaje de programación. En resumen, hace referencia a la forma en la que se debe escribir las instrucciones para que el ordenador, o más bien el lenguaje de programación entienda lo que se está solicitando.

Como es de común acuerdo, en la mayoría de lenguajes existe una sintaxis propia de cada lenguaje, también existen similitudes como por ejemplo, el uso del término matemático (igual) = para asignar un dato a una variable, o el uso de los famosos corchetes {} para designar bloques de código, pero Python tiene ciertas particularidades.

Por lo tanto, la sintaxis viene siendo tan importante para la programación como lo que es la gramática para los idiomas. Se puede dar un pequeño comentario acerca de la frase “Yo estamos aquí”escribirla así no es correcta y el siguiente código en Python no sería correcto, ya que no respeta las normas del lenguaje.

```Python
if ($variable){
    x=9;
}
```

El anterior código, lo veremos a continuación en detalle; pero, lo importante de Python es que no soporta el uso de lo que se conoce como el signo pesos ``$`` ni hace falta terminar las líneas con el signo de puntuación punto y coma (;) como en otros lenguajes, y tampoco hay que usar {} en estructuras de control como en el if.

De la misma forma que, un idioma no se habla con simplemente saber todas sus palabras, en la programación no basta con saber la sintaxis de un lenguaje para programar correctamente en este. También es cierto, que sabiendo la sintaxis se puede empezar a programar y a hacer muchas cosas con la sintaxis; pero, utilizar un lenguaje de programación va mucho más allá de la sintaxis.

Ahora, con el objeto de empezar a perderle el miedo a la sintaxis de Python, se puede ver un ejemplo donde se observa cadenas, operadores aritméticos y el uso del condicional if; entre otros. Así, el siguiente código simplemente define tres valores a, b y c, realiza unas operaciones con ellos y muestra el resultado por pantalla.

```Python
# Se define una variable x con una cadena
x = "El valor de (a+b)*c es"

# Se pueden realizar múltiples asignaciones
a, b, c = 4, 3, 2

# También se pueden realizar unas operaciones con a,b,c
d = (a + b) * c

# Y se define una variable booleana
imprimir = True

# Y por lo tanto se debe de imprimir, ``print()``
if imprimir:
    print(x, d)

# Por lo que la salida: El valor de (a+b)*c es 14
```

Al observar el anterior código, se tiene que, la sintaxis de Python es muy parecida al lenguaje natural o [pseudocódigo](https://www.youtube.com/watch?v=KcSD3r16Pl0) por [Kiko Palomares](https://github.com/KikoPalomares "Kiko Palomares"). Entonces, El pseudocódigo es una representación textual de un [algoritmo](https://www.epitech-it.es/algoritmo-diferentes-tipos/) o proceso, escrito de manera que imita el lenguaje de programación; pero, no es específico de un lenguaje en particular. Es como una forma de expresar los pasos que va a realizar un programa de manera clara y concisa, utilizando estructuras de control, sentencias de asignación y comentarios para explicar el proceso.

A diferencia de un lenguaje de programación real, el pseudocódigo no es ejecutable directamente por la máquina, sino que se utiliza como intermediario entre la resolución de problemas y la codificación real en un lenguaje de programación. Esto permite a los programadores trabajar de manera independiente del lenguaje, centrándose en el algoritmo y su lógica, lo que facilita la colaboración y la comprensión mutua. Con esto en mente, lo que hace el pseudocódigo es que sea es relativamente fácil de leer. Otra ventaja es que no necesitamos nada más.

Volviendo al código anterior, puede ser ejecutado tal cual está. Ahora al tener conocimientos en otros lenguajes como C o Java, esto resultará de mucha utilidad, ya que no es necesario crear la típica función main(). Pero, obsérvese que se tienen unos comentarios para ir describiendo lo que puede o tiene el código.

## ¿Qué son los Comentarios en los lenguajes de programación?

como su nombre lo índica, los comentarios son bloques de texto usados para comentar el código. Es decir, para ofrecer información relevante tanto al que lo escribe como a otros programadores que brinda información relevante acerca del código que se está escribiendo. Para efectos prácticos, para Python como para algunos lenguajes de programación es como si no existieran, ya que no son código propiamente dicho, solamente son anotaciones.

Los comentarios se inician con # y todo lo que vaya después en la misma línea será considerado un comentario.

```Python
# Esto es un comentario
```

Como se mencionó anteriormente, al igual que en otros lenguajes de programación, podemos también comentar varias líneas de código. Para ello es necesario hacer uso de triples comillas bien sean simples, inclinadas ''' o dobles """. Es necesario usarlas para abrir el bloque del comentario y para cerrarlo.

```Python
Esto es un comentario
de varias líneas
de código
```

## Identación y bloques de código en Python

La identación en Python es la práctica de utilizar espacios o tabuladores para identar los bloques de código. Esta identación es necesaria para indicar la estructura jerárquica de los comandos y controlar la fluidez del programa. En Python, los bloques de código se definen mediante la identación, es decir, al utilizar espacios o tabuladores para identar las líneas dentro de un bloque.

por lo tanto, es importante mantener consistencia en la identación a lo largo del código; debido a que, Python no tiene un límite explícito de identación, sino que se basa en la lógica de que las líneas identadas pertenecen al mismo bloque. Por lo general, se utiliza cuatro espacios para la identación, pero esto puede variar según las preferencias personales del desarrollador.

### Los bloques de código en Python se definen de la siguiente manera

* Un bloque ``if`` se identifica con una identación adicional después de la palabra clave ``if``.
* Un bloque ``elif`` se identifica con una identación adicional después del bloque ``if`` precedente.
* Un bloque ``else`` se identifica con una identación adicional después del bloque ``elif`` o ``if`` precedente.
* La identación se deshace al llegar al final del bloque, lo que indica el regreso a la instrucción principal.

En el siguiente ejemplo, el bloque ``if`` se identifica con cuatro espacios, y los bloques ``elif`` y ``else`` también se identifican con cuatro espacios respectivos. El código dentro de cada bloque está identado también con cuatro espacios para mostrar claramente la estructura del programa.

En resumen, la identación en Python es esencial para definir los bloques de código y controlar la fluidez del programa. Es importante mantener consistencia en la identación a lo largo del código y utilizar una cantidad consistente de espacios o tabuladores para identar las líneas.

#### Código de ejemplo en Python

```Python
if edad <= 2:
    print('Vuelo gratuito')
elif 2 < edad < 13:
    print('Tarifa de niño')
else:
    print('Tarifa para adultos')
```

**Nota**: En este ejemplo, se utiliza cuatro espacios para la identación. Sin embargo, es importante mantener consistencia en esta a lo largo del código y utilizar la cantidad de espacios o tabuladores que se prefiera.

Generalmente, En Python los bloques de código se representan con identación, y aunque hay un poco de debate con respecto a usar tabulador o espacios, la norma general es usar cuatro espacios. Obsérvese otro ejemplo.

En el siguiente código se tiene un condicional ``if``. Justo después aparece un ````print()```` identado con cuatro espacios. Por lo tanto, todo lo que tenga esa identación pertenecerá al bloque del if.

```Python
if True:
    print("True")
```

Esto es muy importante ya que el código anterior y el siguiente no son lo mismo. De hecho el siguiente código daría un error ya que el ``if`` no contiene ningún bloque de código, y eso es algo que no se puede hacer en Python.

```Python
if True:
print("True")
```

Como se manifestara en anteriores líneas a diferencia que en otros lenguajes de programación, no es necesario utilizar el signo de punto y coma (;) para terminar cada línea.

```c
# Otros lenguajes como C requieren del signo de puntuación punto y coma (;) al final de cada línea

x = 10;
```

Sin embargo en Python no es necesario, basta con un salto de línea.

```Python
x = 5
y = 10
```

Pero se puede usar el signo de puntuación punto y coma (;) para tener dos sentencias en la misma línea.

```Python
x = 5; y = 10
```

### Múltiples líneas

En algunas situaciones se puede dar el caso de que se quiera tener una sola instrucción en varias líneas de código. Uno de los motivos principales podría ser que fuera demasiado larga, y de hecho en la especificación [PEP8](https://dev.to/viktorvillalobos/que-es-el-pep-8-y-porque-deberia-implementarlo-54bh) se recomienda que las líneas no excedan los 80 caracteres, usar cuatro espacios en la identación en ves de tabs y otras más.

Haciendo uso de la barra inclinada invertida (\ ) se puede romper el código en varias líneas, lo que en determinados casos hace que el código sea mucho más legible.

```Python
x = 1 + 2 + 3 + 4 +\
    5 + 6 + 7 + 8
```

Si por lo contrario estamos dentro de un bloque rodeado con paréntesis (), bastaría con saltar a la siguiente línea.

```Python
x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)
```

Se puede hacer lo mismo para llamadas a funciones

```Python
def funcion(a, b, c):
    return a+b+c

d = funcion(10,
23,
3)
```

### Creando variables

Anteriormente, se ha visto como crear una variable y asignarle un valor con el uso de =. Existen también otras formas de hacerlo de una manera un poco más sofisticada.

Por ejemplo asignar el mismo valor a diferentes variables con el siguiente código.

```Python
x = y = z = 10
```

O también se puede asignar varios valores separados por coma.

```Python
x, y = 4, 2
x, y, z = 1, 2, 3
```

### Nombrando variables

De igual manera, se pueden nombrar las variables como se quiera nombrar, pero es importante saber que las mayúsculas y minúsculas son importantes. Las variables x (en minúscula) y X (en mayúscula) son distintas.

Por otro lado existen ciertas normas a la hora de nombrar variables:

* El nombre no puede empezar por un número
* No se permite el uso de guiones -
* Tampoco se permite el uso de espacios.

Se muestran unos ejemplos de nombres de variables válidos y no válidos.

```Python
# Válido

_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

# No válido

2variable = 10
var-iable = 10
var iable = 10
```

Una última condición para nombrar a una variable en Python, es no usar nombres reservados para Python. Las palabras reservadas son utilizadas por Python internamente, por lo que no se pueden utilizar para las variables o funciones.

```Python
import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert'

# 'async', 'await', 'break', 'class', 'continue'

# 'def', 'del', 'elif', 'else', 'except', 'finally'

# 'for', 'from', 'global', 'if', 'import', 'in', 'is'

# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise'

# 'return', 'try', 'while', 'with', 'yield']
```

De hecho con el siguiente comando se pueden ver todas las palabras clave que no se pueden utilizar.

```Python
import keyword
print(keyword.kwlist)
```

### Uso de paréntesis

Python soporta todos los operadores matemáticos más comunes, conocidos como operadores aritméticos. Por lo tanto se pueden realizar sumas, restas, multiplicaciones, exponentes (usando **) y otros que no se explican por el momento. Por ejemplo se realizan varias operaciones en la misma línea, y se almacenan su resultados en y.

```Python
x = 10
y = x*3-3**10-2+3
```

Pero el comportamiento del código anterior y el siguiente es distinto, ya que el uso de paréntesis () da prioridad a unas operaciones sobre otras.

```Python
x = 10
y = (x*3-3)**(10-2)+3
```

El uso de paréntesis no solo se aplica a los operadores aritméticos, sino que también pueden ser aplicados a otros operadores como los relacionales o de membresía. En Python, los operadores relacionales o de membresía se utilizan para comparar valores y evaluar condiciones booleanas. Estos operadores se definen como sigue:

* == (igual que): evalúa si el valor del lado izquierdo es igual al valor del lado derecho.
* != (diferente): evalúa si el valor del lado izquierdo es diferente al valor del lado derecho.
* > (mayor que): evalúa si el valor del lado izquierdo es mayor que el valor del lado derecho.
* < (menor que): evalúa si el valor del lado izquierdo es menor que el valor del lado derecho.
* >= (mayor o igual que): evalúa si el valor del lado izquierdo es mayor o igual que el valor del lado derecho.
* <= (menor o igual que): evalúa si el valor del lado izquierdo es menor o igual que el valor del lado derecho.

Estos operadores se utilizan comúnmente en sentencias ``if`` y ``elif`` para tomar decisiones basadas en condiciones específicas. Por ejemplo:

```Python
x = 5
if x > 3:
    print("x es mayor que 3")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 3")
```

En el anterior ejemplo, se evalúa la condición x > 3 y, si es verdadera, se imprime el mensaje correspondiente. Si no es verdadera, se evalúa la condición x == 5 y, si es verdadera, se imprime otro mensaje. Si ninguna de las condiciones es verdadera, se ejecuta el bloque ``else``.

Además, los operadores relacionales también se utilizan en expresiones que asignan valores booleanos, como en un ejemplo simple:

```Python
a = 4
b = 5
resultado = a <= b  # resultado es True
```

En este caso, el operador <= evalúa la condición y devuelve un valor booleano (True en este caso). Este valor booleano se puede utilizar en sentencias ``if`` o en otras expresiones.

Recuerda que los operadores relacionales son estrictos, lo que significa que 4 no es considerado igual a 4.0, por ejemplo. Si se necesita comparar valores numéricos con precisión decimal, se debe utilizar bibliotecas adicionales como ``decimal`` o ``fractions`` que vendría a ser otro tema de presentación más adelante.

### Variables y alcance

Un concepto muy importante cuando se define una variable, es saber el alcance o scope que tiene. En el siguiente ejemplo la variable con valor 10 tiene un alcance global y la que tiene el valor 5 dentro de la función, tiene un alcance local. Esto significa que cuando hacemos print(x), estamos accediendo a la variable global x y no a la x definida dentro de la función.

```Python
x = 10

def funcion():
    x = 5

funcion()
print(x)
```

Es normal que al inicio de todo este tema se tenga un concepto un poco complicado de observar; pero lo veremos más adelante. Te recomendamos leer los siguientes posts para entender mejor las funciones y el alcance de las variables:

### Funciones en Python y sus argumentos

Las funciones en Python son bloques de código que realizan una tarea específica y pueden ser llamadas desde otras partes del programa. Se definen mediante la palabra clave ``def`` seguida del nombre de la función y paréntesis que pueden contener parámetros.

### Estructura básica de una función en Python

* def nombre_de_la_funcion(Argumentos):

1. Código que realiza la tarea específica.
2. Puede incluir sentencias return para devolver valores.
3. Puede incluir parámetros con valores predeterminados

#### Ejemplos

Una función personalizada que toma un parámetro nombre y devuelve un mensaje de saludo:

```Python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")
```

La función len() es una función incorporada que devuelve la longitud de un objeto:

```Python
print(len("Hola mundo"))  # la longitud es diez (10) caracteres
```

La función input() es una función incorporada que permite obtener la entrada del usuario:

```Python
nombre = input("Ingrese su nombre: ")
print(f"¡Hola, {nombre}!")
```

## Reglas y consejos

1. Utilizar la palabra clave ``def`` para definir funciones
2. Utilizar paréntesis () para contener parámetros
3. Pueden tener cero (0) o más parámetros
4. Pueden devolver valores utilizando la palabra clave ``return``
5. Pueden tener parámetros con valores predeterminados
6. La definición de una función debe ser seguida de dos puntos (:) y el código que la compone debe estar identado con cuatro (4) espacios
7. Las funciones no se ejecutan hasta que no sean invocadas
8. Los parámetros son valores que se esperan recibir cuando se llama a la función

## Conclusión

Las funciones en Python son una herramienta poderosa para organizar y reutilizar el código. Al entender cómo se definen y se utilizan, los programadores pueden escribir programas más eficientes y fáciles de mantener. Es importante seguir las reglas y consejos mencionados para definir y utilizar funciones de manera efectiva.

## Paso por valor y por referencia

Así mismo, en Python, hay dos maneras en que las funciones pueden tratar los parámetros de entrada: paso por valor y paso por referencia.

**1. Paso por valor**: Los tipos simples como enteros, flotantes, cadenas y lógicos se pasan por valor. Esto significa que se crea una copia local de la variable dentro de la función, por lo que cualquier modificación realizada en la función no afecta la variable original. Ver el siguiente ejemplo:

```Python
def incrementar(x): # función llamada incrementar
    x = x + 1 # variable x

x = 5
incrementar(x)
print(x)  # Output: 5
```

En el anterior ejemplo, la variable ``x`` se pasa por valor a la función incrementar. La modificación realizada en la función ``(x = x + 1)`` no afecta la variable original x, que sigue siendo 5.

**2. Paso por referencia**: Los tipos compuestos como listas, [diccionarios](https://devcode.la/tutoriales/diccionarios-en-Python/) y objetos se pasan por referencia. Esto significa que se envía una copia de la referencia a la variable original, por lo que cualquier modificación realizada en la función afecta la variable original. Ver el siguiente ejemplo:

```Python
def agregar_elemento(numeros): # Función llamada agregar_elemento y variable numeros
    numeros.append(4)

numeros = [1, 2, 3]
agregar_elemento(numeros)
print(numeros)  # Output: [1, 2, 3, 4]
```

En el anterior ejemplo, la variable numeros se pasa por referencia a la función ``agregar_elemento``. La modificación realizada en la función (``numeros.append(4)``) afecta la variable original ``numeros``, que ahora contiene cuatro elementos.

Para evitar que los tipos compuestos se modificuen accidentalmente, se puede crear una copia de la lista antes de pasarla como parámetro:

```Python
def agregar_elemento(numeros):
    numeros.append(4)

numeros = [1, 2, 3]
agregar_elemento(numeros[:])  # Crear copia con slicing
print(numeros)  # Output: [1, 2, 3]
```

En este ejemplo, se crea una copia de la lista ``numeros`` utilizando [slicing](https://naps.com.mx/blog/listas-en-Python/) (``numeros[:]``), y se pasa esa copia como parámetro a la función ``agregar_elemento``. La variable original ``numeros`` no se modifica.

## Variable global en Python

En Python, las variables globales son aquellas definidas en el cuerpo principal del programa, fuera de cualquier función. Estas variables son accesibles desde cualquier punto del programa, incluyendo dentro de funciones. También se puede acceder a las variables globales de otros módulos o programas importados.

Por otro lado, las variables locales son aquellas definidas dentro de una función y solo permiten su acceso desde ella. No se pueden acceder o modificar desde fuera de la función en la que se definen.

Para acceder y modificar variables globales, se puede utilizar la función ``globals()``, que devuelve un diccionario que contiene todas las variables del ámbito global actual. Este diccionario se utiliza para acceder al valor de las variables globales y modificarlo. Sin embargo, para variables locales, se utiliza la función ``locals()``, que devuelve un diccionario que contiene todas las variables del ámbito local actual, pero no se puede modificar.

A continuación, te presento un ejemplo que ilustra la diferencia entre variables globales y locales en Python:

```Python
# Variable global llamada global_valor
global_valor = 10

def funcion(): # Función llamada funcion
    # Variable local llamada local_valor
    local_valor = 20
    print(f'La variable local valor es {locals()["local_valor"]}')
    print(f'La variable global valor es {globals()["global_valor"]}')

    # Modificamos la variable global
    globals()['global_valor'] = 30

funcion()
print(f'La variable global valor es ahora {global_valor}')
```

En el anterior ejemplo, se define una variable global llamada ``global_valor`` y una variable local llamada ``local_valor`` dentro de la función llamada ``funcion``. Luego, se modifica el valor de la variable global utilizando el diccionario devuelto por ``globals()``. Al final, se imprime el valor actual de la variable global ``global_valor``, que ha sido modificada dentro de la función.

Es importante destacar que las variables locales no se pueden acceder ni modificar desde fuera de la función en la que se definen, mientras que las variables globales pueden ser accedidas y modificadas desde cualquier punto del programa

### Uso de la función ``print()``

Por último, en cualquier lenguaje de programación es importante saber lo que va pasando a medida que se ejecutan las diferentes instrucciones. Por ello, es interesante hacer uso de ````print()```` en diferentes secciones del código, ya que permiten ver el valor de las variables y muestra información útil.

Existen muchas formas de usar la función ````print()```` y te las explicamos en detalle en este post, pero por ahora basta con que sepas lo básico.

Como ya hemos visto se puede usar ``print()`` para imprimir por pantalla el texto que se quiera ver.

```Python
print("Esto es el contenido a imprimir")
```

De la misma manera, también es posible imprimir el contenido de una variable.

```Python
x = 10
print(x)
```

Ahora, separando por comas estos valores, es posible imprimir el texto y el contenido de variables.

```Python
x = 10
y = 20
print("Los valores x, y son:", x, y)

# Salida: Los valores x, y son: 10 20
```

## Creación de nuestro primer archivo

1. First list item
   * First nested list item
     * Second nested list item

Estando ya dentro del editor; se procede a crear un archivo con el nombre que quiera utilizar el usuario; no sin antes advertir que debe de tener la extensión punto py (.py)

* [ ] #739
* [ ] <https://github.com/octo-org/octo-repo/issues/740>
* [ ] Add delight to the experience when all tasks are complete :tada: