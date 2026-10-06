# ==========================================
# 04: LISTAS (Colecciones de datos)
# ==========================================
# Las listas sirven para guardar muchos elementos en una sola variable.
# Son ORDENADAS (tienen índice) y MUTABLES (se pueden modificar).

# ==========================================
# 1. CREACIÓN Y CONCEPTOS BÁSICOS
# ==========================================
# Se crean usando corchetes [] o la función list().
lista_vacia = []
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja", "mango"]

# ¡En Python las listas pueden mezclar diferentes tipos de datos!
mixta = ["Alejandro", 23, True, 3.14, {"pais": "España"}]

# len() -> Cuenta cuántos elementos hay en total
# print(len(frutas)) -> 4


# ==========================================
# 2. ACCESO Y SLICING (Extraer datos)
# ==========================================
# Funciona EXACTAMENTE igual que con los Strings (textos).
    # frutas = ["manzana", "banana", "naranja", "mango"]
    #              0          1          2         3

    # Índices:
        # frutas[0]   -> "manzana" (El primer elemento)
        # frutas[-1]  -> "mango"   (El último elemento)

    # Slicing (Rebanado) [inicio : fin_sin_incluir : saltos]:
        # frutas[1:3] -> ['banana', 'naranja']
        # frutas[:2]  -> ['manzana', 'banana'] (Desde el inicio hasta el 1)
        # frutas[::-1]-> ['mango', 'naranja', 'banana', 'manzana'] (Invierte la lista)

    # Comprobar si existe (Operador 'in'):
        # "naranja" in frutas -> True


# ==========================================
# 3. MODIFICAR Y AÑADIR ELEMENTOS
# ==========================================
# A diferencia de los strings, las listas SÍ se pueden cambiar internamente.

    # Cambiar un valor existente:
        # frutas[0] = "kiwi"  -> Ahora la lista empieza por 'kiwi' en vez de 'manzana'

    # Añadir al final (El más usado):
        # frutas.append("pera") -> Añade 'pera' al final de la lista.

    # Insertar en una posición específica:
        # frutas.insert(1, "uva") -> Empuja 'uva' a la posición 1, desplazando el resto.

    # Unir dos listas:
        # frutas.extend(["limón", "fresa"]) -> Pega los elementos de la nueva lista al final.
        # (También se puede usar suma: lista3 = frutas + ["limón", "fresa"])


# ==========================================
# 4. ELIMINAR ELEMENTOS
# ==========================================
    
    # remove() -> Borra el elemento por su NOMBRE. (Si hay varios, borra el primero).
        # frutas.remove("banana")

    # pop() -> Borra por ÍNDICE y además TE DEVUELVE el elemento borrado.
        # robado = frutas.pop()  -> Borra y guarda el ÚLTIMO elemento.
        # robado = frutas.pop(0) -> Borra y guarda el PRIMER elemento.

    # del -> Borra por índice o destruye variables (Cuidado con él).
        # del frutas[1:3] -> Borra un trozo entero de la lista.

    # clear() -> Vacía la lista por completo, dejándola como [].
        # frutas.clear()


# ==========================================
# 5. ORDENAR, COPIAR Y OTROS MÉTODOS
# ==========================================
    # letras = ['z', 'a', 'b', 'c', 'c']

    # count()   -> letras.count('c') -> 2 (Cuenta cuántas veces aparece)
    # index()   -> letras.index('b') -> 2 (Devuelve en qué posición está la 'b')
    # reverse() -> letras.reverse()  -> Le da la vuelta a la lista.

    # Ordenar alfabéticamente/numéricamente:
        # letras.sort()             -> Ordena de la A a la Z modificando la lista original.
        # letras.sort(reverse=True) -> Ordena de la Z a la A.
        # sorted(letras)            -> Crea una lista nueva ordenada sin alterar la original.

    # Copiar una lista (¡MUY IMPORTANTE!):
        # ⚠️ MAL: lista2 = letras -> Si modificas lista2, ¡también se modifica letras!
        # ✅ BIEN: lista2 = letras.copy() -> Crea un clon independiente.


# ==========================================
# 6. DESEMPAQUETADO AVANZADO (Unpacking con *)
# ==========================================
# Si tienes una lista larga y solo te importan los primeros datos:
    # paises = ["España", "Francia", "Italia", "Alemania", "Portugal"]
    # primero, segundo, *resto = paises
    
    # print(primero) -> "España"
    # print(segundo) -> "Francia"
    # print(resto)   -> ["Italia", "Alemania", "Portugal"] (Las agrupa en una lista nueva)


# ==========================================
# EJEMPLO PRÁCTICO: CARRITO DE COMPRAS INTERACTIVO
# ==========================================
print("\n--- AMAZON: TU CARRITO DE COMPRAS ---")

# 1. Lista inicial del usuario
carrito = ["Teclado", "Ratón", "Monitor"]
print(f"Estado inicial: {carrito}")

# 2. El usuario añade un producto nuevo (append)
nuevo_producto = input("¿Qué producto quieres añadir al carrito?: ").strip().title()

if nuevo_producto:  # Aprovechamos el truco 'Falsy' por si pulsa Enter sin escribir
    carrito.append(nuevo_producto)
    print(f"✅ '{nuevo_producto}' añadido al carrito.")
else:
    print("⚠️ No escribiste nada. No se añadió nada.")

# 3. Promoción especial (insert)
print("\n🎁 ¡SORPRESA! Te regalamos una 'Alfombrilla' por tu fidelidad.")
carrito.insert(0, "Alfombrilla") # La ponemos de primera en la lista

# 4. Eliminación de un elemento (pop y remove)
print("\n💳 Procesando pago...")
if "Monitor" in carrito:
    carrito.remove("Monitor")
    print("❌ 'Monitor' eliminado porque no hay stock.")

# Sacamos el último elemento añadido para enviarlo por separado
envio_separado = carrito.pop()
print(f"📦 El producto '{envio_separado}' se enviará en una caja aparte.")

# 5. Ordenación e Impresión final (sort)
carrito.sort() # Ordenamos lo que queda alfabéticamente
total_items = len(carrito)

print("\n--- RESUMEN DE TU PEDIDO ---")
print(f"Artículos finales en la caja principal ({total_items}): {carrito}")

# 6. Desempaquetado (El primer ítem es el regalo, el resto compras)
if total_items >= 2:
    regalo, *compras = carrito
    print(f"Tu regalo es: {regalo}")
    print(f"Tus compras son: {compras}")

print("\n¡Gracias por tu compra!")