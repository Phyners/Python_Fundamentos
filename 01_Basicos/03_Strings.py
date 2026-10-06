### Strings ###

#   \n: Nueva Linea
#   \t: Tab(8 espacios)
#   \" , \' , \\: Comilla Simple ('), Comilla Doble ("), Back slash (\)

# ==========================================
# FORMATEO DE CADENAS ESTILO %
# ==========================================

    # Formateo de Textos y Caracteres
        # %s (string): Convierte a texto legible (usa str())
        # %r (repr): Texto interno de Python, incluye comillas (usa repr())
        # %a (ascii): Como %r pero pasa caracteres especiales a ASCII
        # %c (char): Un único carácter (acepta letra suelta o código ASCII)

    # Formateo de Números Enteros
        # %d (decimal): Número entero normal en base 10
        # %i (integer): Exactamente igual que %d
        # %u (unsigned): Igual que %d en Python actual
        # %o (octal): Convierte el número a base 8
        # %x (hex minúscula): Base 16 usando letras minúsculas (a-f)
        # %X (hex mayúscula): Base 16 usando letras mayúsculas (A-F)

    # Formateo de Números Decimales (Floats)
        # %f (float): Decimal normal (pone 6 decimales por defecto)
        # %F (float): Igual que %f, pero escribe INF/NAN en mayúsculas
        # %e (exponencial): Notación científica (ej. 1.2e+03)
        # %E (exponencial): Igual pero con 'E' mayúscula (ej. 1.2E+03)
        # %g (general): Usa %f o %e automáticamente (el que quede más corto)
        # %G (general): Igual que %g pero con letras mayúsculas

    # Especial
        # %%(porcentaje): Imprime el símbolo '%' literal

    # Modificadores (Se ponen entre el % y la letra)
        # %.Nf : Limita a N decimales precisos (ej. %.2f -> 3.14)
        # %0Nd : Rellena con ceros hasta tener N cifras (ej. %05d -> 00042)
        # %Ns  : Alinea a la derecha ocupando N espacios (ej. %10s)


# ==========================================
# FORMATEO CON .format() (Python 3+)
# ==========================================

    # Sintaxis básica y posiciones
        # "{}".format(var)       : Inserta la variable en las llaves
        # "{0} {1}".format(a, b) : Por índice (0 es 'a', 1 es 'b')
        # "{1} {0}".format(a, b) : Cambia el orden (imprime 'b' y luego 'a')
        # "{n}".format(n="Ana")  : Por nombre de variable (keyword)

    # Modificadores (Se pone ':' dentro de las llaves)
        # {:.2f}  : Limita a 2 decimales (ej. 3.14)
        # {:05d}  : Rellena con ceros hasta 5 cifras (ej. 00042)
        # {:>10}  : Alinea a la derecha en 10 espacios
        # {:<10}  : Alinea a la izquierda en 10 espacios
        # {:^10}  : Centra el texto en 10 espacios
        # {:,}    : Separador de miles con coma (ej. 1,000,000)
        # {:_}    : Separador de miles con guion bajo (ej. 1_000_000)
        # {:b}    : Convierte a Binario (ej. 5 -> 101)


# ==========================================
# F-STRINGS (Python 3.6+ -> LA MÁS RECOMENDADA)
# ==========================================
    # Se pone una 'f' o 'F' antes de las comillas: f"texto {variable}"

    # Usos principales
        # f"Hola {nombre}"       : Inserta variables directamente
        # f"Suma: {2 + 2}"       : Permite operaciones matemáticas directas
        # f"{nombre.upper()}"    : Permite ejecutar métodos/funciones dentro

    # Modificadores (Son EXACTAMENTE los mismos que en .format())
        # f"{precio:.2f}"        : Variable con 2 decimales
        # f"{numero:05d}"        : Rellena con ceros

    # Truco de Debugging (Python 3.8+)
        # f"{variable=}"         : Imprime el nombre y el valor (ej. variable=42)


# ==========================================
# OTRAS FORMAS (Menos usadas)
# ==========================================

    # 1. Concatenación básica (+)
        # "Hola " + nombre + ", tienes " + str(edad) 
        # (Poco eficiente y obliga a usar str() en los números manualmente)

    # 2. Template Strings (Módulo 'string')
        # from string import Template
        # t = Template("Hola $nombre")
        # t.substitute(nombre="Juan")
        # (Se usa casi exclusivamente cuando el texto viene del usuario, por seguridad)


# ==========================================
# STRINGS COMO SECUENCIAS (Índices y Slicing)
# ==========================================
    # texto = "Python" -> P(0) y(1) t(2) h(3) o(4) n(5)

    # 1. Desempaquetado (Unpacking)
        # Asignar cada letra a una variable distinta.
        # a, b, c = "Sol"  # a='S', b='o', c='l'

    # 2. Índices (Acceder a UNA letra)
        # Los números positivos cuentan desde el principio (empezando en 0)
        # Los números negativos cuentan desde el final (empezando en -1)
        # texto[0]   -> 'P' (Primera letra)
        # texto[-1]  -> 'n' (Última letra)
        # texto[-2]  -> 'o' (Penúltima letra)

    # 3. Slicing o "Rebanado" (Extraer un trozo)
        # Sintaxis: texto[inicio : fin_sin_incluir : saltos]
        # texto[0:3] -> 'Pyt' (Índices 0, 1 y 2. ¡El 3 NO entra!)
        # texto[3:6] -> 'hon' (Índices 3, 4 y 5)
        
        # Atajos de Slicing (Si omites números, Python asume los extremos)
        # texto[:3]  -> 'Pyt' (Desde el inicio hasta el índice 2)
        # texto[3:]  -> 'hon' (Desde el índice 3 hasta el final)

    # 4. Saltos y Reverso (Step)
        # texto[0:6:2] -> 'Pto' (De principio a fin, saltando de 2 en 2)
        # texto[::-1]  -> 'nohtyP' (¡El truco de oro para invertir textos!)

