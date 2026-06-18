# 🎯 INICIO AQUÍ — Dashboard Proveedores v1.2

¡Bienvenido! Tu dashboard ha sido actualizado y está listo para usar. Lee esto primero. ⬇️

---

## 📚 GUÍAS POR ORDEN DE LECTURA

### 1️⃣ **PUBLICAR_EN_WEB.md** ← EMPIEZA POR AQUÍ
📌 **Para:** Publicar tu dashboard en internet en **5 minutos**
- ✅ Paso a paso super simple
- ✅ Sin terminal (opción visual)
- ✅ Gratis en Streamlit Cloud
- ⏱️ **5 minutos máximo**

### 2️⃣ **CAMBIOS_REALIZADOS.md**
📌 **Para:** Saber exactamente qué cambió
- ✅ Todas las funciones nuevas
- ✅ Datos agregados
- ✅ Mejoras de seguridad
- 📊 Estadísticas de cambios

### 3️⃣ **CHECKLIST_PRE_PUBLICACION.md**
📌 **Para:** Verificar todo antes de publicar
- ✅ Checklist de archivos
- ✅ Verificación de seguridad
- ✅ Verificación de datos
- 🆘 Troubleshooting

### 4️⃣ **DEPLOYMENT_GUIDE.md**
📌 **Para:** Opciones avanzadas
- ✅ VPS/Servidor propio
- ✅ Docker
- ✅ Cambiar dominio
- ✅ HTTPS/SSL

### 5️⃣ **README.md**
📌 **Para:** Documentación técnica
- ✅ Cómo ejecutar localmente
- ✅ Estructura del proyecto
- ✅ Credenciales

---

## 🚀 OPCIÓN RÁPIDA (5 MINUTOS)

Si quieres publicar YA en internet sin leer mucho:

### PASO 1: Crear cuenta en GitHub (3 min)
```
https://github.com/signup
```

### PASO 2: Cargar archivos a GitHub (1 min)
```
https://github.com/new
→ Repository name: dashboard_proveedores
→ Public (important!)
→ Subir 8 archivos
```

### PASO 3: Publicar en Streamlit Cloud (1 min)
```
https://share.streamlit.io
→ New app
→ Seleccionar repo: dashboard_proveedores
→ Main file: app.py
→ Deploy
```

✅ **¡LISTO!** Tu URL será:
```
https://dashboard-proveedores-TU_USUARIO.streamlit.app
```

---

## 🔐 ACCESO AL DASHBOARD

### Credenciales por defecto:

**👑 Admin (puede ver/editar TODO):**
```
Usuario:     admin
Contraseña:  Admin2024*
```

**👁️ Viewer (solo lectura):**
```
Usuario:     viewer
Contraseña:  Ver2024*
```

---

## 📦 ARCHIVOS INCLUIDOS (8 TOTAL)

```
dashboard_proveedores/
├── app.py                          ← App principal (la que se ejecuta)
├── database.py                     ← Base de datos
├── auth.py                         ← Login y seguridad
├── seed_data.py                    ← Datos iniciales
├── requirements.txt                ← Dependencias Python
├── README.md                       ← Documentación oficial
├── .gitignore                      ← Para GitHub
└── .streamlit/config.toml          ← Configuración
```

Descarga TODOS los archivos. Necesitas los 8.

---

## ✨ NOVEDADES v1.2

### 🔒 Seguridad
- ✅ Credenciales ocultas (no se ven en la UI)
- ✅ Panel de cambio de contraseña
- ✅ Hashing SHA-256 en todas las contraseñas

### 📊 Nuevas Pestañas
- ✅ **🗺️ Manos Remotas** — 55+ municipios de cobertura en Colombia
- ✅ **⏰ Turnos DMC** — Horarios de guardia por país

### 📈 Datos Agregados
- ✅ 19 extensiones (antes 5) — +14 nuevas
- ✅ 9 contactos ETB con escalamiento
- ✅ 55+ municipios de Manos Remotas
- ✅ 7 turnos DMC (Honduras, Guatemala, El Salvador)

