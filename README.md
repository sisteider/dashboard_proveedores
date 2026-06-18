# 📡 Dashboard de Proveedores

Dashboard centralizado para gestión de proveedores, contactos y escalamiento.

## 🚀 Cómo ejecutar localmente

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la app
```bash
streamlit run app.py
```

### 3. Abrir en el navegador
La app abre automáticamente en: http://localhost:8501

---

## 👥 Credenciales

| Usuario  | Contraseña  | Rol           |
|----------|-------------|---------------|
| admin    | Admin2024*  | Administrador |
| viewer   | Ver2024*    | Solo lectura  |

---

## 📁 Estructura del proyecto

```
dashboard_proveedores/
├── app.py          → App principal (ejecutar este)
├── database.py     → Base de datos SQLite
├── auth.py         → Sistema de login
├── data/
│   └── seed_data.py → Datos iniciales
├── dashboard.db    → BD (se crea automático)
└── requirements.txt
```

---

## ☁️ Subir a Streamlit Cloud (gratis)

1. Sube el proyecto a GitHub
2. Entra a https://share.streamlit.io
3. Conecta tu repositorio
4. En "Main file path" pon: `app.py`
5. Clic en Deploy — ¡listo!

---

## 🖥️ Subir a VPS con Docker

```bash
# En el servidor:
pip install -r requirements.txt
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```
