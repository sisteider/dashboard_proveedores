"""
database.py
-----------
Este archivo maneja TODA la comunicación con la base de datos SQLite.

¿Qué es SQLite?
- Es una base de datos que vive en un solo archivo (.db)
- No necesitas instalar nada extra, Python la trae incluida
- El módulo que usamos se llama 'sqlite3' (ya viene con Python)

¿Qué es una función CRUD?
- CREATE  → Insertar datos nuevos
- READ    → Leer / consultar datos
- UPDATE  → Modificar datos existentes
- DELETE  → Eliminar datos

Este archivo tiene funciones CRUD para cada tabla.
"""

import sqlite3  # Módulo nativo de Python, no hay que instalarlo
import os

# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────

# __file__ es la ruta de este archivo (database.py)
# os.path.dirname() saca la carpeta donde vive
# Así el archivo .db siempre queda junto al proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "dashboard.db")


# ─────────────────────────────────────────────
# CONEXIÓN
# ─────────────────────────────────────────────

def get_connection():
    """
    Crea y retorna una conexión a la base de datos.
    
    - check_same_thread=False es necesario para Streamlit
      porque Streamlit puede llamar funciones desde varios hilos.
    - row_factory=sqlite3.Row hace que los resultados se puedan
      usar como diccionarios: fila['nombre'] en vez de fila[0]
    """
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Acceso por nombre de columna
    return conn


# ─────────────────────────────────────────────
# CREAR TABLAS (se ejecuta una sola vez al inicio)
# ─────────────────────────────────────────────

def crear_tablas():
    """
    Crea las tablas si no existen.
    'IF NOT EXISTS' evita errores si ya están creadas.
    
    Relaciones:
    - proveedores → tiene muchos contactos (1 a muchos)
    - contactos.proveedor_id → apunta a proveedores.id
    """
    conn = get_connection()
    cursor = conn.cursor()  # El cursor es como el "lápiz" que escribe en la BD

    # ── Tabla 1: Proveedores ──────────────────
    # Cada proveedor es una empresa externa (UFINET, CLARO, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proveedores (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT    NOT NULL,
            categoria   TEXT,
            portal_url  TEXT,
            usuario     TEXT,
            contrasena  TEXT,
            telefono    TEXT,
            email       TEXT,
            notas       TEXT,
            activo      INTEGER DEFAULT 1
        )
    """)
    # INTEGER PRIMARY KEY AUTOINCREMENT → el ID se asigna solo (1, 2, 3...)
    # NOT NULL → ese campo es obligatorio
    # DEFAULT 1 → activo=1 significa que sí está activo

    # ── Tabla 2: Contactos ───────────────────
    # Cada proveedor puede tener varios contactos (L1, L2, L3...)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            proveedor_id    INTEGER,
            nombre          TEXT,
            cargo           TEXT,
            telefono        TEXT,
            email           TEXT,
            nivel           TEXT,
            horario         TEXT,
            FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)
        )
    """)
    # FOREIGN KEY → esta columna apunta a otra tabla
    # Así sabemos a qué proveedor pertenece cada contacto

    # ── Tabla 3: Áreas / Países ──────────────
    # Son los equipos internos por región (Colombia, Honduras, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS areas (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT    NOT NULL,
            correo      TEXT,
            extension   TEXT,
            jefe        TEXT,
            jefe_tel    TEXT,
            oncall_l3   TEXT,
            oncall_tel  TEXT,
            notas       TEXT
        )
    """)

    # ── Tabla 4: Extensiones internas ────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS extensiones (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            numero      TEXT,
            servicio    TEXT,
            descripcion TEXT
        )
    """)

    # ── Tabla 5: Escalamiento RMP ─────────────
    # El equipo de RMP Comunicaciones (escalamiento interno)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipo_rmp (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT,
            cargo       TEXT,
            celular     TEXT,
            email       TEXT,
            notas       TEXT
        )
    """)

    # ── Tabla 6: Manos Remotas ───────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS manos_remotas (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            municipio       TEXT,
            departamento    TEXT,
            tipo_lugar      TEXT,
            proveedor_ppal  TEXT,
            proveedor_bk    TEXT,
            contacto_email  TEXT,
            contacto_tel    TEXT,
            contacto_esc    TEXT
        )
    """)

    # ── Tabla 7: Turnos DMC ──────────────────
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turnos_dmc (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            pais        TEXT,
            dia_semana  TEXT,
            horario_ini TEXT,
            horario_fin TEXT,
            telefono    TEXT,
            ingeniero   TEXT,
            notas       TEXT
        )
    """)

    conn.commit()   # commit() guarda los cambios permanentemente
    conn.close()    # Siempre cerrar la conexión al terminar
    print(f"✅ Base de datos lista en: {DB_PATH}")


# ─────────────────────────────────────────────
# CRUD — PROVEEDORES
# ─────────────────────────────────────────────

def get_proveedores():
    """Retorna todos los proveedores activos como lista de diccionarios."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proveedores WHERE activo=1 ORDER BY nombre")
    # fetchall() trae TODOS los resultados
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados


def get_proveedor_por_id(proveedor_id):
    """Retorna un solo proveedor por su ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proveedores WHERE id=?", (proveedor_id,))
    # El '?' es un placeholder — evita inyección SQL (buena práctica de seguridad)
    # fetchone() trae solo el primer resultado
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def agregar_proveedor(nombre, categoria, portal_url, usuario,
                      contrasena, telefono, email, notas):
    """Inserta un nuevo proveedor en la base de datos."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO proveedores 
            (nombre, categoria, portal_url, usuario, contrasena, telefono, email, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nombre, categoria, portal_url, usuario, contrasena, telefono, email, notas))
    # lastrowid → el ID que se le asignó al registro recién creado
    nuevo_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return nuevo_id


def editar_proveedor(proveedor_id, nombre, categoria, portal_url,
                     usuario, contrasena, telefono, email, notas):
    """Actualiza los datos de un proveedor existente."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE proveedores
        SET nombre=?, categoria=?, portal_url=?, usuario=?,
            contrasena=?, telefono=?, email=?, notas=?
        WHERE id=?
    """, (nombre, categoria, portal_url, usuario, contrasena, telefono, email, notas, proveedor_id))
    conn.commit()
    conn.close()


def eliminar_proveedor(proveedor_id):
    """
    'Elimina' un proveedor poniéndolo inactivo (activo=0).
    Esto se llama 'soft delete' — los datos no se borran realmente,
    solo se ocultan. Buena práctica para no perder información.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE proveedores SET activo=0 WHERE id=?", (proveedor_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# CRUD — CONTACTOS
# ─────────────────────────────────────────────

def get_contactos_por_proveedor(proveedor_id):
    """Trae todos los contactos de un proveedor específico."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM contactos 
        WHERE proveedor_id=? 
        ORDER BY nivel
    """, (proveedor_id,))
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados


def agregar_contacto(proveedor_id, nombre, cargo, telefono, email, nivel, horario):
    """Agrega un contacto vinculado a un proveedor."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contactos 
            (proveedor_id, nombre, cargo, telefono, email, nivel, horario)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (proveedor_id, nombre, cargo, telefono, email, nivel, horario))
    conn.commit()
    conn.close()


def editar_contacto(contacto_id, nombre, cargo, telefono, email, nivel, horario):
    """Edita un contacto existente."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE contactos
        SET nombre=?, cargo=?, telefono=?, email=?, nivel=?, horario=?
        WHERE id=?
    """, (nombre, cargo, telefono, email, nivel, horario, contacto_id))
    conn.commit()
    conn.close()


def eliminar_contacto(contacto_id):
    """Elimina un contacto permanentemente."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE id=?", (contacto_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# CRUD — ÁREAS / PAÍSES
# ─────────────────────────────────────────────

def get_areas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM areas ORDER BY nombre")
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados


def agregar_area(nombre, correo, extension, jefe, jefe_tel, oncall_l3, oncall_tel, notas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO areas 
            (nombre, correo, extension, jefe, jefe_tel, oncall_l3, oncall_tel, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nombre, correo, extension, jefe, jefe_tel, oncall_l3, oncall_tel, notas))
    conn.commit()
    conn.close()


def editar_area(area_id, nombre, correo, extension, jefe, jefe_tel, oncall_l3, oncall_tel, notas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE areas
        SET nombre=?, correo=?, extension=?, jefe=?, jefe_tel=?,
            oncall_l3=?, oncall_tel=?, notas=?
        WHERE id=?
    """, (nombre, correo, extension, jefe, jefe_tel, oncall_l3, oncall_tel, notas, area_id))
    conn.commit()
    conn.close()