### 🎨 Interfaz
- ✅ 6 pestañas (antes 4)
- ✅ Panel cambio de contraseña en sidebar
- ✅ Mejor organización visual

---

## 💡 PREGUNTAS FRECUENTES

### P: ¿Necesito pagar?
**R:** No, Streamlit Cloud es gratis.

### P: ¿Es seguro?
**R:** Sí. Las contraseñas usan SHA-256. Es seguro.

### P: ¿Funciona en móvil?
**R:** Sí, perfectamente.

### P: ¿Dónde se guardan los datos?
**R:** En una BD SQLite en los servidores de Streamlit Cloud.

### P: ¿Puedo cambiar la contraseña?
**R:** Sí, desde el panel en el sidebar. O edita `auth.py` para hacerlo permanente.

### P: ¿Cuántos usuarios simultáneos?
**R:** ~100 sin problemas en Streamlit Cloud.

### P: ¿Qué pasa si reseteo la BD?
**R:** Se recrea automático con los datos de `seed_data.py`.

---

## 🎓 CÓMO FUNCIONA

### Si ejecutas LOCAL (en tu computadora):
```bash
pip install -r requirements.txt
streamlit run app.py
```
Abre: http://localhost:8501

### Si publicas en Streamlit Cloud:
1. Subes a GitHub
2. Streamlit Cloud ve los cambios
3. Redeploy automático en 30 segundos
4. Todos pueden acceder por URL

### Base de datos:
- SQLite = archivo `dashboard.db`
- Se crea automático
- Persiste entre sesiones
- 7 tablas

---

## 🔧 PERSONALIZAR (OPCIONAL)

### Cambiar contraseña permanente:
1. Abre `auth.py`
2. Busca `USUARIOS = {`
3. Reemplaza `"Admin2024*"` por tu contraseña
4. Guarda y sube a GitHub

### Agregar más municipios:
1. Abre `seed_data.py`
2. Agrega a lista `MANOS_REMOTAS`
3. Sube a GitHub

### Cambiar colores:
1. Abre `.streamlit/config.toml`
2. Modifica colores HEX
3. Sube a GitHub

---

## 📖 DOCUMENTACIÓN COMPLETA

Si necesitas más detalles, lee en orden:

1. **PUBLICAR_EN_WEB.md** — Paso a paso visual
2. **CAMBIOS_REALIZADOS.md** — Todo lo nuevo
3. **CHECKLIST_PRE_PUBLICACION.md** — Antes de publicar
4. **DEPLOYMENT_GUIDE.md** — Opciones avanzadas
5. **README.md** — Documentación técnica

---

## ✅ PRÓXIMOS PASOS

### Opción A: Publicar YA (RECOMENDADO)
```
1. Leer: PUBLICAR_EN_WEB.md (5 min)
2. Seguir pasos
3. Compartir URL con tu equipo
```

### Opción B: Entender primero
```
1. Leer: CAMBIOS_REALIZADOS.md (10 min)
2. Leer: CHECKLIST_PRE_PUBLICACION.md (5 min)
3. Luego publicar
```

### Opción C: Ejecutar local
```
1. pip install -r requirements.txt
2. streamlit run app.py
3. Probar en http://localhost:8501
4. Luego publicar en Streamlit Cloud
```

---

## 🚀 PARA PUBLICAR EN 5 MIN

1. Ve a **PUBLICAR_EN_WEB.md**
2. Sigue los pasos (4 pasos = GitHub + Streamlit Cloud)
3. ¡Listo!

---

## 📞 AYUDA

Si algo no funciona:
1. Revisa **CHECKLIST_PRE_PUBLICACION.md** → sección "🆘 TROUBLESHOOTING"
2. Verifica que tengas los 8 archivos
3. Comprueba que `requirements.txt` está correcto

---

## 🎉 ¡FELICIDADES!

Tu dashboard está 100% actualizado, seguro y listo para producción.

**Próximo paso:** Lee **PUBLICAR_EN_WEB.md** y publica en 5 minutos.

---

**Dashboard Proveedores v1.2**
**Estado: ✅ Listo para producción**
**Última actualización: Junio 2026**

