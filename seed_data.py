"""
seed_data.py
------------
Este archivo contiene TODOS los datos iniciales extraídos del CSV
y de las imágenes del SharePoint.

¿Qué es 'seed data'?
- En programación, 'seed' (semilla) es la carga inicial de datos
- Es como plantar la semilla antes de que el árbol crezca
- Se ejecuta UNA SOLA VEZ cuando la app arranca por primera vez
- Después, los admins pueden agregar/editar desde la interfaz

Estructura de los datos:
- Usamos diccionarios Python → { "clave": "valor" }
- Y listas de diccionarios → [ {...}, {...} ]
- Esto es lo más cercano a cómo los guarda la base de datos
"""

import sys
import os

# Esto agrega la carpeta raíz del proyecto al PATH de Python
# para que podamos importar database.py desde aquí
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database as db


# ─────────────────────────────────────────────
# DATOS: PROVEEDORES
# ─────────────────────────────────────────────
# Fuente: CSV + imágenes del SharePoint

PROVEEDORES = [
    {
        "nombre": "UFINET",
        "categoria": "Transporte / Conectividad",
        "portal_url": "https://gestionservicios.ufinet.com/auth",
        "usuario": "incident / customercwc",
        "contrasena": "Cwc2022* / Customer2022*",
        "telefono": "",
        "email": "noc.latam@ufinet.com / suministros@ufinet.com",
        "notas": "Dos usuarios: 'incident' para incidentes, 'customercwc' para gestión general"
    },
    {
        "nombre": "CIRION",
        "categoria": "Datacenter / Conectividad",
        "portal_url": "https://portal.ciriontechnologies.com/portal/#/login",
        "usuario": "csc@cwc.com",
        "contrasena": "CsCS2024$Liberty*",
        "telefono": "",
        "email": "csc@cwc.com",
        "notas": ""
    },
    {
        "nombre": "CLARO",
        "categoria": "Operador Telecom",
        "portal_url": "https://servicio.triara.co/ens/do",
        "usuario": "oscar.rodriguez@cwc.com",
        "contrasena": "c0lumbuS",
        "telefono": "18000127774 / 6013285000 / 3058170594 / 3058170190",
        "email": "oscar.rodriguez@cwc.com",
        "notas": "Si no genera reporte con CLARO, escalar a Movistar"
    },
    {
        "nombre": "AZTECA",
        "categoria": "Operador Telecom",
        "portal_url": "https://www.azteca-comunicaciones.com",
        "usuario": "csc@libertynet.com",
        "contrasena": "CsCS2024$Liberty*",
        "telefono": "",
        "email": "casantib@azteca-comunicaciones.com",
        "notas": ""
    },
    {
        "nombre": "MOVISTAR",
        "categoria": "Operador Telecom",
        "portal_url": "www.movistar.co/en/negocio/web-soporte-basico",
        "usuario": "clientes_dsp_ANS",
        "contrasena": "g&hPe9R4da",
        "telefono": "",
        "email": "",
        "notas": "Escalamiento disponible en portal web"
    },
    {
        "nombre": "ETB",
        "categoria": "Operador Telecom",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "4093113087 / 6017915300 / 6014066418",
        "email": "liderpalabronetb@etb.com.co / noc.latam@etb.com / capacitacionesempresariales@etb.com",
        "notas": "Columbus Networks de Colombia Ltda — proveedor ETB"
    },
    {
        "nombre": "TIGO",
        "categoria": "Operador Telecom",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "",
        "email": "gestiontelecomunicaciones@tigo.com.co",
        "notas": ""
    },
    {
        "nombre": "GTD",
        "categoria": "Conectividad",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "+57 314 880 019 / +57 314 782 9492 / +57 318 241 2354 / +57 318 710 1923",
        "email": "juan.penuela@grupogtd.com",
        "notas": "Escalamiento por niveles con tiempos definidos (ver contactos)"
    },
    {
        "nombre": "IDEAY",
        "categoria": "Conectividad / ISP",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "+505 8459 4000 / +505 7516 8547 / +505 7516 8960 / +505 8966 7932",
        "email": "noc@ideay.com / celia.sequeira@ideay.com / isaias.miranda@ideay.com / nschaffer.diaz@ideay.com",
        "notas": "Lista de escalación de 4 niveles (ver contactos)"
    },
    {
        "nombre": "LIBERTY NETWORKS",
        "categoria": "Conectividad / ISP",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "",
        "email": "",
        "notas": "Atención de fallas con niveles de escalación. Turnos On-Call por país."
    },
    {
        "nombre": "NETBEAM (Netstream)",
        "categoria": "Transporte / Monitoreo",
        "portal_url": "https://140.141.200.30:4994",
        "usuario": "",
        "contrasena": "",
        "telefono": "",
        "email": "noc@netbeam-digital.co / networking@netbeam.com.co / networking@netbeam.com.co",
        "notas": "Atención de incidentes: NOC 80 min, Networking 2h 7x24, Director 4h, Gerente 6h, Jorge 12h"
    },
    {
        "nombre": "MNC / MC.NET",
        "categoria": "Conectividad / ISP",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "018000112862",
        "email": "controldespacho@mc-net.co / soluciones1@mc-net.co / soluciones2@mc-net.co",
        "notas": "Número de MC: 018000112862. Escalamiento por niveles con tiempos (1h NOC, 2h Sub S&A, 4h Líder, 5h Gerente Operativo)"
    },
    {
        "nombre": "FLEXO",
        "categoria": "Conectividad",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "",
        "email": "",
        "notas": "Proveedor de conectividad"
    },
    {
        "nombre": "CENTURY LINK",
        "categoria": "Conectividad Internacional",
        "portal_url": "",
        "usuario": "",
        "contrasena": "",
        "telefono": "800-860-5493 / 800-641-893 / 800-690-903",
        "email": "",
        "notas": "Números On-Call: PA 9007507882752548 / RMNOC 9601429401 / DQ 9007506615136 / SV 9007503715060848 / ECU (809) 5006641 / GT (5025919-6716 / HN (504)9453-6449 / CR 506-0-7953482"
    },
]