# ==========================================
# MÉTODOS DE STRINGS (Textos)
# ==========================================
    # texto = "python mola"

    # 1. Modificar Mayúsculas/Minúsculas
        # texto.capitalize() -> 'Python mola' (Solo la primera letra de la frase)
        # texto.title()      -> 'Python Mola' (La primera de CADA palabra)
        # texto.swapcase()   -> Invierte: minúsculas a mayúsculas y viceversa
        # texto.upper()      -> 'PYTHON MOLA' (Todo mayúsculas)
        # texto.lower()      -> 'python mola' (Todo minúsculas)

    # 2. Buscar y Contar
        # texto.count('o')       -> 2 (Cuántas veces aparece la letra/palabra)
        # texto.startswith('py') -> True (¿Empieza con esto?)
        # texto.endswith('la')   -> True (¿Termina con esto?)
        
        # texto.find('m')  -> 7 (Índice de la primera 'm'. Si no existe, devuelve -1)
        # texto.rfind('o') -> 8 (Índice de la ÚLTIMA 'o'. Si no existe, devuelve -1)
        # texto.index('m') -> 7 (Igual que find, pero si NO existe, lanza un ERROR)
        # texto.rindex('o')-> 8 (Igual que rfind, pero con ERROR si no existe)

    # 3. Limpiar, Reemplazar, Dividir y Unir (¡Los más usados!)
        # "  hola  ".strip()            -> 'hola' (Borra espacios al inicio y final)
        # texto.replace('mola', 'top')  -> 'python top' (Cambia A por B)
        # "a,b,c".split(',')            -> ['a', 'b', 'c'] (Corta el texto y crea una lista)
        # "-".join(['a', 'b', 'c'])     -> 'a-b-c' (Une una lista usando el texto como pegamento)
        # "a\tb".expandtabs(4)          -> 'a   b' (Cambia los tabuladores por espacios)

    # 4. Validaciones (Devuelven True o False)
        # texto.isalpha()  -> False (¿Son SOLO letras? Falso por el espacio)
        # texto.isalnum()  -> False (¿Son letras y números? Falso por el espacio)
        # texto.islower()  -> True  (¿Está TODO en minúsculas?)
        # texto.isupper()  -> False (¿Está TODO en mayúsculas?)
        # "var_1".isidentifier() -> True (¿Sirve como nombre de variable? ej: no empezar por número)

    # 5. Diferencias locas al validar Números
        # "123".isdecimal() -> True (Solo números del 0-9 normales)
        # "3²".isdigit()    -> True (Acepta 0-9 y superíndices como el ²)
        # "½".isnumeric()   -> True (Acepta TODO lo anterior más fracciones)


# ==========================================
# EJEMPLO PRÁCTICO: PROCESADOR DE PERFILES
# ==========================================

print("\n--- INICIO DEL EJEMPLO PRÁCTICO ---")

# 1. Recibimos un texto "sucio" (con espacios extra y mayúsculas/minúsculas mezcladas)
datos_crudos = "   aLeJaNdRo, piÑeRoS, 23 , pYtHoN   "

# 2. LIMPIEZA Y DIVISIÓN (Strip, Replace y Split)
# Primero limpiamos los espacios de los bordes y luego dividimos por la coma
datos_lista = datos_crudos.strip().replace(" ", "").split(',')
# Resultado interno: ['aLeJaNdRo', 'piÑeRoS', '23', 'pYtHoN']

# 3. ASIGNACIÓN Y FORMATO DE MAYÚSCULAS/MINÚSCULAS (Unpacking y Métodos)
nombre, apellido, edad, lenguaje = datos_lista
nombre = nombre.title()       # "Alejandro"
apellido = apellido.title()   # "Piñeros"
lenguaje = lenguaje.upper()   # "PYTHON"

# 4. VALIDACIONES (Métodos 'is...')
edad_valida = edad.isdigit()  # ¿La edad contiene solo números? -> True

# 5. ÍNDICES Y SLICING (Creando un "Nickname" de usuario)
# Tomamos las 3 primeras letras del nombre y las 3 últimas del apellido
nick_inicio = nombre[:3]      # "Ale"
nick_fin = apellido[-3:]      # "ros"
nickname = (nick_inicio + nick_fin).lower()  # "aleros"

# 6. BÚSQUEDA (Count y secuencias)
nombre_completo = f"{nombre} {apellido}"
cantidad_a = nombre_completo.lower().count('a') # Cuenta cuántas 'a' hay en total

# ==========================================
# RESULTADOS USANDO LOS 3 TIPOS DE FORMATEO
# ==========================================
print("\n\t[Perfil Generado]\n")

# Formateo 1: Clásico con %
print("Nombre completo: %s %s" % (nombre, apellido))

# Formateo 2: Con .format() (alineando a la derecha y rellenando la edad)
print("Nickname : {:>8}".format(nickname))
print("Edad     : {:05d}".format(int(edad))) # Se convierte a int() para usar el relleno con ceros

# Formateo 3: F-Strings (Poniendo lógica directamente dentro de las llaves)
print(f"Lenguaje : {lenguaje.replace('PYTHON', 'Python 3')}")
print(f"Seguridad: ¿Edad es número válido? -> {edad_valida}")
print(f"Curiosidad: Tu nombre al revés es '{nombre_completo[::-1]}'")
print(f"Estadística: Tu nombre completo tiene {cantidad_a} letras 'a'.")