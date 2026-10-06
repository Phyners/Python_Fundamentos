# ==========================================
# 03: STRINGS (Cadenas de texto)
# ==========================================

# ==========================================
# CREACIÓN Y OPERACIONES BÁSICAS
# ==========================================

    # 1. Creación Básica y Multilínea
    # Puedes usar comillas simples o dobles. Para textos de varias líneas, usa triples.
texto_simple = "Hola Mundo"
texto_largo = """Este es un texto
que respeta los saltos de línea
tal y como los escribes."""

    # 2. Caracteres de Escape (Trucos dentro del texto)
        # \n  -> Nueva Línea (Enter)
        # \t  -> Tabulador (Crea un espacio grande)
        # \\  -> Imprime una barra diagonal '\' real
        # \' o \" -> Permite imprimir comillas dentro de un texto con comillas

    # 3. Operaciones Matemáticas con Textos
        # Concatenar (+) : "Hola " + "Mundo" -> "Hola Mundo"
        # Repetir (*)    : "Ja" * 3          -> "JaJaJa"

    # 4. Longitud y Pertenencia
        # len() -> Cuenta caracteres (incluyendo espacios): len("Hola") -> 4
        # in    -> Busca sub-textos: "py" in "python" -> True


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
        # %% (porcentaje): Imprime el símbolo '%' literal

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
# EJEMPLO PRÁCTICO: GENERADOR DE USUARIOS CORPORATIVOS
# ==========================================
print("\n--- SISTEMA DE RECURSOS HUMANOS ---")
print("Por favor, ingresa tus datos para generar tu perfil corporativo.")

# 1. Recibimos un input "sucio" interactivo
# Prueba a escribirlo mal a propósito: con mayúsculas mezcladas y espacios locos.
datos_crudos = input("Ingresa Nombre, Apellido y Año separados por coma (Ej: '   aLeJaNdRo, piÑeRoS , 2004   '): ")

# 2. LIMPIEZA Y DIVISIÓN (Strip y Split)
# Dividimos el texto por la coma para obtener una lista con las 3 partes
datos_lista = datos_crudos.split(',')

# 3. ASIGNACIÓN Y FORMATO (Unpacking y Métodos de limpieza)
# Sacamos cada parte, le borramos los espacios extra (strip) y arreglamos las mayúsculas (title)
nombre = datos_lista[0].strip().title()       
apellido = datos_lista[1].strip().title()     
anio = datos_lista[2].strip()                 

# 4. VALIDACIONES (Métodos 'is...')
anio_valido = anio.isdigit()  # ¿El año tiene solo números? -> True/False
nombre_valido = nombre.isalpha() # ¿El nombre tiene solo letras? -> True/False

# 5. ÍNDICES Y SLICING (Creando el "Usuario" de la empresa)
# Regla de la empresa: 1ª letra del nombre + 3 primeras del apellido + 2 últimos números del año
inicial_nombre = nombre[0].lower()       # ej: "a"
inicio_apellido = apellido[:3].lower()   # ej: "piñ"
final_anio = anio[-2:]                   # ej: "04"

usuario_corp = inicial_nombre + inicio_apellido + final_anio # ej: "apiñ04"

# 6. BÚSQUEDA Y OPERACIONES MATEMÁTICAS CON STRINGS
nombre_completo = nombre + " " + apellido
vocales_a = nombre_completo.lower().count('a') # Usamos lower() para contar todas las 'a' sin importar mayúsculas/minúsculas
linea_separadora = "-" * 40  # Repetimos el guion 40 veces

# ==========================================
# RESULTADOS USANDO LOS 3 TIPOS DE FORMATEO
# ==========================================
print("\n\t[ CARNET GENERADO CON ÉXITO ]\n")
print(linea_separadora)

# Formateo 1: Clásico con %
print("Empleado Registrado : %s %s" % (nombre, apellido))

# Formateo 2: Con .format() (Alineación a la derecha en 15 espacios)
print("Usuario Corporativo : {:>15}".format(usuario_corp))
print("Contraseña Temporal : {:>15}".format(nombre[::-1] + anio)) # Nombre al revés concatenado al año

# Formateo 3: F-Strings (Lógica directa dentro de llaves)
print(f"Correo Asignado     : {usuario_corp}@empresa.com")
print(f"Seguridad           : Año numérico válido -> {anio_valido}")
print(f"Curiosidad          : Tu nombre contiene {vocales_a} letras 'A'.")

print(linea_separadora)