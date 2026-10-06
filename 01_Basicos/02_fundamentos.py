# ==========================================
# 02: FUNDAMENTOS DE PYTHON 
# ==========================================

# ==========================================
# INTRODUCCIÓN Y TIPOS DE DATOS
# ==========================================

# 1. COMENTARIOS
# El hashtag sirve para comentar una sola línea.
"""
Las triples comillas dobles (o simples) crean textos multilínea.
Si no los guardas en una variable, Python los ignora.
Por eso se usan como comentarios largos.
"""

# 2. SALIDA BÁSICA (print)
print("¡Hola Mundo!")
# Unimos texto y variables separándolos con comas:
print("El número es:", 10) 

# 3. VERIFICACIÓN DE TIPOS (type)
# Python asigna el tipo automáticamente. type() nos dice cuál es.
print(type(10))                  # <class 'int'>      (Enteros)
print(type(3.14))                # <class 'float'>    (Decimales, siempre con punto)
print(type(1 + 3j))              # <class 'complex'>  (Complejos, matemáticos)
print(type("Hola"))              # <class 'str'>      (Strings / Cadenas de texto)
print(type(True))                # <class 'bool'>     (Booleanos: True o False)

# Colecciones básicas (Se verán a fondo más adelante):
print(type([1, 2, 3]))           # <class 'list'>     (Listas)
print(type((1, 2, 3)))           # <class 'tuple'>    (Tuplas)
print(type({1, 2, 3}))           # <class 'set'>      (Sets)
print(type({"nombre": "Alex"}))  # <class 'dict'>     (Diccionarios)


# ==========================================
# VARIABLES Y FUNCIONES INTEGRADAS
# ==========================================

# 1. VARIABLES (Cajas en la memoria)
# Reglas válidas (Snake Case es estándar): primer_nombre, edad_usuario, num_1
# Reglas inválidas: 1_numero (inicia con número), mi-nombre (guion), mi nombre (espacio)
nombre = "Alejandro"
edad = 23
es_estudiante = True

# Asignación múltiple en una sola línea:
pais, ciudad, codigo_postal = "España", "Barcelona", 8013

# 2. FUNCIONES INTEGRADAS (Built-in functions)
# Python tiene decenas de funciones nativas listas para usar.
# Aquí están las más importantes agrupadas por utilidad:

    # A. Matemáticas Básicas
        # abs(-5)      -> 5 (Valor absoluto)
        # round(3.14)  -> 3 (Redondea al entero más cercano)
        # min(1, 5, 2) -> 1 (Encuentra el mínimo)
        # max(1, 5, 2) -> 5 (Encuentra el máximo)
        # sum([1, 2])  -> 3 (Suma los elementos)
        # pow(2, 3)    -> 8 (Potencia, igual que 2 ** 3)
        # divmod(10, 3)-> (3, 1) (Devuelve el cociente y el resto)

    # B. Utilidades de Sistema e Información
        # print()      -> Imprime en pantalla
        # input()      -> Pide datos (⚠️ SIEMPRE devuelve un string)
        # len("Hola")  -> 4 (Cuenta la longitud)
        # type(var)    -> Devuelve el tipo de dato
        # id(var)      -> Devuelve el número de identidad en la memoria RAM
        # help(print)  -> Muestra el manual de ayuda de una función
        # dir(var)     -> Muestra métodos que se le pueden aplicar a algo
 
# 3. CASTING (Conversión de tipos de datos)
# Transformamos un tipo de dato en otro usando int(), float(), str(), bool()
num_texto = "10"
num_entero = int(num_texto)      # 10 (Ahora sí podemos sumar)
gravedad = int(9.81)             # 9 (Corta el decimal)
peso = float(75)                 # 75.0 (Añade decimal)
edad_texto = str(23)             # "23" (Convierte número a texto)


# ==========================================
# OPERADORES Y BOOLEANOS
# ==========================================

# 1. OPERADORES ARITMÉTICOS
a = 10
b = 3

