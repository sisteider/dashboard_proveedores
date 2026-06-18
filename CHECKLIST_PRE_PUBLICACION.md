# ✅ CHECKLIST PRE-PUBLICACIÓN

Antes de publicar tu dashboard en internet, verifica que todo esté correcto.

---

## 📦 ARCHIVOS NECESARIOS

Asegúrate de tener TODOS estos archivos en tu carpeta `dashboard_proveedores/`:

- [ ] `app.py` (37 KB)
- [ ] `database.py` (19 KB)
- [ ] `auth.py` (10 KB)
- [ ] `seed_data.py` (47 KB)
- [ ] `requirements.txt` (336 B)
- [ ] `README.md` (1.3 KB)
- [ ] `.gitignore` (para GitHub)
- [ ] `.streamlit/config.toml` (configuración)

**Total: 8 archivos**

---

## 🔐 SEGURIDAD

- [ ] Las credenciales NO aparecen en el expander del login
- [ ] El archivo `auth.py` contiene las contraseñas hasheadas
- [ ] El panel "Cambiar contraseña" aparece en el sidebar
- [ ] Solo admin puede cambiar contraseña de otros usuarios
- [ ] Las contraseñas usan SHA-256 (seguro)

---

## 📊 DATOS CARGADOS

### Extensiones
- [ ] Mínimo 19 extensiones cargadas
- [ ] Incluyen: DC, NETWORKING, SOC, CSIRT, etc.

### ETB - Contactos
- [ ] 9 contactos con escalamiento
- [ ] Incluyen niveles: Día 0-1, Día 3, Día 5, Día 6, Día 7, Día 9, Día 13

### Manos Remotas
- [ ] Mínimo 55 municipios cargados
- [ ] Incluyen: Cundinamarca, Córdoba, Valle, Antioquia, Santander, Atlántico, etc.
- [ ] Cada uno con: Tipo de lugar, proveedores, emails, teléfonos

### Turnos DMC
- [ ] Turnos para: Honduras, Guatemala, El Salvador
- [ ] Incluyen: Horarios, teléfonos, notas

---

## 🎨 INTERFAZ

- [ ] Aparecen 6 pestañas: Proveedores, Países, RMP, Extensiones, Manos Remotas, Turnos
- [ ] Cada pestaña carga datos sin errores
- [ ] El sidebar muestra: Usuario, Rol, Botón logout, Panel cambio contraseña
- [ ] Los botones (Agregar, Editar, Eliminar) funcionan para admin
- [ ] Los formularios validan campos requeridos

---

## 🗄️ BASE DE DATOS

- [ ] El archivo `dashboard.db` existe localmente (si lo ejecutaste)
- [ ] No hay errores de SQL al cargar datos
- [ ] Se pueden agregar nuevos registros sin errores
- [ ] Se pueden editar registros sin errores
- [ ] Se pueden eliminar registros sin errores

---

## 📝 CAMBIOS EDITADOS (SI APLICA)

Si cambiaste algo, verifica:

### Si editaste `auth.py`:
- [ ] Las contraseñas nuevas usan SHA-256
- [ ] La sintaxis está correcta (sin errores de paréntesis)
- [ ] Los nombres de usuario son únicos

### Si editaste `seed_data.py`:
- [ ] Agregar datos nuevos no causa errores SQL
- [ ] Los datos se cargan correctamente en la UI

### Si editaste `app.py`:
- [ ] No hay código duplicado
- [ ] Las pestañas se muestran correctamente
- [ ] Los imports están al inicio del archivo

---

## 🌐 ANTES DE PUBLICAR EN GITHUB