# ─────────────────────────────────────────────
# DATOS: CONTACTOS POR PROVEEDOR
# ─────────────────────────────────────────────
# Formato: { "proveedor": "NOMBRE", "contactos": [ {...} ] }

CONTACTOS = [
    {
        "proveedor": "GTD",
        "contactos": [
            {"nombre": "Juan Guillermo Peñuela Vera",  "cargo": "Coordinador Centro de Experiencia", "telefono": "+57 314 880 019",  "email": "juan.penuela@grupogtd.com",    "nivel": "Nivel 1 - 60 min",  "horario": ""},
            {"nombre": "Carlos Ortega Hernández",       "cargo": "Jefe de Clientes y Servicios",      "telefono": "+57 314 782 9492", "email": "carlos.ortega@grupogtd.com",   "nivel": "Nivel 2 - 240 min", "horario": ""},
            {"nombre": "Ivan Amezcua Macín",            "cargo": "Gerente Experiencia al Cliente",    "telefono": "+57 318 241 2354", "email": "iamezcua@grupogtd.com",        "nivel": "Nivel 3 - 360 min", "horario": ""},
            {"nombre": "Fernando Maturana Almarza",     "cargo": "Gerente General Gtd Colombia",      "telefono": "+57 318 710 1923", "email": "fmaturana@grupogtd.com",       "nivel": "Nivel 4 - 480 min", "horario": ""},
        ]
    },
    {
        "proveedor": "IDEAY",
        "contactos": [
            {"nombre": "NOC L1",           "cargo": "Área de soporte NOC L1",         "telefono": "+505 8459 4000 / PBX 22559755 ext 2", "email": "noc@ideay.com",                   "nivel": "1er Nivel",      "horario": ""},
            {"nombre": "Celia Sequeira",   "cargo": "Coordinador NOC",                "telefono": "+505 7516 8547",                        "email": "celia.sequeira@ideay.com",        "nivel": "2do Nivel",      "horario": ""},
            {"nombre": "Isaias Miranda",   "cargo": "Coordinador Ingeniería y Proyectos", "telefono": "+505 7516 8960",                    "email": "isaias.miranda@ideay.com",        "nivel": "3er Nivel",      "horario": ""},
            {"nombre": "Otto Schaffer Diaz","cargo": "Gerencia de Operaciones",        "telefono": "+505 8966 7932",                        "email": "nschaffer.diaz@ideay.com",        "nivel": "4to Nivel",      "horario": ""},
        ]
    },
    {
        "proveedor": "LIBERTY NETWORKS",
        "contactos": [
            {"nombre": "B2B NOC LATAM",    "cargo": "Profesional de Soporte",          "telefono": "(1)8022 519322 / +57 3156038173 / +57 507-429-463", "email": "NOCLatam@mc.com",              "nivel": "Nivel 1",   "horario": "0 horas"},
            {"nombre": "Luzmeira Imthia",  "cargo": "Supervisora B2B NOC",             "telefono": "+57 3103189592",                                      "email": "luzmeira.imthia@libertynet.com","nivel": "Nivel 2",   "horario": "2 horas"},
            {"nombre": "Richard Lamouth",  "cargo": "Director NOC - B2B NOC",          "telefono": "+1 3007939440",                                       "email": "Richard.Lamouth@mc.com",       "nivel": "Nivel 3",   "horario": "4h 7x24"},
            {"nombre": "Mario Vignali",    "cargo": "Senior Director Technical Operations", "telefono": "+1 3057752410",                                  "email": "Mario.Vignali@lla.com",        "nivel": "Nivel 4",   "horario": "6 horas"},
            {"nombre": "Peter Collins",    "cargo": "VP Core Networks OPS",            "telefono": "+1 3054391677",                                       "email": "Peter.Collins@lla.com",        "nivel": "Nivel 5",   "horario": "8 horas"},
        ]
    },
    {
        "proveedor": "NETBEAM (Netstream)",
        "contactos": [
            {"nombre": "NOC",              "cargo": "Soporte NOC",           "telefono": "", "email": "noc@netbeam-digital.co",          "nivel": "Nivel 1", "horario": "80 min"},
            {"nombre": "Networking",       "cargo": "Soporte Networking",    "telefono": "", "email": "networking@netbeam.com.co",       "nivel": "Nivel 2", "horario": "2h 7x24"},
            {"nombre": "manuel.rojas",     "cargo": "Soporte",               "telefono": "", "email": "manuel.rojas@netbeam.com.co",    "nivel": "Nivel 2", "horario": "2h 7x24"},
            {"nombre": "andres.clavijo",   "cargo": "Soporte",               "telefono": "", "email": "andres.clavijo@netbeam.com.co",  "nivel": "Nivel 2", "horario": "2h 7x24"},
            {"nombre": "luisa.mesa",       "cargo": "Director",              "telefono": "", "email": "luisa.mesa@netbeam.com.co",      "nivel": "Nivel 3", "horario": "4h"},
            {"nombre": "director.noc",     "cargo": "Director NOC",          "telefono": "", "email": "director.noc@netbeam.com.co",    "nivel": "Nivel 3", "horario": "4h"},
            {"nombre": "Gerente",          "cargo": "Gerente",               "telefono": "", "email": "gerente@netbeam.com.co",         "nivel": "Nivel 4", "horario": "6h"},
            {"nombre": "Jorge Osorio",     "cargo": "Gerente",               "telefono": "", "email": "jorge.osorio@netbeam.com.co",    "nivel": "Nivel 5", "horario": "12h"},
        ]
    },
    {
        "proveedor": "ETB",
        "contactos": [
            {"nombre": "Centro de Contacto",        "cargo": "Centro de Atención al Cliente",        "telefono": "018000123737",    "email": "solucion_grandes_clientes@etb.com.co",  "nivel": "Día 0-1",  "horario": "L-V 7am-6pm"},
            {"nombre": "Paola Andrea Espejo",       "cargo": "Coordinación Operación PQR's (Quejas)","telefono": "3059308134",      "email": "paola.espejom2.pr@etb.com.co",           "nivel": "Día 3",    "horario": ""},
            {"nombre": "Lady Maritza Arias",        "cargo": "Coordinación Operación PQR's (Trámites)","telefono": "3058170602",    "email": "lady.ariasp1.pr@etb.com.co",             "nivel": "Día 3",    "horario": ""},
            {"nombre": "Maritza Montenegro",        "cargo": "Jefe de Operación PQR's (Quejas)",     "telefono": "3203912307",      "email": "marimon1@etb.com.co",                    "nivel": "Día 5",    "horario": ""},
            {"nombre": "Carolina Ovalle",           "cargo": "Jefe de Operación PQR's (Trámites)",   "telefono": "3057292804",      "email": "carolina.ovallev.pr@etb.com.co",         "nivel": "Día 5",    "horario": ""},
            {"nombre": "Cristian Cadena Marín",     "cargo": "Ejecutivo de Experiencia",             "telefono": "3059475164",      "email": "cristian.cadenam2.pr@etb.com.co",        "nivel": "Día 6",    "horario": ""},
            {"nombre": "Milena Vargas",             "cargo": "Líder de Segmento",                    "telefono": "305 7065941",     "email": "milena.vargasq@etb.com.co",              "nivel": "Día 7",    "horario": ""},
            {"nombre": "Angélica Palacios",         "cargo": "Coordinación Experiencia al Cliente",  "telefono": "3057067314",      "email": "angelica.palacioso@etb.com.co",          "nivel": "Día 9",    "horario": ""},
            {"nombre": "Roberto Uribe",             "cargo": "Dirección de Experiencia al Cliente",  "telefono": "3057841244",      "email": "roberto.uribeg@etb.com.co",              "nivel": "Día 13",   "horario": ""},
        ]
    },
    {
        "proveedor": "MNC / MC.NET",
        "contactos": [
            {"nombre": "Carlos Fabián Holguín Florez", "cargo": "NOC",              "telefono": "+57 3206032918",  "email": "carlos.holguin@mc.net.co",         "nivel": "Nivel 01 - Inmediato", "horario": ""},
            {"nombre": "Bryan Eduardo Guzmán González","cargo": "Sub S&A",          "telefono": "+57 3206770387",  "email": "bryan.guzman@mc.net.co",           "nivel": "Nivel 02 - 1 hora",    "horario": ""},
            {"nombre": "Cristian Camilo Uriche Velez", "cargo": "Líder de Soporte", "telefono": "+57 3207700387",  "email": "cristian.uriche@mc.net.co",        "nivel": "Nivel 03 - 2 horas",   "horario": ""},
            {"nombre": "Fabio Augusto Gutiérrez",      "cargo": "Sub S&A / Dr. Redes y Tecnología", "telefono": "+57 3936866082", "email": "fabio.gutierrez@mc.net.co", "nivel": "Nivel 04 - 4 horas", "horario": ""},
            {"nombre": "Gerente Operativo",            "cargo": "Gerente Operativo","telefono": "",               "email": "",                                 "nivel": "Nivel 05 - 5 horas",   "horario": ""},
        ]
    },
]


