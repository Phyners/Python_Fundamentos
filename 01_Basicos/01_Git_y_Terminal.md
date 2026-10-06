# ==========================================
# 00: GUÍA DE GIT Y GITHUB
# ==========================================

## 1. Conceptos Clave
*   **Git:** Tu máquina del tiempo local. Toma "fotografías" (commits) de tu código para que nunca pierdas el trabajo.
*   **GitHub:** La nube (como Google Drive de los programadores) donde guardas esas fotos para tener copias de seguridad o compartir con otros.
*   **Repositorio (Repo):** La carpeta de tu proyecto que Git está vigilando.
*   **Local vs. Remoto:** "Local" es tu PC. "Remoto" (Origin) es GitHub.

---

## 2. Configuración Inicial (Solo una vez por PC)
Es la "firma" que quedará registrada en cada punto de guardado que hagas.

*   `git config --global user.name "Tu Nombre"` -> Define tu nombre.
*   `git config --global user.email "tu@correo.com"` -> Usa el correo de tu cuenta de GitHub.

---

## 3. Empezar a trabajar (Dos caminos posibles)

**Camino A: Crear un proyecto nuevo desde cero y conectarlo a GitHub**
1.  `git init` -> Enciende la cámara en tu carpeta (crea el archivo oculto `.git`).
2.  `git branch -M main` -> Nombra la línea de tiempo principal como "main".
3.  `git remote add origin URL_DEL_REPO` -> Conecta tu PC con el repo vacío de GitHub.
4.  `git push -u origin main` -> Sube la primera foto y guarda el camino para el futuro.

**Camino B: Descargar un proyecto que ya existe en GitHub (Clonar)**
1.  `git clone URL_DEL_REPO` -> Descarga la carpeta completa con todo su historial. (No necesitas hacer `git init` ni conectar nada, ya viene listo para usar).

---

## 4. El Archivo Salvador: `.gitignore`
Antes de hacer tu primer guardado, DEBES crear un archivo llamado `.gitignore` (con el punto al principio). 
Ahí escribes el nombre de los archivos y carpetas que Git **debe ignorar y nunca subir a la nube** (como contraseñas, configuraciones personales o archivos pesados).

**Ejemplo de qué poner en un .gitignore de Python:**
*   `__pycache__/` (Carpetas que Python crea automáticamente)
*   `.env` (Archivo donde guardas contraseñas secretas)
*   `venv/` (El entorno virtual, ¡pesa muchísimo y no se sube!)

---

## 5. El Flujo de Trabajo Diario (Bucle Infinito)
Esto es lo que harás cada vez que te sientes a programar y termines una tarea.

1.  `git pull` -> **(OBLIGATORIO AL EMPEZAR)** Descarga cambios si trabajaste desde otro PC.
2.  `git status` -> Tu radar. Te dice qué archivos cambiaste y faltan por guardar.
3.  `git add .` -> Prepara TODOS los archivos modificados para la foto.
    *   *(Si solo quieres uno: `git add mi_archivo.py`)*
4.  `git commit -m "Mensaje explicando el cambio"` -> Toma la foto y la guarda en tu disco duro.
5.  `git push` -> Sube todas las fotos nuevas a GitHub.

---

## 6. Las Ramas (Branches): Magia para no romper nada
Las ramas sirven para experimentar o crear nuevas funciones sin tocar el código principal que ya funciona. Imagina realidades alternativas.

*   `git branch` -> Lista todas las ramas. La que tiene un `*` es donde estás ahora.
*   `git checkout -b "nueva_funcion"` -> Crea una nueva rama llamada "nueva_funcion" y te mueve a ella. *(En Git moderno también se usa `git switch -c "nueva_funcion"`)*.
*   `git checkout main` -> Te devuelve a la línea de tiempo principal.
*   `git merge "nueva_funcion"` -> (Estando en `main`): Absorbe y fusiona los cambios que hiciste en la rama alternativa.

---

## 7. Emergencias y Máquina del Tiempo (Viajes y Correcciones)
¿Rompiste algo? ¿Te arrepientes de un cambio? Git al rescate.

*   **Inspeccionar el pasado:**
    *   `git log` -> Muestra el historial completo de commits con su ID (código largo). Para salir, pulsa `q`.
    *   `git diff` -> Te muestra exactamente qué líneas de código borraste (en rojo) o añadiste (en verde) antes de guardarlas.
*   **Viajar en el tiempo (Modo Observador):**
    *   `git checkout <ID>` -> Viajas a un punto del pasado en específico (ej. `git checkout 3a4f8b2`). Tu código volverá a como estaba ese día.
    *   `git checkout main` -> Te regresa al presente una vez terminaste de mirar el pasado.
*   **Deshacer cagadas que AÚN NO has guardado (sin commit):**
    *   `git restore nombre_archivo.py` -> Borra los cambios de ese archivo y lo devuelve a como estaba en el último commit.
    *   `git restore .` -> Borra los cambios de TODOS los archivos. (Peligro: no hay vuelta atrás).
*   **El guardado de pánico (Stash):**
    *   `git stash` -> Tienes código a medias que no quieres guardar en un commit todavía, pero necesitas cambiar de rama. Esto "esconde" los cambios temporalmente.
    *   `git stash pop` -> Te devuelve los cambios que habías escondido.

---

## 8. Buenas Prácticas: Cómo escribir un buen Commit
Si pones "guardando", en tres meses no sabrás qué archivo modificaste. Escríbelo como si completaras la frase: *"Si aplico este commit, el código..."*

**Malos:**
❌ `git commit -m "actualizado"`
❌ `git commit -m "arreglando cosas"`

**Buenos:**
✅ `git commit -m "Añade botón de login en el menú principal"`
✅ `git commit -m "Arregla error de cálculo del IVA en el carrito"`
✅ `git commit -m "Ignora archivos del entorno virtual en el .gitignore"`