def eliminar_area(area_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM areas WHERE id=?", (area_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# CRUD — EQUIPO RMP
# ─────────────────────────────────────────────

def get_equipo_rmp():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipo_rmp ORDER BY nombre")
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados


def agregar_miembro_rmp(nombre, cargo, celular, email, notas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO equipo_rmp (nombre, cargo, celular, email, notas)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, cargo, celular, email, notas))
    conn.commit()
    conn.close()


def editar_miembro_rmp(miembro_id, nombre, cargo, celular, email, notas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE equipo_rmp
        SET nombre=?, cargo=?, celular=?, email=?, notas=?
        WHERE id=?
    """, (nombre, cargo, celular, email, notas, miembro_id))
    conn.commit()
    conn.close()


def eliminar_miembro_rmp(miembro_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM equipo_rmp WHERE id=?", (miembro_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# CRUD — EXTENSIONES
# ─────────────────────────────────────────────

def get_extensiones():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM extensiones ORDER BY numero")
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados


def agregar_extension(numero, servicio, descripcion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO extensiones (numero, servicio, descripcion)
        VALUES (?, ?, ?)
    """, (numero, servicio, descripcion))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# CRUD — MANOS REMOTAS
# ─────────────────────────────────────────────

def get_manos_remotas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM manos_remotas ORDER BY departamento, municipio")
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados

def agregar_mano_remota(municipio, departamento, tipo_lugar, proveedor_ppal, proveedor_bk, contacto_email, contacto_tel, contacto_esc):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO manos_remotas (municipio, departamento, tipo_lugar, proveedor_ppal, proveedor_bk, contacto_email, contacto_tel, contacto_esc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (municipio, departamento, tipo_lugar, proveedor_ppal, proveedor_bk, contacto_email, contacto_tel, contacto_esc))
    conn.commit()
    conn.close()

def editar_mano_remota(mr_id, municipio, departamento, tipo_lugar, proveedor_ppal, proveedor_bk, contacto_email, contacto_tel, contacto_esc):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE manos_remotas SET municipio=?, departamento=?, tipo_lugar=?, proveedor_ppal=?, proveedor_bk=?, contacto_email=?, contacto_tel=?, contacto_esc=?
        WHERE id=?
    """, (municipio, departamento, tipo_lugar, proveedor_ppal, proveedor_bk, contacto_email, contacto_tel, contacto_esc, mr_id))
    conn.commit()
    conn.close()

def eliminar_mano_remota(mr_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM manos_remotas WHERE id=?", (mr_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# CRUD — TURNOS DMC
# ─────────────────────────────────────────────

def get_turnos_dmc():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turnos_dmc ORDER BY pais, dia_semana")
    resultados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return resultados

def agregar_turno_dmc(pais, dia_semana, horario_ini, horario_fin, telefono, ingeniero, notas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO turnos_dmc (pais, dia_semana, horario_ini, horario_fin, telefono, ingeniero, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (pais, dia_semana, horario_ini, horario_fin, telefono, ingeniero, notas))
    conn.commit()
    conn.close()

def eliminar_turno_dmc(turno_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM turnos_dmc WHERE id=?", (turno_id,))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# UTILIDAD — verificar si la BD ya tiene datos
# ─────────────────────────────────────────────

def bd_tiene_datos():
    """
    Retorna True si ya hay proveedores en la BD.
    Sirve para no cargar los datos iniciales dos veces.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM proveedores")
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA (para probar este archivo solo)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Esto solo se ejecuta si corres: python database.py
    # No se ejecuta cuando otros archivos importan este módulo
    crear_tablas()
    print("Tablas creadas correctamente.")