### GitHub
- [ ] Cuentas creada en GitHub (https://github.com/signup)
- [ ] Email confirmado
- [ ] Repositorio `dashboard_proveedores` creado
- [ ] Repositorio está en **"Public"** (importante para Streamlit Cloud)
- [ ] Todos los 8 archivos subidos

### Git (si usas terminal)
- [ ] `git init` ejecutado
- [ ] `git remote add origin` con tu URL
- [ ] `git branch -M main` ejecutado
- [ ] Primer `git push` fue exitoso

---

## 🚀 ANTES DE PUBLICAR EN STREAMLIT CLOUD

- [ ] Cuenta Streamlit Cloud creada (https://share.streamlit.io)
- [ ] Conectada con tu cuenta de GitHub
- [ ] Repositorio visible en Streamlit Cloud
- [ ] Seleccionaste: Branch = `main`, Main file = `app.py`
- [ ] Hiciste clic en "Deploy"

---

## ✅ DESPUÉS DE PUBLICAR EN STREAMLIT CLOUD

- [ ] La app se está compilando (ves un spinner/loading)
- [ ] No hay errores en los logs (revisa abajo a la derecha)
- [ ] La URL está lista: `https://dashboard-proveedores-TU_USUARIO.streamlit.app`
- [ ] Puedes acceder con user: `admin` y contraseña: `Admin2024*`
- [ ] Las 6 pestañas cargan correctamente
- [ ] Puedes ver los datos cargados

---

## 🔍 VERIFICACIÓN DE FUNCIONES

### Login
- [ ] Puedo iniciar sesión como admin
- [ ] Puedo iniciar sesión como viewer
- [ ] Credenciales incorrectas muestran error
- [ ] Después de logout, el dashboard pide login

### Panel Admin (con user: admin)
- [ ] Puedo ver "Agregar proveedor" expandible
- [ ] Puedo ver "Agregar contacto" expandible
- [ ] Puedo agregar un proveedor sin errores
- [ ] Puedo editar un proveedor existente
- [ ] Puedo eliminar un proveedor
- [ ] Veo el panel "Cambiar contraseña" en el sidebar
- [ ] Puedo cambiar mi contraseña

### Panel Viewer (con user: viewer)
- [ ] NO veo botones "Agregar"
- [ ] NO veo botones "Eliminar"
- [ ] SÍ puedo ver todos los datos en lectura
- [ ] SÍ puedo cambiar mi propia contraseña
- [ ] NO puedo cambiar contraseña de otros usuarios

### Manos Remotas
- [ ] Carga 55+ municipios sin errores
- [ ] Se agrupa por departamento
- [ ] Puedo ver proveedores, emails, teléfonos
- [ ] Admin puede agregar/eliminar

### Turnos DMC
- [ ] Carga turnos para Honduras, Guatemala, El Salvador
- [ ] Se agrupa por país
- [ ] Puedo ver horarios, teléfonos, notas
- [ ] Admin puede agregar/eliminar

---

## 📋 DATOS ESPERADOS

Al cargar tu dashboard, deberías ver:

| Sección | Cantidad Esperada |
|---------|-------------------|
| Proveedores | 3+ (Liberty, ETB, MNC, etc.) |
| Contactos por proveedor | 2-9 según proveedor |
| Extensiones | 19+ |
| Áreas/Países | 2+ |
| Equipo RMP | 4+ |
| Municipios Manos Remotas | 55+ |
| Turnos DMC | 7 |

Si ves menos, revisa `seed_data.py` que todos los datos estén ahí.

---

## 🆘 TROUBLESHOOTING

Si algo no funciona:

### Error: "ModuleNotFoundError: No module named 'streamlit'"
✅ **Solución:** En Streamlit Cloud, usa `requirements.txt`
```
Verifica que requirements.txt tenga:
streamlit==1.35.0
pandas==2.2.2
```

### Error: "database.db not found"
✅ **Solución:** Automático. Se crea al primer acceso.
- Solo espera un poco en Streamlit Cloud (1-2 minutos)

### Error: "Port 8501 already in use"
✅ **Solución:** Solo si ejecutas LOCAL
```bash
streamlit run app.py --server.port 8502
```

### No puedo iniciar sesión
✅ **Solución:** Verifica:
- Usuario correcto: `admin` o `viewer` (minúsculas)
- Contraseña correcta: `Admin2024*` o `Ver2024*`
- No hay espacios antes/después

### Los datos no se cargan
✅ **Solución:**
1. Cierra Streamlit Cloud (clic en "Manage app" → "Reboot")
2. Espera a que reinicie
3. Recarga la página (F5)

### Los cambios que hice no aparecen
✅ **Solución:**
```bash
git add .
git commit -m "Mis cambios"
git push origin main
# Espera 30-60 segundos a que Streamlit redeploy
```

---

## 📞 PREGUNTAS ANTES DE PUBLICAR

**P: ¿Qué pasa si reseteo la BD?**
A: Simplement elimina `dashboard.db`, se recrea con los datos de `seed_data.py`

**P: ¿Puedo compartir la URL con otros?**
A: Sí, cualquiera puede acceder con las credenciales (admin/Admin2024* o viewer/Ver2024*)

**P: ¿Es seguro que todos conozcan la contraseña?**
A: No es lo ideal. Considera cambiarla en `auth.py` y hacer push a GitHub.

**P: ¿Se pierden los datos si Streamlit Cloud reinicia?**
A: No, SQLite persiste los datos en el servidor.

**P: ¿Cuántos usuarios simultáneos soporta?**
A: Streamlit Cloud gratis soporta ~100 usuarios activos sin problemas.

---

## ✨ FINAL

Si todo está en ✅, ¡**Tu dashboard está listo para producción!**

Comparte con tu equipo:
```
https://dashboard-proveedores-TU_USUARIO.streamlit.app

Credenciales:
- Admin: admin / Admin2024*
- Viewer: viewer / Ver2024*
```

---

**Última verificación:** Hoy
**Estado:** ✅ LISTO PARA PUBLICAR