print("Suma:", a + b)            # 13
print("Resta:", a - b)           # 7
print("Multiplicación:", a * b)  # 30
print("División:", a / b)        # 3.3333333333333335 (Siempre devuelve float)
print("Div. Entera:", a // b)    # 3 (Elimina los decimales, no redondea)
print("Módulo:", a % b)          # 1 (Es el resto de la división. 10/3=3, sobra 1)
print("Exponente:", a ** b)      # 1000 (10 elevado a 3)

# 2. OPERADORES DE ASIGNACIÓN (Atajos)
# Actualizan el valor de una variable existente.
c = 5
c += 3                           # Equivale a: c = c + 3 (Ahora c vale 8)
c -= 2                           # Equivale a: c = c - 2 (Ahora c vale 6)
c *= 2                           # Equivale a: c = c * 2 (Ahora c vale 12)

# 3. OPERADORES DE COMPARACIÓN
# Comparan dos valores y siempre devuelven un Booleano (True o False).
print("Igualdad:", a == b)       # False
print("Diferencia:", a != b)     # True
print("Mayor que:", a > b)       # True
print("Menor que:", a < b)       # False
print("Mayor o igual:", a >= b)  # True
print("Menor o igual:", a <= b)  # False

# Comparando textos (Python los evalúa por su valor alfabético ASCII)
print("Manzana" == "manzana")    # False (Las mayúsculas importan)
print("A" > "B")                 # False (La B está después, por lo que vale más)
print(len("Hola") == len("Gato"))# True (Compara el tamaño: 4 == 4)

# 4. OPERADORES DE PERTENENCIA E IDENTIDAD
    # in -> ¿Está dentro?
print("a" in "manzana")          # True
print(1 in [1, 2, 3])            # True

    # not in -> ¿NO está dentro? 
print("a" not in "hola")         # False
print(4 not in [1, 2, 3])        # True

    # is -> ¿Es exactamente el mismo objeto en memoria?
lista_1 = [1, 2]
lista_2 = [1, 2]
lista_3 = lista_1
lista_4 = None

print(lista_1 is lista_3)        # True (lista_3 es la misma caja en memoria que lista_1)
print(lista_1 is lista_2)        # False (Son cajas distintas, aunque tengan lo mismo adentro)
# '==' compara contenido, 'is' compara identidad en memoria:
print(lista_1 == lista_2)        # True (Tienen el mismo contenido exacto)

    # is not -> ¿Son objetos diferentes?
print(lista_1 is not lista_2)    # True (Son objetos distintos en memoria)

    # None -> Comprueba si una variable no tiene valor asignado
print(5 is None)                 # False (5 no es nulo)
print(lista_4 is None)              # True (lista_4 no tiene valor asignado, es nula)

# 5. VALORES "FALSY" (El secreto de los Booleanos)
# Todo en Python es True por defecto, EXCEPTO los que representan la "nada":
    # 0, 0.0                -> Números cero
    # ""                    -> Textos vacíos
    # False                 -> Booleano Falso
    # [], {}, (), set()     -> Colecciones vacías
    # None                  -> Ausencia total de valor
# 💡 Tip Pro: En vez de 'if len(lista) == 0:', escribe 'if not lista:'.

# 6. TABLAS DE VERDAD Y OPERADORES LÓGICOS (and, or, not)
    # and -> Devuelve True SOLO SI AMBAS condiciones se cumplen.
print(3 > 2 and 4 > 3)           # True
print(3 > 2 and 4 < 3)           # False
    
    # or -> Devuelve True SI AL MENOS UNA condición se cumple.
print(3 > 2 or 4 < 3)            # True (La primera se cumple, ignora la segunda)
    
    # not -> Invierte el resultado.
print(not True)                  # False
print(not (3 > 2))               # False
   
    # A       B     | A and B | A or B
    # --------------------------------
    # True    True  | True    | True    
    # True    False | False   | True    
    # False   True  | False   | True    
    # False   False | False   | False   
    # --------------------------------

# 7. JERARQUÍA DE OPERACIONES LÓGICAS (Orden de prioridad)
# Si hay varios en una línea, Python los resuelve en este orden:
    # 1. () Paréntesis (Máxima prioridad)
    # 2. not (Negación)
    # 3. and (Y lógico)
    # 4. or  (O lógico - Mínima prioridad)
# Ejemplos: 
# 1º Resuelve el and (False) -> 2º Resuelve el or (True or False) = True.
print(True or True and False)    # True
# 1º Resuelve paréntesis (True) -> 2º Resuelve and (True and False) = False.
print((True or True) and False)  # False


# ==========================================
# EJEMPLO PRÁCTICO: EVALUADOR DE TARJETA DE CRÉDITO
# ==========================================
print("\n--- SISTEMA BANCARIO: EVALUACIÓN DE CRÉDITO ---")

# 1. Recolección de datos y Casting
nombre = input("Nombre y apellido del solicitante: ")
edad = int(input("Edad del solicitante: "))
ingresos = float(input("Ingresos mensuales (€): "))
gastos = float(input("Gastos mensuales (€): "))

# Pedimos un dato opcional para jugar con los valores Falsy
avalista = input("Nombre del avalista (Pulsa Enter para dejar en blanco si no tiene): ")

# 2. Operaciones Aritméticas y de Asignación
ingresos_libres = ingresos - gastos
ahorro_anual = ingresos_libres * 12

# Simulamos que el banco cobra una tasa administrativa de 15€ restándolo directo
ingresos_libres -= 15.0  

# 3. Uso de Valores Falsy y Booleanos
# Si el usuario pulsó Enter sin escribir nada, el texto está vacío (""). 
# bool("") devuelve False. Si escribió un nombre, devuelve True.
tiene_aval = bool(avalista) 

# 4. Operadores de Identidad (is)
# Como es un cliente nuevo, su nivel de riesgo aún no existe (es nulo)
perfil_riesgo = None
pendiente_revision = perfil_riesgo is None # Esto dará True

# 5. Operadores de Comparación y Lógica Compleja (Jerarquía)
es_mayor_edad = edad >= 18
capacidad_pago = ingresos_libres > 500

# LÓGICA DEL BANCO: 
# Para aprobar, DEBE ser mayor de edad Y (Tener capacidad de pago O tener un aval)
# Usamos paréntesis para agrupar el 'or' antes del 'and'
aprobado = es_mayor_edad and (capacidad_pago or tiene_aval)

# --- IMPRESIÓN DE RESULTADOS ---
print("\n--- RESUMEN FINANCIERO ---")
print("Cliente:", nombre)
print("Dinero libre estimado tras tasa:", ingresos_libres, "€")
print("¿Tiene un avalista registrado?:", tiene_aval)
print("¿El perfil de riesgo requiere revisión manual?:", pendiente_revision)

print("\n--- DECISIÓN AUTOMÁTICA DEL SISTEMA ---")
print("¿Cumple requisito de mayoría de edad?:", es_mayor_edad)
print("¿Tiene capacidad de pago (más de 500€ libres)?:", capacidad_pago)
print("¿TARJETA APROBADA?:", aprobado)

print("\n¡Fin de la evaluación!")