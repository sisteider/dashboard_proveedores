"""
auth.py
-------
Maneja la autenticación del usuario administrador.

¿Cómo funciona el login en Streamlit?
- Streamlit tiene un objeto especial llamado 'session_state'
- session_state es como una memoria temporal que dura mientras
  el usuario tiene la pestaña abierta
- Cuando cierra el navegador, session_state se borra
- Lo usamos para recordar si el admin ya inició sesión

¿Qué es un hash de contraseña?
- Nunca guardamos contraseñas en texto plano ("admin123")
- Las convertimos a un hash: una cadena irreversible
- hashlib.sha256("admin123") → "a665a45920422f9d417e4867efdc..."
- Si alguien ve el código, no puede saber la contraseña original
"""

import hashlib          # Módulo nativo de Python para encriptar
import streamlit as st  # Framework del dashboard


# ─────────────────────────────────────────────
# CONFIGURACIÓN DE CREDENCIALES
# ─────────────────────────────────────────────

# ⚠️  EN PRODUCCIÓN: mover estas credenciales a variables de entorno
#     o a un archivo .env — nunca dejarlas en el código fuente
#     Por ahora las dejamos aquí para simplicidad del ejemplo

USUARIOS = {
    "admin": {
        "password_hash": hashlib.sha256("Admin2024*".encode()).hexdigest(),
        "rol": "admin",
        "nombre": "Administrador"
    },
    "viewer": {
        "password_hash": hashlib.sha256("Ver2024*".encode()).hexdigest(),
        "rol": "viewer",
        "nombre": "Visitante"
    }
}

# Las credenciales por defecto son:
# Usuario: admin    Contraseña: Admin2024*
# Usuario: viewer   Contraseña: Ver2024*


# ─────────────────────────────────────────────
# FUNCIONES DE AUTENTICACIÓN
# ─────────────────────────────────────────────