# ─────────────────────────────────────────────
# DATOS: ÁREAS / PAÍSES
# ─────────────────────────────────────────────

AREAS = [
    {"nombre": "Colombia",        "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "Honduras",        "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "+504 2280 7777", "oncall_l3": "",                "oncall_tel": "+505 21213599", "notas": ""},
    {"nombre": "Panama",          "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "Opción 1",        "oncall_tel": "+506 41008611", "notas": ""},
    {"nombre": "R. Dominicana",   "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "Salvador",        "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "Guatemala",       "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "Costa Rica",      "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "CSCVOICE",        "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": "Área de soporte de voz"},
    {"nombre": "NOCESCPR",        "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": "NOC Escalamiento PR"},
    {"nombre": "NETCOOL",         "correo": "",                                      "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": "Plataforma de monitoreo"},
    # Libertynet por país
    {"nombre": "Libertynet - Honduras",    "correo": "libertynet.com",               "extension": "",    "jefe": "Gerente Asociado Cuidado al Cliente", "jefe_tel": "",   "oncall_l3": "Carlos Hincapié / Paola Lancheros", "oncall_tel": "+57 300 2725207 / +57 3127737905", "notas": "Equipo Ciclo de vida: ciclodevidade@libertynet.com"},
    {"nombre": "Libertynet - Costa Rica",  "correo": "libertynet.com",               "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "Libertynet - Panama",      "correo": "libertynet.com",               "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
    {"nombre": "Libertynet - Salvador",    "correo": "libertynet.com",               "extension": "",    "jefe": "",                   "jefe_tel": "",              "oncall_l3": "",                "oncall_tel": "",              "notas": ""},
]


# ─────────────────────────────────────────────
# DATOS: EQUIPO RMP
# ─────────────────────────────────────────────

EQUIPO_RMP = [
    {"nombre": "Valentina Herrera",        "cargo": "Personal Noc",       "celular": "+57 3219498463", "email": "valentina@rmp.com",    "notas": ""},
    {"nombre": "Monica Contreras",         "cargo": "Personal Noc",       "celular": "+57 3176862861", "email": "monica@rmp.com",       "notas": ""},
    {"nombre": "Maria Camila Zapata",      "cargo": "Coordinadora",       "celular": "+57 314 8447367","email": "mcamila@rmp.com",      "notas": ""},
    {"nombre": "Laura Ospina",             "cargo": "Coordinadora",       "celular": "",               "email": "laura@rmp.com",        "notas": ""},
    {"nombre": "Laura Cano",               "cargo": "Coordinadora",       "celular": "",               "email": "lcano@rmp.com",        "notas": ""},
    {"nombre": "Jennifer Espitia",         "cargo": "Coordinadora",       "celular": "+57 314 9441642","email": "jespitia@rmp.com",     "notas": ""},
    {"nombre": "David Acevedo Muñoz ADS",  "cargo": "Ingeniero",          "celular": "+57 321 3998402","email": "dacevedo@rmp.com",     "notas": ""},
    {"nombre": "Andres Morales Piso Pérez","cargo": "Ingeniero",          "celular": "",               "email": "amorales@rmp.com",     "notas": ""},
    {"nombre": "Ngestor Comercial",        "cargo": "Comercial",          "celular": "",               "email": "ngestor@rmp.com",      "notas": ""},
]


# ─────────────────────────────────────────────
# DATOS: EXTENSIONES INTERNAS
# ─────────────────────────────────────────────

EXTENSIONES = [
    {"numero": "19981",       "servicio": "DC",              "descripcion": "Datacenter"},
    {"numero": "19982",       "servicio": "NETWORKING",      "descripcion": "Soporte Networking"},
    {"numero": "19985",       "servicio": "SOC",             "descripcion": "Security Operations Center"},
    {"numero": "5023",        "servicio": "SOC L3",          "descripcion": "SOC Nivel 3"},
    {"numero": "5025",        "servicio": "NOC",             "descripcion": "Network Operations Center"},
    {"numero": "19171",       "servicio": "CSIRT",           "descripcion": "Computer Security Incident Response Team"},
    {"numero": "19980",       "servicio": "(Voice) UC",      "descripcion": "Soporte Voz Unificada"},
    {"numero": "19984",       "servicio": "UNICOMER",        "descripcion": "Soporte Unicomer"},
    {"numero": "3322",        "servicio": "FLOW JAMAICA",    "descripcion": "Flow Jamaica"},
    {"numero": "2001",        "servicio": "FLOW TRINIDAD",   "descripcion": "Flow Trinidad"},
    {"numero": "2751",        "servicio": "FLOW CURACAO",    "descripcion": "Flow Curazao"},
    {"numero": "7586",        "servicio": "SI USA",          "descripcion": "SI Estados Unidos"},
    {"numero": "7294",        "servicio": "TX USA",          "descripcion": "TX Estados Unidos"},
    {"numero": "4831",        "servicio": "APROVISIONAMIENTO","descripcion": "Aprovisionamiento"},
    {"numero": "4236",        "servicio": "DISP. IASS",      "descripcion": "Disposición IASS"},
    {"numero": "1615",        "servicio": "SID",             "descripcion": "SID"},
    {"numero": "7812",        "servicio": "NAP",             "descripcion": "NAP"},
    {"numero": "3216484276",  "servicio": "BT DC Nimbus",    "descripcion": "BT DC Nimbus - Manos Remotas"},
    {"numero": "7513",        "servicio": "IP SERVICES",     "descripcion": "Servicios IP"},
    {"numero": "7517",        "servicio": "",                "descripcion": "Extensión adicional"},
]

# ─────────────────────────────────────────────
# DATOS: TURNOS DMC — LIBERTY NETWORKS
# ─────────────────────────────────────────────

TURNOS_DMC = [
    # Honduras
    {"pais": "Honduras", "dia_semana": "Lunes a Viernes",  "horario_ini": "07:00 pm", "horario_fin": "07:00 am", "telefono": "+504 9453-6449", "ingeniero": "", "notas": ""},
    {"pais": "Honduras", "dia_semana": "On Call Sábado",   "horario_ini": "12:00 pm", "horario_fin": "",          "telefono": "+504 9453-6449", "ingeniero": "", "notas": "Fin de semana"},
    {"pais": "Honduras", "dia_semana": "On Call Domingo",  "horario_ini": "",          "horario_fin": "07:00 am", "telefono": "+504 9453-6449", "ingeniero": "", "notas": "A lunes"},
    # Guatemala
    {"pais": "Guatemala","dia_semana": "Lunes a Viernes",  "horario_ini": "08:00 pm", "horario_fin": "07:00 am", "telefono": "+502 5919-6716", "ingeniero": "", "notas": ""},
    {"pais": "Guatemala","dia_semana": "On Call Fin Semana","horario_ini": "",          "horario_fin": "",          "telefono": "+502 5919-6716", "ingeniero": "", "notas": "Sábado y Domingo"},
    # El Salvador
    {"pais": "El Salvador","dia_semana": "Lunes a Viernes","horario_ini": "07:00 pm", "horario_fin": "07:00 am", "telefono": "+503 7150 6984", "ingeniero": "", "notas": ""},
    {"pais": "El Salvador","dia_semana": "On Call Fin Semana","horario_ini": "",        "horario_fin": "",          "telefono": "+503 7150 6984", "ingeniero": "", "notas": "Sábado y Domingo"},
]

# ─────────────────────────────────────────────
# DATOS: MANOS REMOTAS — COBERTURA COLOMBIA
# ─────────────────────────────────────────────

MANOS_REMOTAS = [
    # Cundinamarca
    {"municipio": "Bogotá",       "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": "freddy.rodriguez@sti.com.co / Gustavo.sanchez@stiias.co"},
    {"municipio": "Chía",         "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Cajicá",       "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Cota",         "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Funza",        "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Tenjo",        "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Zipaquirá",    "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Mosquera",     "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Girardot",     "departamento": "Cundinamarca", "tipo_lugar": "Tipo 3", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Facatativá",   "departamento": "Cundinamarca", "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    # Córdoba
    {"municipio": "Montería",     "departamento": "Córdoba",      "tipo_lugar": "Tipo 2", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "Planeta Rica", "departamento": "Córdoba",      "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "Lorica",       "departamento": "Córdoba",      "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "Sahagún",      "departamento": "Córdoba",      "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "Monte Líbano", "departamento": "Córdoba",      "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "Cereté",       "departamento": "Córdoba",      "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    # Valle del Cauca
    {"municipio": "Yumbo",        "departamento": "Valle del Cauca","tipo_lugar":"Tipo 3", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Palmira",      "departamento": "Valle del Cauca","tipo_lugar":"Tipo 1", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Cali",         "departamento": "Valle del Cauca","tipo_lugar":"Tipo 1", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Buga",         "departamento": "Valle del Cauca","tipo_lugar":"Tipo 2", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Buenaventura", "departamento": "Valle del Cauca","tipo_lugar":"Tipo 2", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Jamundí",      "departamento": "Valle del Cauca","tipo_lugar":"Tipo 2", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Candelaria",   "departamento": "Valle del Cauca","tipo_lugar":"Tipo 2", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Tulúa",        "departamento": "Valle del Cauca","tipo_lugar":"Tipo 2", "proveedor_ppal": "STI",      "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    # Antioquia
    {"municipio": "Medellín",     "departamento": "Antioquia",    "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Itagüí",       "departamento": "Antioquia",    "tipo_lugar": "Tipo 2", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    {"municipio": "Envigado",     "departamento": "Antioquia",    "tipo_lugar": "Tipo 3", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    # Santander
    {"municipio": "Piedecuesta",  "departamento": "Santander",    "tipo_lugar": "Tipo 2", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez / Mónica Villamizar"},
    {"municipio": "San Gil",      "departamento": "Santander",    "tipo_lugar": "Tipo 2", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    {"municipio": "Socorro",      "departamento": "Santander",    "tipo_lugar": "Tipo 3", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    {"municipio": "Río negro",    "departamento": "Santander",    "tipo_lugar": "Tipo 3", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    {"municipio": "Barrancabermeja","departamento":"Santander",   "tipo_lugar": "Tipo 2", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    # Norte de Santander
    {"municipio": "Cúcuta",       "departamento": "Norte de Santander","tipo_lugar":"Tipo 3","proveedor_ppal":"INPRORIENTE","proveedor_bk":"ACT","contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    # Risaralda
    {"municipio": "Pereira",      "departamento": "Risaralda",    "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    # Caldas
    {"municipio": "Manizales",    "departamento": "Caldas",       "tipo_lugar": "Tipo 1", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    # Sucre
    {"municipio": "Sincelejo",    "departamento": "Sucre",        "tipo_lugar": "Tipo 1", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "San Onofre",   "departamento": "Sucre",        "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "San Marcos",   "departamento": "Sucre",        "tipo_lugar": "Tipo 3", "proveedor_ppal": "R.TIF SAS", "proveedor_bk": "ACT",  "contacto_email": "redestelecomunicacionessas@gmail.com","contacto_tel": "302-3945879", "contacto_esc": "Ivan E Marriaga"},
    {"municipio": "Valledupar",   "departamento": "Sucre",        "tipo_lugar": "Tipo 3", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    # Atlántico
    {"municipio": "Barranquilla", "departamento": "Atlántico",    "tipo_lugar": "Tipo 1", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido / 315 2692065"},
    {"municipio": "Puerto Colombia","departamento":"Atlántico",   "tipo_lugar": "Tipo 2", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    {"municipio": "Galapa",       "departamento": "Atlántico",    "tipo_lugar": "Tipo 3", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    {"municipio": "Soledad",      "departamento": "Atlántico",    "tipo_lugar": "Tipo 2", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    {"municipio": "Malambo",      "departamento": "Atlántico",    "tipo_lugar": "Tipo 2", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    {"municipio": "Sabanalarga",  "departamento": "Atlántico",    "tipo_lugar": "Tipo 3", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    {"municipio": "Baranoa",      "departamento": "Atlántico",    "tipo_lugar": "Tipo 3", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    # Guajira
    {"municipio": "Riohacha",     "departamento": "Guajira",      "tipo_lugar": "Tipo 2", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    # Magdalena
    {"municipio": "Santa Marta",  "departamento": "Magdalena",    "tipo_lugar": "Tipo 1", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    # Cartagena
    {"municipio": "Cartagena",    "departamento": "Bolívar",      "tipo_lugar": "Tipo 1", "proveedor_ppal": "ACT",       "proveedor_bk": "RMP",  "contacto_email": "ingrid.pinilla@actitelematica.com.co","contacto_tel":"318 3279401","contacto_esc": "Diana Pulido"},
    # Cesar
    {"municipio": "Valledupar",   "departamento": "Cesar",        "tipo_lugar": "Tipo 1", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    {"municipio": "Curumani",     "departamento": "Cesar",        "tipo_lugar": "Tipo 2", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    {"municipio": "Aguachica",    "departamento": "Cesar",        "tipo_lugar": "Tipo 2", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    {"municipio": "Bosconia",     "departamento": "Cesar",        "tipo_lugar": "Tipo 2", "proveedor_ppal": "INPRORIENTE","proveedor_bk": "ACT", "contacto_email": "inspector.obras@inproriente.com", "contacto_tel": "3214449701",   "contacto_esc": "Jhon Álvarez"},
    # Huilas
    {"municipio": "Neiva",        "departamento": "Huila",        "tipo_lugar": "Tipo 2", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
    # Nariño
    {"municipio": "Pasto",        "departamento": "Nariño",       "tipo_lugar": "Tipo 2", "proveedor_ppal": "STI",       "proveedor_bk": "RMP",  "contacto_email": "Liberty@sti.com.co",              "contacto_tel": "",             "contacto_esc": ""},
]

# Proveedores de Manos Remotas con sus contactos de escalamiento
PROVEEDORES_MR = {
    "STI": {
        "email_principal": "Liberty@sti.com.co",
        "contactos": [
            {"nombre": "Freddy Rodríguez",  "email": "freddy.rodriguez@sti.com.co", "tel": "3208095620"},
            {"nombre": "Gustavo Sánchez",   "email": "Gustavo.sanchez@stiias.co",   "tel": ""},
        ]
    },
    "ACT": {
        "email_principal": "ingrid.pinilla@actitelematica.com.co",
        "contactos": [
            {"nombre": "Ingrid Pinilla",    "email": "ingrid.pinilla@actitelematica.com.co", "tel": "318 3279401"},
            {"nombre": "Diana Pulido",      "email": "diana.pulido@actitelematica.com.co",   "tel": "315 2692065"},
            {"nombre": "Daniel Sandoval",   "email": "daniel.sandoval@actitelematica.com.co","tel": "3174274170"},
            {"nombre": "Alberto Bello",     "email": "Alberto.bello@actitelematica.com.co",  "tel": ""},
            {"nombre": "Ashlley Russo",     "email": "ashlley.russo@actitelematica.com.co",  "tel": ""},
            {"nombre": "Mike Bernal",       "email": "mike.bernal@actitelematica.com.co",    "tel": "316 3510138"},
        ]
    },
    "INPRORIENTE": {
        "email_principal": "gerencia@inproriente.com",
        "contactos": [
            {"nombre": "Gerencia",          "email": "gerencia@inproriente.com",            "tel": "3214449701"},
            {"nombre": "Jhon Álvarez",      "email": "inspector.obras@inproriente.com",     "tel": "3214449701"},
            {"nombre": "Mónica Villamizar", "email": "",                                     "tel": "3206161190"},
        ]
    },
    "R.TIF SAS": {
        "email_principal": "redestelecomunicacionessas@gmail.com",
        "contactos": [
            {"nombre": "Ivan E Marriaga",   "email": "redestelecomunicacionessas@gmail.com","tel": "302-3945879"},
        ]
    },
}


# ─────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: cargar todo a la BD
# ─────────────────────────────────────────────

def cargar_datos_iniciales():
    """
    Carga todos los datos a la base de datos.
    Esta función es llamada desde app.py al iniciar la aplicación.
    Solo se ejecuta si la BD está vacía (gracias a bd_tiene_datos()).
    """

    print("🌱 Cargando datos iniciales...")

    # ── 1. Proveedores ────────────────────────
    print("  → Cargando proveedores...")
    # Guardamos un mapa nombre→id para luego asignar contactos
    mapa_proveedores = {}

    for p in PROVEEDORES:
        nuevo_id = db.agregar_proveedor(
            nombre      = p["nombre"],
            categoria   = p["categoria"],
            portal_url  = p["portal_url"],
            usuario     = p["usuario"],
            contrasena  = p["contrasena"],
            telefono    = p["telefono"],
            email       = p["email"],
            notas       = p["notas"]
        )
        # Guardamos el id asignado para usarlo en los contactos
        mapa_proveedores[p["nombre"]] = nuevo_id

    print(f"     ✅ {len(PROVEEDORES)} proveedores cargados")

    # ── 2. Contactos ──────────────────────────
    print("  → Cargando contactos...")
    total_contactos = 0
    for grupo in CONTACTOS:
        proveedor_nombre = grupo["proveedor"]
        proveedor_id = mapa_proveedores.get(proveedor_nombre)
        if not proveedor_id:
            print(f"     ⚠️  Proveedor '{proveedor_nombre}' no encontrado, saltando contactos...")
            continue
        for c in grupo["contactos"]:
            db.agregar_contacto(
                proveedor_id = proveedor_id,
                nombre       = c["nombre"],
                cargo        = c["cargo"],
                telefono     = c["telefono"],
                email        = c["email"],
                nivel        = c["nivel"],
                horario      = c["horario"]
            )
            total_contactos += 1

    print(f"     ✅ {total_contactos} contactos cargados")

    # ── 3. Áreas / Países ─────────────────────
    print("  → Cargando áreas/países...")
    for a in AREAS:
        db.agregar_area(
            nombre     = a["nombre"],
            correo     = a["correo"],
            extension  = a["extension"],
            jefe       = a["jefe"],
            jefe_tel   = a["jefe_tel"],
            oncall_l3  = a["oncall_l3"],
            oncall_tel = a["oncall_tel"],
            notas      = a["notas"]
        )
    print(f"     ✅ {len(AREAS)} áreas cargadas")

    # ── 4. Equipo RMP ─────────────────────────
    print("  → Cargando equipo RMP...")
    for m in EQUIPO_RMP:
        db.agregar_miembro_rmp(
            nombre  = m["nombre"],
            cargo   = m["cargo"],
            celular = m["celular"],
            email   = m["email"],
            notas   = m["notas"]
        )
    print(f"     ✅ {len(EQUIPO_RMP)} miembros RMP cargados")

    # ── 5. Extensiones ────────────────────────
    print("  → Cargando extensiones...")
    for e in EXTENSIONES:
        db.agregar_extension(
            numero      = e["numero"],
            servicio    = e["servicio"],
            descripcion = e["descripcion"]
        )
    print(f"     ✅ {len(EXTENSIONES)} extensiones cargadas")

    # ── 6. Manos Remotas ─────────────────────
    print("  → Cargando manos remotas...")
    for mr in MANOS_REMOTAS:
        db.agregar_mano_remota(
            municipio      = mr["municipio"],
            departamento   = mr["departamento"],
            tipo_lugar     = mr["tipo_lugar"],
            proveedor_ppal = mr["proveedor_ppal"],
            proveedor_bk   = mr["proveedor_bk"],
            contacto_email = mr["contacto_email"],
            contacto_tel   = mr["contacto_tel"],
            contacto_esc   = mr["contacto_esc"]
        )
    print(f"     ✅ {len(MANOS_REMOTAS)} municipios de manos remotas cargados")

    # ── 7. Turnos DMC ────────────────────────
    print("  → Cargando turnos DMC...")
    for t in TURNOS_DMC:
        db.agregar_turno_dmc(
            pais        = t["pais"],
            dia_semana  = t["dia_semana"],
            horario_ini = t["horario_ini"],
            horario_fin = t["horario_fin"],
            telefono    = t["telefono"],
            ingeniero   = t["ingeniero"],
            notas       = t["notas"]
        )
    print(f"     ✅ {len(TURNOS_DMC)} turnos DMC cargados")

    print("\n🎉 ¡Datos iniciales cargados correctamente!")


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA (para probar solo este archivo)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    db.crear_tablas()
    if not db.bd_tiene_datos():
        cargar_datos_iniciales()
    else:
        print("⚠️  La base de datos ya tiene datos. No se recargaron.")
