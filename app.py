"""
app.py
------
Archivo principal del dashboard. Es el punto de entrada de la aplicación.

Para ejecutarlo:
    streamlit run app.py

¿Cómo funciona Streamlit al ejecutarse?
1. Python ejecuta este archivo de arriba a abajo
2. Cada st.algo() dibuja un elemento en el navegador
3. Cuando el usuario interactúa (clic, escribir), Streamlit
   vuelve a ejecutar TODO el archivo desde arriba
4. session_state conserva los datos entre ejecuciones

Flujo de la app:
    Inicio → ¿Hay datos en BD? → No → cargar seed_data
                                → Sí → mostrar dashboard
           → ¿Está autenticado? → No → mostrar login en sidebar
                                 → Sí → mostrar botón logout
"""

import streamlit as st
import pandas as pd
import database as db
import auth
import sys, os

# Agregamos la carpeta 'data' al path para importar seed_data
sys.path.append(os.path.join(os.path.dirname(__file__), "data"))
import seed_data


# ─────────────────────────────────────────────
# CONFIGURACIÓN GENERAL DE LA APP
# ─────────────────────────────────────────────
# Esta función DEBE ser la primera llamada a Streamlit en el archivo

st.set_page_config(
    page_title     = "Dashboard Proveedores",   # Título en la pestaña del navegador
    page_icon      = "📡",                       # Emoji como ícono
    layout         = "wide",                    # Usa todo el ancho de la pantalla
    initial_sidebar_state = "expanded"          # Sidebar abierto por defecto
)


# ─────────────────────────────────────────────
# ESTILOS CSS PERSONALIZADOS
# ─────────────────────────────────────────────
# st.markdown con unsafe_allow_html=True permite inyectar HTML/CSS

