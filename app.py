import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA Y MARCA
st.set_page_config(page_title="AhoraSI Marketplace", layout="wide")

st.title("🚀 AhoraSI Marketplace")
st.markdown("### La vitrina de activos digitales para creadores de IA")

# 2. SIMULACIÓN DE BASE DE DATOS (En un proyecto real usarías SQLite o Supabase)
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = pd.DataFrame([
        {"id": 1, "nombre": "Claudio Heyden", "wsp": "56912345678", "estado": "Activa", "bio": "Experto en No-Code"},
        {"id": 2, "nombre": "Creador Demo", "wsp": "56987654321", "estado": "Inactiva", "bio": "Prompts Pro"}
    ])

if 'contenidos' not in st.session_state:
    st.session_state.contenidos = pd.DataFrame([
        {"id": 101, "creador_id": 1, "titulo": "Guía de Prompts Pro", "precio": 3000, "cat": "Guías IA"},
        {"id": 102, "creador_id": 1, "titulo": "Pack 50 Ideas Negocio", "precio": 5000, "cat": "Marketing"},
        {"id": 103, "creador_id": 2, "titulo": "Curso Midjourney", "precio": 10000, "cat": "Cursos"}
    ])

# 3. LÓGICA DE NAVEGACIÓN (Sidebar)
menu = st.sidebar.selectbox("Ir a:", ["Vitrina Pública", "Mi Panel (Creadores)", "Admin (Suscripciones)"])

# --- VISTA 1: VITRINA PÚBLICA ---
if menu == "Vitrina Pública":
    st.subheader("Todos los activos disponibles")
    
    # Cruce de datos: Solo mostrar guías de creadores con suscripción ACTIVA
    df_activos = st.session_state.contenidos.merge(
        st.session_state.usuarios[st.session_state.usuarios['estado'] == 'Activa'],
        left_on='creador_id', right_on='id'
    )

    cols = st.columns(3)
    for index, row in df_activos.iterrows():
        with cols[index % 3]:
            st.info(f"*{row['titulo']}*")
            st.write(f"Vendedor: {row['nombre']}")
            st.write(f"Precio: ${row['precio']}")
            
            # Botón dinámico de WhatsApp
            wsp_link = f"https://wa.me/{row['wsp']}?text=Hola%20{row['nombre']},%20quiero%20comprar:%20{row['titulo']}"
            st.markdown(f"[![Comprar](https://img.shields.io/badge/Comprar-WhatsApp-25D366?style=for-the-badge&logo=whatsapp)]({wsp_link})")

# --- VISTA 2: PANEL DEL CREADOR ---
elif menu == "Mi Panel (Creadores)":
    st.subheader("Gestión de tus Guías")
    usuario_actual = st.selectbox("Simular sesión como:", st.session_state.usuarios['nombre'])
    datos_user = st.session_state.usuarios[st.session_state.usuarios['nombre'] == usuario_actual].iloc[0]

    if datos_user['estado'] == "Activa":
        st.success("✅ Tu suscripción está activa. Puedes publicar.")
        with st.expander("➕ Publicar Nueva Guía"):
            nuevo_titulo = st.text_input("Título de la guía")
            nuevo_precio = st.number_input("Precio", min_value=0)
            if st.button("Subir guía"):
                st.write(f"Publicando {nuevo_titulo}...")
    else:
        st.error("❌ Tu suscripción está inactiva. Contacta a Claudio para renovar.")
        st.button("Pagar Suscripción vía Transferencia")

# --- VISTA 3: ADMIN (Donde tú controlas el negocio) ---
elif menu == "Admin (Suscripciones)":
    st.subheader("Panel de Control de AhoraSI")
    st.write("Aquí activas o desactivas a los creadores que te han pagado.")
    
    for i, row in st.session_state.usuarios.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"*{row['nombre']}* - Estado actual: {row['estado']}")
        with col2:
            if st.button("Cambiar Estado", key=f"btn_{i}"):
                nuevo_estado = "Inactiva" if row['estado'] == "Activa" else "Activa"
                st.session_state.usuarios.at[i, 'estado'] = nuevo_estado
                st.rerun()
