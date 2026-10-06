# ==========================================
# 00: LÓGICA Y PSEUDOCÓDIGO
# ==========================================

## 1. ¿Qué es el Pseudocódigo?
Antes de empezar a escribir código real en Python (o cualquier lenguaje), usamos el pseudocódigo como nuestro **borrador mental**. 

Se redacta usando lenguaje simple, humano y paso a paso para definir cómo vamos a resolver un problema. Esto te permite enfocarte al 100% en la **lógica** sin estresarte por si te falta una coma, un paréntesis o si escribiste mal un comando de Python. ¡Primero piensa, luego programa!

---

## 2. Variables y la Regla de Oro del Símbolo "="
Imagina que la memoria de tu ordenador es un almacén lleno de cajas vacías.
En programación, usamos el símbolo `=` **NO como una igualdad matemática**, sino como una orden de **guardado o asignación**.

* **La regla:** "Guarda lo que está a la derecha, dentro de la caja de la izquierda".
* **Ejemplo:** `edad = 25` (El sistema toma el número 25 y lo mete en una caja a la que le pone la etiqueta "edad").
* **Ejemplo actualizable:** `vidas = vidas - 1` (Toma las vidas actuales, réstales una, y guarda el nuevo resultado en la misma caja).

---

## 3. El Cerebro del Programa (Estructuras de Control)
Todo programa, desde una calculadora hasta un videojuego, se construye combinando estas tres formas de leer instrucciones:

1. **Secuencial (Paso a paso):** El código se lee de arriba hacia abajo, una línea tras otra.
2. **Condicional (Bifurcaciones):** El programa toma decisiones.
   * `Si` ocurre esto -> haz el Plan A.
   * `Sino` -> haz el Plan B.
3. **Iterativa (Bucles/Repeticiones):** El programa repite una acción hasta que se cumpla una regla.
   * `Mientras` pase esto -> repite el código.

---

## 4. Diccionario de Acciones Básicas
Para escribir pseudocódigo, usaremos estas palabras clave estandarizadas:
* **Pedir:** El usuario introduce información mediante el teclado.
* **Mostrar:** El PC responde al usuario imprimiendo texto en la pantalla.
* **Guardar:** Se crea una variable para recordar un dato.
* **Calcular:** Se realizan operaciones matemáticas.

### Operadores Clave para usar en tu lógica:
* **Matemáticas:** `+`, `-`, `*`, `/`
* **Comparaciones:** `==` (es igual a), `!=` (es diferente de), `>`, `<`.
* **Lógicos:** 
  * `Y` (Se deben cumplir AMBAS cosas. Ej: *Si es mayor de 18 Y tiene entrada*).
  * `O` (Con que se cumpla UNA basta. Ej: *Si es sábado O domingo -> no trabajo*).

---

## 5. EJERCICIOS PRÁCTICOS DE LÓGICA

A continuación, ejemplos desde lo más básico hasta lógica más compleja. Léelos como si fueras el ordenador ejecutando las órdenes.

### Ejercicio 1: Nivel Básico (Secuencial pura)
**Contexto:** Un programa que calcula el IVA (21%) de un producto.

**Pseudocódigo:**
Mostrar: "Bienvenido a la calculadora de impuestos"
Pedir: Precio del producto
Guardar: precio_base

Calcular: iva = precio_base * 0.21
Calcular: precio_final = precio_base + iva

Mostrar: "El producto cuesta un total de:"
Mostrar: precio_final


### Ejercicio 2: Nivel Intermedio (Condicionales lógicos)
**Contexto:** Sistema de seguridad de una montaña rusa. Solo pasas si tienes la edad Y la altura adecuada.

**Pseudocódigo:**
Pedir: Edad del visitante
Guardar: edad
Pedir: Altura del visitante en cm
Guardar: altura

Si edad >= 12 Y altura >= 150:
    Mostrar: "¡Puedes subir a la atracción!"
Sino Si edad < 12:
    Mostrar: "Lo siento, eres demasiado joven."
Sino:
    Mostrar: "Lo siento, no alcanzas la altura mínima de seguridad."


### Ejercicio 3: Nivel Intermedio-Alto (Bucles + Condicionales)
**Contexto:** Un inicio de sesión de un banco. Tienes 3 intentos antes de que se bloquee la cuenta.

**Pseudocódigo:**
Guardar: pin_correcto = "1234"
Guardar: intentos = 3

Mientras intentos > 0:
    Pedir: "Introduce tu PIN"
    Guardar: intento_usuario

    Si intento_usuario == pin_correcto:
        Mostrar: "Acceso concedido. Bienvenido a tu cuenta."
        Terminar programa
    Sino:
        Calcular: intentos = intentos - 1
        Mostrar: "PIN Incorrecto. Te quedan", intentos, "intentos."

Mostrar: "Cuenta bloqueada por seguridad. Acude a una sucursal."


### Ejercicio 4: Nivel Avanzado (Taquilla de Cine Completa)
**Contexto:** Vender entradas aplicando descuentos y calculando el cambio en efectivo.

**Pseudocódigo:**
Guardar: precio_original = 10

Mostrar: "El precio es 10€, si tienes 65 años o más son 7€"
Pedir: Edad del cliente
Guardar: edad

// Calculamos el precio según la edad
Si edad >= 65:
    Guardar: precio_final = precio_original - 3
Sino:
    Guardar: precio_final = precio_original

// Proceso de Pago
Mostrar: "El total es: ", precio_final, "€"
Mostrar: "¿Pagas en efectivo? (si/no)"
Pedir: respuesta_pago
Guardar: pago_efectivo

Si pago_efectivo == "si":
    Pedir: "¿Cuánto dinero me entregas?"
    Guardar: dinero_recibido
    
    Si dinero_recibido < precio_final:
        Mostrar: "Error: No es dinero suficiente."
    Sino:
        Calcular: cambio = dinero_recibido - precio_final
        Mostrar: "Aquí tienes tu cambio de: ", cambio, "€"
        Mostrar: "¡Disfruta tu película!"
Sino:
    Mostrar: "Por favor, acerca tu tarjeta al datáfono..."
    Mostrar: "Cobro exacto realizado. ¡Disfruta tu película!"