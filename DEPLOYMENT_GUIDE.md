# 🚀 Guía de Publicación en Internet

## 📋 Resumen de Cambios Realizados

✅ **Seguridad:**
- ✓ Credenciales OCULTAS (ya no se muestran en la UI)
- ✓ Panel para cambiar contraseñas (solo admin)
- ✓ Hashing SHA-256 en todas las contraseñas

✅ **Nuevas Pestañas:**
- ✓ **Manos Remotas** (🗺️) — Cobertura geográfica de Colombia con proveedores
- ✓ **Turnos DMC** (⏰) — On-Call por país para Liberty Networks

✅ **Datos Completados:**
- ✓ 19 extensiones (todas las que faltaban)
- ✓ 9 contactos de ETB con matriz de escalamiento
- ✓ 55+ municipios de cobertura en Manos Remotas
- ✓ Turnos DMC para Honduras, Guatemala, El Salvador

---

## 🌐 OPCIÓN 1: Streamlit Cloud (RECOMENDADO - GRATIS)

### ✅ Pasos:

#### 1️⃣ Crear cuenta en GitHub (si no tienes)
```
https://github.com/signup
```
- Email + contraseña
- Confirmar email
- Listo

#### 2️⃣ Subir archivos a GitHub
```bash
# En tu computadora, crea una carpeta:
mkdir dashboard_proveedores
cd dashboard_proveedores

# Copiar los archivos descargados aquí:
# - app.py
# - database.py
# - auth.py
# - seed_data.py
# - requirements.txt
# - README.md
```

#### 3️⃣ Crear repositorio en GitHub
- Ve a https://github.com/new
- Nombre: `dashboard_proveedores`
- Descripción: "Dashboard de gestión de proveedores"
- Selecciona "Public" (para que Streamlit Cloud pueda verlo)
- Clic en "Create repository"

#### 4️⃣ Subir archivos a GitHub
```bash
cd dashboard_proveedores

# Inicializar git
git init
git add .
git commit -m "Dashboard proveedores v1.2"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/dashboard_proveedores.git
git push -u origin main
```

Reemplaza `TU_USUARIO` con tu usuario de GitHub.

#### 5️⃣ Publicar en Streamlit Cloud
- Ve a https://share.streamlit.io
- Haz clic en "New app"
- Conecta tu cuenta de GitHub
- Selecciona:
  - **Repository:** `TU_USUARIO/dashboard_proveedores`
  - **Branch:** `main`
  - **Main file path:** `app.py`
- Clic en "Deploy"

⏳ **Espera 2-3 minutos...**

✅ **¡Tu dashboard estará en línea!**

URL: `https://dashboard-proveedores.streamlit.app`

---

## 🖥️ OPCIÓN 2: VPS/Servidor (Self-Hosted)

Si prefieres control total y no confiar en Streamlit Cloud.

### Requisitos:
- VPS/Servidor Linux (DigitalOcean, Linode, AWS, etc.)
- Acceso SSH

### Pasos:

#### 1️⃣ Conectar al servidor
```bash
ssh root@TU_IP_SERVIDOR
```

#### 2️⃣ Instalar Python y dependencias
```bash
apt update && apt upgrade -y
apt install python3 python3-pip -y
pip install --upgrade pip
```

#### 3️⃣ Clonar/subir el proyecto
```bash
cd /home
git clone https://github.com/TU_USUARIO/dashboard_proveedores.git
cd dashboard_proveedores
pip install -r requirements.txt
```

#### 4️⃣ Ejecutar en background
```bash
# Opción A: Con nohup (simple)
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &

# Opción B: Con PM2 (recomendado)
npm install -g pm2
pm2 start "streamlit run app.py --server.port 8501 --server.address 0.0.0.0" --name "dashboard"
pm2 save
```

#### 5️⃣ Configurar dominio (opcional)
Si quieres un dominio como `dashboard.tuempresa.com`:

```bash
# Instalar Nginx
apt install nginx -y

# Crear config
nano /etc/nginx/sites-available/dashboard
```

Pega esto:
```nginx
server {
    listen 80;
    server_name dashboard.tuempresa.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
ln -s /etc/nginx/sites-available/dashboard /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

#### 6️⃣ SSL (HTTPS) con Let's Encrypt
```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d dashboard.tuempresa.com
```

---

## 🐳 OPCIÓN 3: Docker (Avanzado)

Crea un archivo `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

Construir y ejecutar:
```bash
docker build -t dashboard-proveedores .
docker run -p 8501:8501 dashboard-proveedores
```

---

## 🔐 CAMBIAR CREDENCIALES

### Credenciales actuales:
```
Usuario: admin
Contraseña: Admin2024*

Usuario: viewer
Contraseña: Ver2024*
```

### Para cambiarlas PERMANENTEMENTE:

#### Opción 1: Desde el dashboard (temporal)
1. Inicia sesión como admin
2. Ve al sidebar → "Cambiar contraseña"
3. Cambia las claves
4. **Nota:** Solo se mantiene para esa sesión (se reinician al reiniciar)

#### Opción 2: En el código (permanente)
Edita `auth.py`:

```python
USUARIOS = {
    "admin": {
        "password_hash": hashlib.sha256("TU_NUEVA_CONTRASEÑA".encode()).hexdigest(),
        "rol": "admin",
        "nombre": "Administrador"
    },
    "viewer": {
        "password_hash": hashlib.sha256("OTRA_CONTRASEÑA".encode()).hexdigest(),
        "rol": "viewer",
        "nombre": "Visitante"
    }
}
```

Luego:
```bash
git add auth.py
git commit -m "Actualizar credenciales"
git push
```

Streamlit Cloud se actualizará automáticamente.

---

## 📊 Resumen de Features

| Feature | Estado | Acceso |
|---------|--------|--------|
| Gestión de Proveedores | ✅ | Admin |
| Gestión de Contactos | ✅ | Admin |
| Áreas/Países | ✅ | Admin |
| Equipo RMP | ✅ | Admin |
| Extensiones | ✅ | Admin (ver: todos) |
| Manos Remotas (55+ municipios) | ✅ | Admin (ver: todos) |
| Turnos DMC | ✅ | Admin (ver: todos) |
| Cambio de contraseña | ✅ | Admin |
| Login seguro (SHA-256) | ✅ | Todos |
| Base de datos SQLite | ✅ | Local |

---

## 🆘 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### Error: "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### BD corrupta
```bash
rm dashboard.db
# Recarga la página — se recrea automáticamente
```

### Cambios no se ven en Streamlit Cloud
```bash
git add .
git commit -m "Actualización"
git push origin main
# Espera 30-60 segundos a que Streamlit redeploy
```

---

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs: `streamlit run app.py` en la terminal
2. Comprueba que `requirements.txt` esté actualizado
3. Asegúrate de que `app.py`, `database.py`, `auth.py`, `seed_data.py` estén todos juntos

---

**¡Listo! Tu dashboard está 100% funcional y listo para publicar.** 🎉