def hash_password(password: str) -> str:
    """
    Convierte una contraseña en texto plano a un hash SHA-256.
    
    ¿Qué es SHA-256?
    - Es un algoritmo de hash criptográfico
    - Siempre produce una cadena de 64 caracteres
    - Es de una sola vía: no se puede revertir
    - La misma entrada siempre produce la misma salida
    
    Ejemplo:
        hash_password("hola") → "3338be694f..." (siempre igual)
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verificar_credenciales(username: str, password: str) -> dict | None:
    """
    Verifica si el usuario y contraseña son correctos.
    
    Retorna:
        dict con info del usuario si las credenciales son válidas
        None si son incorrectas
    
    ¿Por qué comparamos hashes y no contraseñas directas?
    - Comparamos hash(lo que escribió) == hash(guardado)
    - Nunca comparamos texto plano
    """
    usuario = USUARIOS.get(username.lower())  # .lower() → no distingue mayúsculas
    if not usuario:
        return None  # Usuario no existe

    if usuario["password_hash"] == hash_password(password):
        return {"username": username, "rol": usuario["rol"], "nombre": usuario["nombre"]}

    return None  # Contraseña incorrecta


def iniciar_sesion(username: str, password: str) -> bool:
    """
    Intenta iniciar sesión y guarda el resultado en session_state.
    
    ¿Qué es st.session_state?
    - Es un diccionario especial de Streamlit
    - Persiste entre re-ejecuciones del script
    - Cada usuario tiene su propio session_state
    - Se borra cuando cierran el navegador
    
    Retorna True si el login fue exitoso, False si no.
    """
    usuario = verificar_credenciales(username, password)
    if usuario:
        # Guardamos la info del usuario en session_state
        st.session_state["autenticado"] = True
        st.session_state["usuario"]     = usuario["username"]
        st.session_state["rol"]         = usuario["rol"]
        st.session_state["nombre"]      = usuario["nombre"]
        return True
    return False


def cerrar_sesion():
    """
    Cierra la sesión borrando los datos de session_state.
    """
    for key in ["autenticado", "usuario", "rol", "nombre"]:
        if key in st.session_state:
            del st.session_state[key]


def esta_autenticado() -> bool:
    """
    Verifica si hay una sesión activa.
    Retorna True si el usuario ya inició sesión.
    """
    return st.session_state.get("autenticado", False)


def es_admin() -> bool:
    """
    Verifica si el usuario actual es administrador.
    Los admins pueden agregar, editar y eliminar datos.
    """
    return st.session_state.get("rol") == "admin"


def get_nombre_usuario() -> str:
    """Retorna el nombre del usuario actual."""
    return st.session_state.get("nombre", "Visitante")


# ─────────────────────────────────────────────
# COMPONENTE VISUAL: Formulario de login
# ─────────────────────────────────────────────

def mostrar_login():
    """
    Renderiza el formulario de inicio de sesión.
    
    En Streamlit, las funciones que empiezan con st. dibujan
    elementos en pantalla. Por ejemplo:
    - st.text_input()  → caja de texto
    - st.button()      → botón
    - st.error()       → mensaje de error en rojo
    - st.success()     → mensaje de éxito en verde
    - st.columns()     → divide la pantalla en columnas
    """
    # Centramos el formulario usando columnas
    # La proporción [1, 2, 1] significa: espacio | formulario (doble ancho) | espacio
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  # Todo lo que está dentro de 'with col2' aparece en la columna del medio
        st.markdown("---")
        st.markdown("### 🔐 Iniciar Sesión")
        st.markdown("*Ingresa tus credenciales para acceder al panel de administración*")

        # st.text_input → caja de texto normal
        username = st.text_input(
            label       = "Usuario",
            placeholder = "Ej: admin",
            key         = "login_username"  # key → identificador único del widget
        )

        # type="password" → oculta los caracteres con ●●●●
        password = st.text_input(
            label       = "Contraseña",
            type        = "password",
            placeholder = "Tu contraseña",
            key         = "login_password"
        )

        # use_container_width=True → el botón ocupa todo el ancho disponible
        if st.button("Ingresar", use_container_width=True, type="primary"):
            if not username or not password:
                st.error("⚠️ Por favor ingresa usuario y contraseña")
            elif iniciar_sesion(username, password):
                st.success(f"✅ Bienvenido, {get_nombre_usuario()}!")
                # st.rerun() → vuelve a ejecutar el script desde arriba
                # Esto hace que la app "recargue" y muestre el dashboard
                st.rerun()
            else:
                st.error("❌ Usuario o contraseña incorrectos")

        st.markdown("---")


# ─────────────────────────────────────────────
# COMPONENTE: Botón de cerrar sesión
# ─────────────────────────────────────────────

def cambiar_contrasena(username: str, nueva_password: str) -> bool:
    """
    Cambia la contraseña de un usuario en memoria (USUARIOS dict).
    Retorna True si el usuario existe y se actualizó.
    """
    if username.lower() not in USUARIOS:
        return False
    USUARIOS[username.lower()]["password_hash"] = hash_password(nueva_password)
    return True


def mostrar_panel_cambio_clave():
    """
    Panel para que el admin cambie la contraseña de cualquier usuario,
    y cualquier usuario cambie la suya propia.
    Solo visible para el admin en el panel de configuración.
    """
    st.markdown("### 🔑 Cambiar Contraseña")

    usuario_actual = st.session_state.get("usuario", "")

    if es_admin():
        usuario_objetivo = st.selectbox(
            "Usuario a modificar",
            options=list(USUARIOS.keys()),
            index=list(USUARIOS.keys()).index(usuario_actual) if usuario_actual in USUARIOS else 0,
            key="cambio_clave_usuario"
        )
    else:
        usuario_objetivo = usuario_actual
        st.info(f"Cambiando contraseña de: **{usuario_actual}**")

    nueva = st.text_input("Nueva contraseña", type="password", key="nueva_clave_input")
    confirmar = st.text_input("Confirmar contraseña", type="password", key="confirmar_clave_input")

    if st.button("💾 Guardar nueva contraseña", type="primary", key="btn_guardar_clave"):
        if not nueva or not confirmar:
            st.error("⚠️ Completa ambos campos.")
        elif nueva != confirmar:
            st.error("❌ Las contraseñas no coinciden.")
        elif len(nueva) < 6:
            st.error("⚠️ La contraseña debe tener al menos 6 caracteres.")
        else:
            if cambiar_contrasena(usuario_objetivo, nueva):
                st.success(f"✅ Contraseña de **{usuario_objetivo}** actualizada correctamente.")
                st.info("💡 El cambio aplica para esta sesión. Para hacerlo permanente, actualiza el código fuente.")
            else:
                st.error("❌ Usuario no encontrado.")


def mostrar_boton_logout():
    """
    Muestra en el sidebar el nombre del usuario y un botón para salir.
    """
    with st.sidebar:
        st.markdown("---")
        rol_emoji = "👑" if es_admin() else "👁️"
        st.markdown(f"**{rol_emoji} {get_nombre_usuario()}**")
        st.caption(f"Rol: {'Administrador' if es_admin() else 'Solo lectura'}")

        if st.button("🚪 Cerrar sesión", use_container_width=True):
            cerrar_sesion()
            st.rerun()