st.markdown("""
<style>
    /* Tarjetas de métricas */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card h2 { margin: 0; font-size: 2.5rem; }
    .metric-card p  { margin: 0; font-size: 0.9rem; opacity: 0.85; }

    /* Tarjetas de proveedor */
    .proveedor-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 0.8rem;
        background: #fafafa;
    }
    .proveedor-card h4 { margin: 0 0 0.3rem 0; color: #1a1a2e; }

    /* Badge de categoría */
    .badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        background: #e8f4fd;
        color: #1565c0;
        margin-bottom: 0.5rem;
    }

    /* Tabla personalizada */
    .custom-table { width: 100%; border-collapse: collapse; }
    .custom-table th {
        background: #1a1a2e;
        color: white;
        padding: 8px 12px;
        text-align: left;
    }
    .custom-table td {
        padding: 8px 12px;
        border-bottom: 1px solid #eee;
    }
    .custom-table tr:hover td { background: #f5f5f5; }

    /* Ocultar el menú de Streamlit (más limpio para demo) */
    #MainMenu  { visibility: hidden; }
    footer     { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# INICIALIZACIÓN
# ─────────────────────────────────────────────

def inicializar():
    """
    Se ejecuta una vez al arrancar la app.
    1. Crea las tablas si no existen
    2. Carga los datos iniciales si la BD está vacía
    
    ¿Qué es @st.cache_resource?
    - Es un decorador (la línea que empieza con @)
    - Le dice a Streamlit que ejecute esta función UNA SOLA VEZ
    - Aunque el script se re-ejecute 100 veces, esto solo corre una
    - Ideal para conexiones a BD e inicializaciones costosas
    """
    db.crear_tablas()
    if not db.bd_tiene_datos():
        seed_data.cargar_datos_iniciales()

inicializar()


# ─────────────────────────────────────────────
# SIDEBAR — Panel lateral
# ─────────────────────────────────────────────

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/network.png", width=60)
    st.title("📡 Dashboard\nProveedores")
    st.markdown("---")

    # Sección de login/logout en el sidebar
    if not auth.esta_autenticado():
        st.markdown("### 🔐 Acceso Admin")
        username = st.text_input("Usuario", key="sb_user")
        password = st.text_input("Contraseña", type="password", key="sb_pass")
        if st.button("Ingresar", use_container_width=True, type="primary"):
            if auth.iniciar_sesion(username, password):
                st.success(f"✅ Bienvenido!")
                st.rerun()
            else:
                st.error("❌ Credenciales incorrectas")
        st.markdown("---")
    else:
        rol_emoji = "👑" if auth.es_admin() else "👁️"
        st.success(f"{rol_emoji} **{auth.get_nombre_usuario()}**")
        st.caption(f"Rol: {'Administrador' if auth.es_admin() else 'Solo lectura'}")
        if st.button("🚪 Cerrar sesión", use_container_width=True):
            auth.cerrar_sesion()
            st.rerun()
        st.markdown("---")
        with st.expander("🔑 Cambiar contraseña"):
            auth.mostrar_panel_cambio_clave()

    st.markdown("---")
    st.caption("v1.2 — Dashboard Proveedores")


# ─────────────────────────────────────────────
# ENCABEZADO PRINCIPAL
# ─────────────────────────────────────────────

st.title("📡 Dashboard de Proveedores y Escalamiento")
st.markdown("Directorio centralizado de proveedores, contactos y escalamiento por región.")
st.markdown("---")


# ─────────────────────────────────────────────
# MÉTRICAS RESUMEN (fila superior)
# ─────────────────────────────────────────────
# st.columns(4) divide la pantalla en 4 columnas iguales

proveedores_data = db.get_proveedores()
areas_data       = db.get_areas()
equipo_data      = db.get_equipo_rmp()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🏢 Proveedores",   len(proveedores_data))
with col2:
    st.metric("🌎 Áreas / Países", len(areas_data))
with col3:
    st.metric("👥 Equipo RMP",    len(equipo_data))
with col4:
    # Contamos todos los contactos sumando los de cada proveedor
    total_contactos = sum(
        len(db.get_contactos_por_proveedor(p["id"])) for p in proveedores_data
    )
    st.metric("📋 Contactos",     total_contactos)

st.markdown("---")


# ─────────────────────────────────────────────
# PESTAÑAS PRINCIPALES
# ─────────────────────────────────────────────
# st.tabs() crea pestañas navegables — retorna una lista de contextos

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏢 Proveedores",
    "🌎 Países / Áreas",
    "👥 Equipo RMP",
    "🔌 Extensiones",
    "🗺️ Manos Remotas",
    "⏰ Turnos DMC"
])


# ══════════════════════════════════════════════
# TAB 1 — PROVEEDORES
# ══════════════════════════════════════════════

with tab1:
    st.subheader("🏢 Directorio de Proveedores")

    # ── Buscador y filtros ────────────────────
    col_buscar, col_filtro = st.columns([3, 1])
    with col_buscar:
        busqueda = st.text_input("🔍 Buscar proveedor...", placeholder="Ej: UFINET, CLARO...")
    with col_filtro:
        categorias = ["Todas"] + sorted(set(p["categoria"] for p in proveedores_data if p["categoria"]))
        categoria_filtro = st.selectbox("Categoría", categorias)

    # Aplicamos los filtros
    # List comprehension: [elemento for elemento in lista if condición]
    proveedores_filtrados = [
        p for p in proveedores_data
        if (busqueda.lower() in p["nombre"].lower() or not busqueda)
        and (categoria_filtro == "Todas" or p["categoria"] == categoria_filtro)
    ]

    st.caption(f"Mostrando {len(proveedores_filtrados)} de {len(proveedores_data)} proveedores")
    st.markdown("---")

    # ── Botón agregar (solo admin) ────────────
    if auth.es_admin():
        if st.button("➕ Agregar Proveedor", type="primary"):
            st.session_state["mostrar_form_proveedor"] = True

        # Formulario de nuevo proveedor
        if st.session_state.get("mostrar_form_proveedor"):
            with st.expander("📝 Nuevo Proveedor", expanded=True):
                with st.form("form_nuevo_proveedor"):
                    st.markdown("#### Datos del proveedor")
                    fc1, fc2 = st.columns(2)
                    with fc1:
                        np_nombre    = st.text_input("Nombre *", placeholder="Ej: NUEVA EMPRESA S.A.")
                        np_categoria = st.text_input("Categoría", placeholder="Ej: Conectividad")
                        np_telefono  = st.text_input("Teléfono(s)")
                        np_email     = st.text_input("Email(s)")
                    with fc2:
                        np_portal    = st.text_input("URL del Portal")
                        np_usuario   = st.text_input("Usuario del portal")
                        np_password  = st.text_input("Contraseña del portal", type="password")
                        np_notas     = st.text_area("Notas adicionales", height=80)

                    col_guardar, col_cancelar = st.columns(2)
                    with col_guardar:
                        guardar = st.form_submit_button("💾 Guardar", use_container_width=True, type="primary")
                    with col_cancelar:
                        cancelar = st.form_submit_button("❌ Cancelar", use_container_width=True)

                    if guardar:
                        if not np_nombre:
                            st.error("El nombre es obligatorio")
                        else:
                            db.agregar_proveedor(np_nombre, np_categoria, np_portal,
                                                 np_usuario, np_password, np_telefono,
                                                 np_email, np_notas)
                            st.success(f"✅ Proveedor '{np_nombre}' agregado!")
                            st.session_state["mostrar_form_proveedor"] = False
                            st.rerun()
                    if cancelar:
                        st.session_state["mostrar_form_proveedor"] = False
                        st.rerun()

    # ── Lista de proveedores ──────────────────
    for p in proveedores_filtrados:
        contactos = db.get_contactos_por_proveedor(p["id"])

        # st.expander → sección colapsable/expandible
        with st.expander(f"**{p['nombre']}** — {p['categoria']}", expanded=False):

            col_info, col_acciones = st.columns([4, 1])

            with col_info:
                # Datos del proveedor en columnas
                d1, d2, d3 = st.columns(3)
                with d1:
                    if p["portal_url"]:
                        st.markdown(f"🌐 **Portal:** [{p['portal_url'][:40]}...]({p['portal_url']})" 
                                    if len(p["portal_url"]) > 40 
                                    else f"🌐 **Portal:** [{p['portal_url']}]({p['portal_url']})")
                    if p["usuario"]:
                        st.markdown(f"👤 **Usuario:** `{p['usuario']}`")
                    if p["contrasena"] and auth.es_admin():
                        st.markdown(f"🔑 **Contraseña:** `{p['contrasena']}`")
                    elif p["contrasena"]:
                        st.markdown("🔑 **Contraseña:** `••••••••` *(solo admin)*")
                with d2:
                    if p["telefono"]:
                        st.markdown(f"📞 **Teléfono:** {p['telefono']}")
                    if p["email"]:
                        st.markdown(f"📧 **Email:** {p['email']}")
                with d3:
                    if p["notas"]:
                        st.info(f"📝 {p['notas']}")

                # Tabla de contactos/escalamiento
                if contactos:
                    st.markdown(f"##### 📋 Escalamiento ({len(contactos)} contactos)")
                    df_contactos = pd.DataFrame(contactos)[
                        ["nivel", "nombre", "cargo", "telefono", "email", "horario"]
                    ]
                    df_contactos.columns = ["Nivel", "Nombre", "Cargo", "Teléfono", "Email", "Horario"]
                    # hide_index=True → oculta la columna de índice numérico
                    st.dataframe(df_contactos, use_container_width=True, hide_index=True)

            # ── Acciones admin ────────────────
            with col_acciones:
                if auth.es_admin():
                    st.markdown("**Acciones**")

                    # Botón editar proveedor
                    if st.button("✏️ Editar", key=f"edit_{p['id']}", use_container_width=True):
                        st.session_state[f"editando_{p['id']}"] = True

                    # Botón eliminar (con confirmación)
                    if st.button("🗑️ Eliminar", key=f"del_{p['id']}", use_container_width=True):
                        st.session_state[f"confirmar_del_{p['id']}"] = True

                    # Confirmación de eliminar
                    if st.session_state.get(f"confirmar_del_{p['id']}"):
                        st.warning("¿Seguro?")
                        if st.button("Sí, eliminar", key=f"confirm_{p['id']}", type="primary"):
                            db.eliminar_proveedor(p["id"])
                            st.success("Eliminado")
                            st.rerun()
                        if st.button("No, cancelar", key=f"cancel_del_{p['id']}"):
                            st.session_state[f"confirmar_del_{p['id']}"] = False
                            st.rerun()

                    # Botón agregar contacto
                    st.markdown("---")
                    if st.button("➕ Contacto", key=f"add_c_{p['id']}", use_container_width=True):
                        st.session_state[f"add_contacto_{p['id']}"] = True

            # Formulario editar proveedor
            if auth.es_admin() and st.session_state.get(f"editando_{p['id']}"):
                st.markdown("---")
                st.markdown("#### ✏️ Editar Proveedor")
                with st.form(f"form_edit_{p['id']}"):
                    ec1, ec2 = st.columns(2)
                    with ec1:
                        e_nombre   = st.text_input("Nombre",    value=p["nombre"])
                        e_cat      = st.text_input("Categoría", value=p["categoria"] or "")
                        e_tel      = st.text_input("Teléfono",  value=p["telefono"] or "")
                        e_email    = st.text_input("Email",     value=p["email"] or "")
                    with ec2:
                        e_portal   = st.text_input("Portal URL",  value=p["portal_url"] or "")
                        e_usuario  = st.text_input("Usuario",     value=p["usuario"] or "")
                        e_pass     = st.text_input("Contraseña",  value=p["contrasena"] or "", type="password")
                        e_notas    = st.text_area("Notas",        value=p["notas"] or "", height=80)

                    s1, s2 = st.columns(2)
                    with s1:
                        if st.form_submit_button("💾 Guardar cambios", use_container_width=True, type="primary"):
                            db.editar_proveedor(p["id"], e_nombre, e_cat, e_portal,
                                                e_usuario, e_pass, e_tel, e_email, e_notas)
                            st.success("✅ Actualizado")
                            st.session_state[f"editando_{p['id']}"] = False
                            st.rerun()
                    with s2:
                        if st.form_submit_button("❌ Cancelar", use_container_width=True):
                            st.session_state[f"editando_{p['id']}"] = False
                            st.rerun()

            # Formulario agregar contacto
            if auth.es_admin() and st.session_state.get(f"add_contacto_{p['id']}"):
                st.markdown("---")
                st.markdown("#### ➕ Agregar Contacto")
                with st.form(f"form_contacto_{p['id']}"):
                    cc1, cc2 = st.columns(2)
                    with cc1:
                        c_nombre  = st.text_input("Nombre *")
                        c_cargo   = st.text_input("Cargo")
                        c_nivel   = st.text_input("Nivel", placeholder="Ej: Nivel 1, L1, 1er Nivel")
                    with cc2:
                        c_tel     = st.text_input("Teléfono")
                        c_email   = st.text_input("Email")
                        c_horario = st.text_input("Horario", placeholder="Ej: 7x24, 2h, 80 min")

                    s1, s2 = st.columns(2)
                    with s1:
                        if st.form_submit_button("💾 Guardar contacto", use_container_width=True, type="primary"):
                            if not c_nombre:
                                st.error("El nombre es obligatorio")
                            else:
                                db.agregar_contacto(p["id"], c_nombre, c_cargo,
                                                    c_tel, c_email, c_nivel, c_horario)
                                st.success(f"✅ Contacto '{c_nombre}' agregado!")
                                st.session_state[f"add_contacto_{p['id']}"] = False
                                st.rerun()
                    with s2:
                        if st.form_submit_button("❌ Cancelar", use_container_width=True):
                            st.session_state[f"add_contacto_{p['id']}"] = False
                            st.rerun()


# ══════════════════════════════════════════════
# TAB 2 — PAÍSES / ÁREAS
# ══════════════════════════════════════════════

with tab2:
    st.subheader("🌎 Países y Áreas de Cobertura")

    if auth.es_admin():
        if st.button("➕ Agregar Área / País", type="primary", key="btn_add_area"):
            st.session_state["mostrar_form_area"] = True

        if st.session_state.get("mostrar_form_area"):
            with st.expander("📝 Nueva Área", expanded=True):
                with st.form("form_nueva_area"):
                    fa1, fa2 = st.columns(2)
                    with fa1:
                        na_nombre   = st.text_input("Nombre del área *", placeholder="Ej: Ecuador")
                        na_correo   = st.text_input("Correo")
                        na_ext      = st.text_input("Extensión")
                        na_notas    = st.text_area("Notas", height=70)
                    with fa2:
                        na_jefe     = st.text_input("Jefe / Responsable")
                        na_jefe_tel = st.text_input("Teléfono Jefe")
                        na_oncall   = st.text_input("OnCall L3")
                        na_oncall_t = st.text_input("Teléfono OnCall")

                    s1, s2 = st.columns(2)
                    with s1:
                        if st.form_submit_button("💾 Guardar", use_container_width=True, type="primary"):
                            if not na_nombre:
                                st.error("El nombre es obligatorio")
                            else:
                                db.agregar_area(na_nombre, na_correo, na_ext, na_jefe,
                                                na_jefe_tel, na_oncall, na_oncall_t, na_notas)
                                st.success(f"✅ Área '{na_nombre}' agregada!")
                                st.session_state["mostrar_form_area"] = False
                                st.rerun()
                    with s2:
                        if st.form_submit_button("❌ Cancelar", use_container_width=True):
                            st.session_state["mostrar_form_area"] = False
                            st.rerun()

    # Tabla de áreas
    if areas_data:
        df_areas = pd.DataFrame(areas_data)
        df_areas = df_areas.rename(columns={
            "nombre": "Área / País", "correo": "Correo",
            "extension": "Ext.", "jefe": "Jefe",
            "jefe_tel": "Tel. Jefe", "oncall_l3": "OnCall L3",
            "oncall_tel": "Tel. OnCall", "notas": "Notas"
        })
        # Quitamos columnas técnicas que no necesita ver el usuario
        cols_mostrar = ["Área / País", "Correo", "Ext.", "Jefe", "Tel. Jefe", "OnCall L3", "Tel. OnCall", "Notas"]
        st.dataframe(df_areas[cols_mostrar], use_container_width=True, hide_index=True)
    else:
        st.info("No hay áreas registradas.")

    # Edición individual de áreas (admin)
    if auth.es_admin() and areas_data:
        st.markdown("---")
        st.markdown("#### ✏️ Editar un área")
        area_nombres = {a["nombre"]: a["id"] for a in areas_data}
        area_sel = st.selectbox("Selecciona el área a editar", list(area_nombres.keys()))
        area_id  = area_nombres[area_sel]
        area_obj = next(a for a in areas_data if a["id"] == area_id)

        with st.form("form_edit_area"):
            ea1, ea2 = st.columns(2)
            with ea1:
                ea_nombre   = st.text_input("Nombre",     value=area_obj["nombre"])
                ea_correo   = st.text_input("Correo",     value=area_obj["correo"] or "")
                ea_ext      = st.text_input("Extensión",  value=area_obj["extension"] or "")
                ea_notas    = st.text_area("Notas",       value=area_obj["notas"] or "", height=70)
            with ea2:
                ea_jefe     = st.text_input("Jefe",       value=area_obj["jefe"] or "")
                ea_jefe_tel = st.text_input("Tel. Jefe",  value=area_obj["jefe_tel"] or "")
                ea_oncall   = st.text_input("OnCall L3",  value=area_obj["oncall_l3"] or "")
                ea_oncall_t = st.text_input("Tel. OnCall",value=area_obj["oncall_tel"] or "")

            s1, s2 = st.columns(2)
            with s1:
                if st.form_submit_button("💾 Guardar cambios", use_container_width=True, type="primary"):
                    db.editar_area(area_id, ea_nombre, ea_correo, ea_ext, ea_jefe,
                                   ea_jefe_tel, ea_oncall, ea_oncall_t, ea_notas)
                    st.success("✅ Área actualizada")
                    st.rerun()
            with s2:
                if st.form_submit_button("🗑️ Eliminar área", use_container_width=True):
                    db.eliminar_area(area_id)
                    st.success("Eliminada")
                    st.rerun()


# ══════════════════════════════════════════════
# TAB 3 — EQUIPO RMP
# ══════════════════════════════════════════════

with tab3:
    st.subheader("👥 Equipo RMP — Escalamiento Interno")
    st.caption("Directorio del equipo de RMP Comunicaciones para escalamiento interno")

    if auth.es_admin():
        if st.button("➕ Agregar Miembro", type="primary", key="btn_add_rmp"):
            st.session_state["mostrar_form_rmp"] = True

        if st.session_state.get("mostrar_form_rmp"):
            with st.expander("📝 Nuevo Miembro", expanded=True):
                with st.form("form_nuevo_rmp"):
                    fr1, fr2 = st.columns(2)
                    with fr1:
                        nr_nombre  = st.text_input("Nombre *")
                        nr_cargo   = st.text_input("Cargo")
                    with fr2:
                        nr_cel     = st.text_input("Celular")
                        nr_email   = st.text_input("Email")
                    nr_notas   = st.text_area("Notas", height=60)

                    s1, s2 = st.columns(2)
                    with s1:
                        if st.form_submit_button("💾 Guardar", use_container_width=True, type="primary"):
                            if not nr_nombre:
                                st.error("El nombre es obligatorio")
                            else:
                                db.agregar_miembro_rmp(nr_nombre, nr_cargo, nr_cel, nr_email, nr_notas)
                                st.success(f"✅ '{nr_nombre}' agregado!")
                                st.session_state["mostrar_form_rmp"] = False
                                st.rerun()
                    with s2:
                        if st.form_submit_button("❌ Cancelar", use_container_width=True):
                            st.session_state["mostrar_form_rmp"] = False
                            st.rerun()

    # Tarjetas del equipo
    equipo_data = db.get_equipo_rmp()
    if equipo_data:
        # Mostramos en grilla de 3 columnas
        # zip(*[iter(lista)]*n) → agrupa en grupos de n
        cols = st.columns(3)
        for i, miembro in enumerate(equipo_data):
            with cols[i % 3]:  # i % 3 → alterna entre columna 0, 1 y 2
                with st.container():
                    st.markdown(f"""
                    <div class='proveedor-card'>
                        <h4>👤 {miembro['nombre']}</h4>
                        <span class='badge'>{miembro['cargo'] or 'Sin cargo'}</span><br>
                        {'📞 ' + miembro['celular'] + '<br>' if miembro['celular'] else ''}
                        {'📧 ' + miembro['email'] + '<br>' if miembro['email'] else ''}
                        {'📝 ' + miembro['notas'] if miembro['notas'] else ''}
                    </div>
                    """, unsafe_allow_html=True)

                    if auth.es_admin():
                        col_e, col_d = st.columns(2)
                        with col_e:
                            if st.button("✏️", key=f"edit_rmp_{miembro['id']}", help="Editar"):
                                st.session_state[f"edit_rmp_{miembro['id']}"] = True
                        with col_d:
                            if st.button("🗑️", key=f"del_rmp_{miembro['id']}", help="Eliminar"):
                                db.eliminar_miembro_rmp(miembro["id"])
                                st.rerun()

                        if st.session_state.get(f"edit_rmp_{miembro['id']}"):
                            with st.form(f"form_edit_rmp_{miembro['id']}"):
                                em_nombre = st.text_input("Nombre", value=miembro["nombre"])
                                em_cargo  = st.text_input("Cargo",  value=miembro["cargo"] or "")
                                em_cel    = st.text_input("Celular",value=miembro["celular"] or "")
                                em_email  = st.text_input("Email",  value=miembro["email"] or "")
                                em_notas  = st.text_area("Notas",   value=miembro["notas"] or "", height=60)
                                s1, s2 = st.columns(2)
                                with s1:
                                    if st.form_submit_button("💾", use_container_width=True, type="primary"):
                                        db.editar_miembro_rmp(miembro["id"], em_nombre, em_cargo,
                                                              em_cel, em_email, em_notas)
                                        st.session_state[f"edit_rmp_{miembro['id']}"] = False
                                        st.rerun()
                                with s2:
                                    if st.form_submit_button("❌", use_container_width=True):
                                        st.session_state[f"edit_rmp_{miembro['id']}"] = False
                                        st.rerun()
    else:
        st.info("No hay miembros registrados en el equipo RMP.")


# ══════════════════════════════════════════════
# TAB 4 — EXTENSIONES
# ══════════════════════════════════════════════

with tab4:
    st.subheader("🔌 Extensiones Internas")

    extensiones_data = db.get_extensiones()

    if auth.es_admin():
        with st.expander("➕ Agregar Extensión"):
            with st.form("form_nueva_ext"):
                ex1, ex2, ex3 = st.columns(3)
                with ex1:
                    ne_num = st.text_input("Número de extensión *")
                with ex2:
                    ne_srv = st.text_input("Servicio", placeholder="Ej: NOC, DC, SOC")
                with ex3:
                    ne_desc = st.text_input("Descripción")

                if st.form_submit_button("💾 Agregar", type="primary"):
                    if not ne_num:
                        st.error("El número es obligatorio")
                    else:
                        db.agregar_extension(ne_num, ne_srv, ne_desc)
                        st.success(f"✅ Extensión {ne_num} agregada!")
                        st.rerun()

    if extensiones_data:
        df_ext = pd.DataFrame(extensiones_data)[["numero", "servicio", "descripcion"]]
        df_ext.columns = ["Número", "Servicio", "Descripción"]
        st.dataframe(df_ext, use_container_width=True, hide_index=True)
    else:
        st.info("No hay extensiones registradas.")


# ══════════════════════════════════════════════
# TAB 5 — MANOS REMOTAS / COBERTURA GEOGRÁFICA
# ══════════════════════════════════════════════

with tab5:
    st.subheader("🗺️ Manos Remotas — Cobertura Colombia")
    st.markdown("*Cobertura geográfica por municipio, departamento y proveedores asociados*")

    manos_data = db.get_manos_remotas()

    if auth.es_admin():
        with st.expander("➕ Agregar Mano Remota"):
            with st.form("form_nueva_mr"):
                mr1, mr2, mr3 = st.columns(3)
                with mr1:
                    mr_mun = st.text_input("Municipio *")
                with mr2:
                    mr_dep = st.text_input("Departamento *")
                with mr3:
                    mr_tipo = st.selectbox("Tipo de Lugar", ["Tipo 1", "Tipo 2", "Tipo 3"])

                mr4, mr5 = st.columns(2)
                with mr4:
                    mr_ppal = st.text_input("Proveedor Principal")
                with mr5:
                    mr_bk = st.text_input("Proveedor Backup")

                mr_email = st.text_input("Email de contacto")
                mr_tel = st.text_input("Teléfono")
                mr_esc = st.text_area("Contacto escalamiento", height=60)

                if st.form_submit_button("💾 Agregar", type="primary"):
                    if not mr_mun or not mr_dep or not mr_ppal:
                        st.error("⚠️ Municipio, Departamento y Proveedor Principal son obligatorios")
                    else:
                        db.agregar_mano_remota(mr_mun, mr_dep, mr_tipo, mr_ppal, mr_bk, mr_email, mr_tel, mr_esc)
                        st.success(f"✅ Mano Remota {mr_mun} agregada!")
                        st.rerun()

    if manos_data:
        # Agrupar por departamento
        departamentos = sorted(set(m["departamento"] for m in manos_data))
        
        for dept in departamentos:
            with st.expander(f"📍 {dept}", expanded=(dept == "Cundinamarca")):
                manos_dept = [m for m in manos_data if m["departamento"] == dept]
                
                for mano in manos_dept:
                    col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
                    with col1:
                        st.markdown(f"**{mano['municipio']}**")
                        st.caption(f"Tipo: {mano['tipo_lugar']}")
                    with col2:
                        st.markdown(f"**Ppal:** {mano['proveedor_ppal']}")
                        st.caption(f"BK: {mano['proveedor_bk']}")
                    with col3:
                        if mano['contacto_email']:
                            st.markdown(f"📧 {mano['contacto_email']}")
                        if mano['contacto_tel']:
                            st.markdown(f"📞 {mano['contacto_tel']}")
                        if mano['contacto_esc']:
                            st.caption(f"🚨 Esc: {mano['contacto_esc'][:40]}...")
                    with col4:
                        if auth.es_admin():
                            if st.button("🗑️", key=f"del_mr_{mano['id']}"):
                                db.eliminar_mano_remota(mano['id'])
                                st.rerun()
    else:
        st.info("No hay cobertura de manos remotas registrada.")


# ══════════════════════════════════════════════
# TAB 6 — TURNOS DMC (LIBERTY NETWORKS)
# ══════════════════════════════════════════════

with tab6:
    st.subheader("⏰ Turnos DMC — On-Call por País")
    st.markdown("*Horarios de guardia y contactos de ingeniero para DMC (Liberty Networks)*")

    turnos_data = db.get_turnos_dmc()

    if auth.es_admin():
        with st.expander("➕ Agregar Turno DMC"):
            with st.form("form_nuevo_turno"):
                t1, t2, t3 = st.columns(3)
                with t1:
                    t_pais = st.selectbox("País", ["Honduras", "Guatemala", "El Salvador", "Otro"])
                with t2:
                    t_dia = st.text_input("Día/Período (Ej: Lunes a Viernes)")
                with t3:
                    t_ini = st.text_input("Horario Inicio (Ej: 07:00 pm)")

                t4, t5, t6 = st.columns(3)
                with t4:
                    t_fin = st.text_input("Horario Fin (Ej: 07:00 am)")
                with t5:
                    t_tel = st.text_input("Teléfono de contacto")
                with t6:
                    t_ing = st.text_input("Ingeniero asignado")

                t_notas = st.text_area("Notas adicionales", height=60)

                if st.form_submit_button("💾 Agregar", type="primary"):
                    if not t_pais or not t_dia:
                        st.error("⚠️ País y Día/Período son obligatorios")
                    else:
                        db.agregar_turno_dmc(t_pais, t_dia, t_ini, t_fin, t_tel, t_ing, t_notas)
                        st.success(f"✅ Turno para {t_pais} agregado!")
                        st.rerun()

    if turnos_data:
        # Agrupar por país
        paises = sorted(set(t["pais"] for t in turnos_data))
        
        for pais in paises:
            with st.expander(f"🌐 {pais}", expanded=(pais == "Honduras")):
                turnos_pais = [t for t in turnos_data if t["pais"] == pais]
                
                for turno in turnos_pais:
                    st.markdown("---")
                    col1, col2, col3 = st.columns([1.5, 2, 1.5])
                    
                    with col1:
                        st.markdown(f"**{turno['dia_semana']}**")
                    with col2:
                        horario = f"{turno['horario_ini']} - {turno['horario_fin']}" if turno['horario_fin'] else turno['horario_ini']
                        st.markdown(f"🕐 {horario}")
                    with col3:
                        if turno['telefono']:
                            st.markdown(f"📞 {turno['telefono']}")
                    
                    if turno['ingeniero'] or turno['notas']:
                        st.caption(f"👨‍💼 {turno['ingeniero']} | {turno['notas']}" if turno['ingeniero'] and turno['notas'] 
                                  else f"👨‍💼 {turno['ingeniero']}" if turno['ingeniero'] 
                                  else f"📝 {turno['notas']}")
                    
                    if auth.es_admin():
                        if st.button("🗑️", key=f"del_turno_{turno['id']}"):
                            db.eliminar_turno_dmc(turno['id'])
                            st.rerun()
    else:
        st.info("No hay turnos DMC registrados.")
