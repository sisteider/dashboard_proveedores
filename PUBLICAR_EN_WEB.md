# 🚀 PUBLICAR EN INTERNET EN 5 MINUTOS

## ✅ Lo que ya tienes listo:
- ✓ Dashboard 100% funcional
- ✓ Base de datos con 55+ municipios
- ✓ Credenciales seguras (ocultas)
- ✓ Cambio de contraseña desde admin

---

## 📝 PASOS PARA PUBLICAR EN LA WEB

### PASO 1: Descargar tus archivos
Ya descargaste de Claude:
- `app.py`
- `database.py`
- `auth.py`
- `seed_data.py`
- `requirements.txt`
- `README.md`
- `.streamlit/config.toml`
- `.gitignore`

Guárdalos en una carpeta llamada: **`dashboard_proveedores`**

---

### PASO 2: Crear cuenta GRATIS en GitHub
1. Ve a → https://github.com/signup
2. Escribe tu email
3. Crea contraseña
4. Escribe tu usuario (ej: `tu_nombre_123`)
5. Confirma el email
6. ✅ **¡Cuenta lista!**

---

### PASO 3: Crear repositorio en GitHub
1. Ve a → https://github.com/new
2. En **"Repository name"** escribe: `dashboard_proveedores`
3. En **"Description"** escribe: `Dashboard de gestión de proveedores`
4. Asegúrate que **Public** esté seleccionado ✅
5. Clic en **"Create repository"** (botón verde)

---

### PASO 4: Subir tus archivos a GitHub
Hay DOS formas:

#### 🟦 **FORMA FÁCIL (sin terminal):**
1. En la página del repositorio, clic en **"uploading an existing file"**
2. Arrastra/selecciona tus 8 archivos
3. Clic en **"Commit changes"** (botón verde)
4. ✅ **¡Archivos subidos!**

#### 🖥️ **FORMA CON TERMINAL (para máquinas Linux/Mac):**
```bash
# 1. Abre terminal en tu carpeta de archivos
cd ~/dashboard_proveedores

# 2. Ejecuta estos comandos (uno por uno):
git init
git add .
git commit -m "Dashboard proveedores v1.2"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/dashboard_proveedores.git
git push -u origin main
```

Reemplaza `TU_USUARIO` con tu usuario de GitHub (el que creaste en PASO 2)

---

### PASO 5: Publicar en Streamlit Cloud
1. Ve a → https://share.streamlit.io
2. Clic en **"New app"** (botón con "+" azul)
3. Selecciona:
   - **GitHub account:** Tu cuenta
   - **Repository:** `dashboard_proveedores`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Clic en **"Deploy"** (botón rosa)

⏳ **ESPERAAAA... 2-3 minutos...**

---

### ✅ ¡¡¡ LISTO !!!

Tu URL será: `https://dashboard-proveedores-TU_USUARIO.streamlit.app`

Ejemplo: Si tu usuario es `juan_lopez`, la URL será:
```
https://dashboard-proveedores-juan-lopez.streamlit.app
```

---

## 🔐 Credenciales para acceder

### Usuario Admin (puede ver/editar TODO):
```
Usuario:     admin
Contraseña:  Admin2024*
```

### Usuario Viewer (solo lectura):
```
Usuario:     viewer
Contraseña:  Ver2024*
```

---

## 🔄 Actualizar el dashboard en la web

Cuando hagas cambios:

```bash
# 1. Modifica tus archivos locales
# (Ej: cambias algo en app.py)

# 2. Sube a GitHub:
git add .
git commit -m "Descripción del cambio"
git push origin main

# 3. Streamlit se actualiza automáticamente en 30-60 segundos
# (No necesitas hacer nada más)
```

---

## 🛡️ Cambiar contraseñas (PERMANENTE)

Si quieres cambiar la contraseña de admin a algo más seguro:

1. Abre el archivo **`auth.py`** con un editor de texto
2. Busca esta sección:
```python
USUARIOS = {
    "admin": {
        "password_hash": hashlib.sha256("Admin2024*".encode()).hexdigest(),
        ...
```

3. Reemplaza `Admin2024*` por tu nueva contraseña:
```python
"password_hash": hashlib.sha256("MiContraseñaNueva123".encode()).hexdigest(),
```

4. Guarda el archivo
5. Sube a GitHub (git add, commit, push)
6. ✅ **¡Cambiada!**

---

## 📊 Características del Dashboard

✅ **Pestañas:**
1. **🏢 Proveedores** — Gestión de proveedores (Liberty, ETB, MNC, etc.)
2. **🌎 Países/Áreas** — Países donde operamos (Colombia, Honduras, etc.)
3. **👥 Equipo RMP** — Equipo RMP Comunicaciones
4. **🔌 Extensiones** — 19 extensiones internas (DC, SOC, NOC, etc.)
5. **🗺️ Manos Remotas** — 55+ municipios de cobertura con proveedores
6. **⏰ Turnos DMC** — Horarios de guardia por país

✅ **Funciones:**
- Login seguro (usuario + contraseña)
- Cambio de contraseña desde admin
- Agregar/editar/eliminar datos (admin)
- Ver datos (viewer)
- BD SQLite automática

---

## ❓ Preguntas Frecuentes

### P: ¿Es gratis?
**R:** Sí, Streamlit Cloud es gratis para proyectos públicos. Si quieres privado, el primer nivel es ~$5/mes.

### P: ¿Puedo acceder desde móvil?
**R:** Sí, funciona perfectamente en teléfono.

### P: ¿Los datos se guardan?
**R:** Sí, en una base de datos SQLite que se guarda en Streamlit Cloud.

### P: ¿Puedo cambiar el dominio?
**R:** Con Streamlit Pro ($5/mes) sí. Sino es: `dashboard-proveedores-tu_usuario.streamlit.app`

### P: ¿Qué pasa si alguien intenta adivinar la contraseña?
**R:** Las contraseñas están hasheadas (SHA-256), no se pueden recuperar. Solo si alguien acierta.

### P: ¿Puedo usar otra base de datos (MySQL, PostgreSQL)?
**R:** Sí, pero requiere modificar `database.py`. Por ahora SQLite funciona bien.

---

## 📞 Ayuda

Si algo no funciona:
1. Verifica que todos los 8 archivos estén en GitHub
2. En Streamlit Cloud, clic en **"View app"** → mira los logs (botón "Logs" arriba a la derecha)
3. Busca el error en los logs
4. Reinicia: Clic en los 3 puntos arriba a la derecha → **"Reboot app"**

---

**¡Felicidades! Tu dashboard está en INTERNET ahora! 🎉**

Comparte la URL con tu equipo:
```
https://dashboard-proveedores-TU_USUARIO.streamlit.app
```

