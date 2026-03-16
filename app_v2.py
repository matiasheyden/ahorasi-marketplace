import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS PERSONALIZADOS
st.set_page_config(
    page_title="AhoraSI Marketplace", 
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS PERSONALIZADO PARA ESTILOS ATRACTIVOS
st.markdown("""
<style>
    /* Estilo general */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Cards de productos */
    .product-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .product-card:hover {
        transform: translateY(-5px);
    }
    
    /* Botón WhatsApp */
    .whatsapp-btn {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        padding: 12px 24px;
        border-radius: 30px;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
    }
    .whatsapp-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.6);
    }
    
    /* Botón Chat Interno */
    .chat-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        padding: 12px 24px;
        border-radius: 30px;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Precio destacado */
    .price-tag {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 1.3em;
        font-weight: bold;
        display: inline-block;
    }
    
    /* Badge de categoría */
    .category-badge {
        background: #e8f5e9;
        color: #2e7d32;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85em;
        font-weight: 500;
    }
    
    /* Header del sidebar */
    .sidebar-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Stats cards */
    .stat-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    .stat-number {
        font-size: 2.5em;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Botones de acción */
    .stButton>button {
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    /* Imagen de producto */
    .product-image {
        border-radius: 15px;
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    
    /* Rating stars */
    .rating {
        color: #ffc107;
        font-size: 1.2em;
    }
    
    /* Chat container */
    .chat-container {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 15px;
        max-height: 400px;
        overflow-y: auto;
    }
    .chat-message {
        background: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .chat-message.sent {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 20%;
    }
    .chat-message.received {
        background: #e8f5e9;
        margin-right: 20%;
    }
</style>
""", unsafe_allow_html=True)

# 2. INICIALIZACIÓN DE BASE DE DATOS SIMULADA
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = pd.DataFrame([
        {"id": 1, "nombre": "Claudio Heyden", "wsp": "56912345678", "estado": "Activa", 
         "bio": "Experto en No-Code y automatización", "email": "claudio@ahorasi.cl",
         "fecha_registro": "2024-01-15", "plan": "Premium", "ventas": 45, "rating": 4.8},
        {"id": 2, "nombre": "María González", "wsp": "56987654321", "estado": "Activa", 
         "bio": "Especialista en Marketing Digital", "email": "maria@email.com",
         "fecha_registro": "2024-02-20", "plan": "Básico", "ventas": 28, "rating": 4.5},
        {"id": 3, "nombre": "Pedro Tech", "wsp": "56911223344", "estado": "Inactiva", 
         "bio": "Desarrollador de Prompts IA", "email": "pedro@email.com",
         "fecha_registro": "2024-03-10", "plan": "Premium", "ventas": 12, "rating": 4.2}
    ])

if 'contenidos' not in st.session_state:
    st.session_state.contenidos = pd.DataFrame([
        {"id": 101, "creador_id": 1, "titulo": "🎯 Guía Maestra de Prompts Pro", 
         "descripcion": "50+ prompts probados para ChatGPT, Claude y Gemini. Aumenta tu productividad 10x.",
         "precio": 3000, "cat": "Guías IA", "ventas": 120, "rating": 4.9,
         "imagen": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400"},
        {"id": 102, "creador_id": 1, "titulo": "💡 Pack 50 Ideas de Negocio 2024", 
         "descripcion": "Ideas validadas de negocios digitales con bajo capital inicial.",
         "precio": 5000, "cat": "Emprendimiento", "ventas": 85, "rating": 4.7,
         "imagen": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400"},
        {"id": 103, "creador_id": 2, "titulo": "🎨 Curso Completo Midjourney", 
         "descripcion": "Aprende a crear imágenes impresionantes con IA. De principiante a experto.",
         "precio": 10000, "cat": "Cursos", "ventas": 67, "rating": 4.8,
         "imagen": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=400"},
        {"id": 104, "creador_id": 2, "titulo": "📱 Templates Canva Premium", 
         "descripcion": "100 templates editables para redes sociales. Instagram, TikTok, LinkedIn.",
         "precio": 4500, "cat": "Diseño", "ventas": 156, "rating": 4.6,
         "imagen": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=400"},
        {"id": 105, "creador_id": 1, "titulo": "🤖 Automatizaciones Make/Zapier", 
         "descripcion": "10 flujos listos para copiar. Ahorra 20+ horas semanales.",
         "precio": 8000, "cat": "Automatización", "ventas": 42, "rating": 4.9,
         "imagen": "https://images.unsplash.com/photo-1518186285589-2f7649de83e0?w=400"},
        {"id": 106, "creador_id": 3, "titulo": "📊 Dashboard Analytics Notion", 
         "descripcion": "Template completo para trackear tu negocio digital.",
         "precio": 2500, "cat": "Productividad", "ventas": 89, "rating": 4.4,
         "imagen": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400"}
    ])

if 'mensajes_chat' not in st.session_state:
    st.session_state.mensajes_chat = []

if 'carrito' not in st.session_state:
    st.session_state.carrito = []

if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

if 'transacciones' not in st.session_state:
    st.session_state.transacciones = pd.DataFrame([
        {"id": 1, "fecha": "2024-03-15", "comprador": "Juan Pérez", "producto_id": 101, "monto": 3000, "estado": "Completada", "metodo": "Transferencia"},
        {"id": 2, "fecha": "2024-03-14", "comprador": "Ana López", "producto_id": 103, "monto": 10000, "estado": "Completada", "metodo": "WebPay"},
        {"id": 3, "fecha": "2024-03-14", "comprador": "Carlos Ruiz", "producto_id": 102, "monto": 5000, "estado": "Pendiente", "metodo": "Transferencia"},
        {"id": 4, "fecha": "2024-03-13", "comprador": "Laura Díaz", "producto_id": 104, "monto": 4500, "estado": "Completada", "metodo": "WebPay"},
        {"id": 5, "fecha": "2024-03-12", "comprador": "Diego Mora", "producto_id": 101, "monto": 3000, "estado": "Completada", "metodo": "Transferencia"},
    ])

# 3. SIDEBAR CON NAVEGACIÓN MEJORADA
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h1>🚀 AhoraSI</h1>
        <p>Marketplace Digital</p>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.selectbox(
        "📍 Navegación",
        ["🏪 Vitrina Pública", "❤️ Mis Favoritos", "🛒 Mi Carrito", 
         "👤 Mi Panel (Creadores)", "⚙️ Admin Dashboard"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Búsqueda global
    busqueda = st.text_input("🔍 Buscar productos...", placeholder="Ej: prompts, cursos...")
    
    # Filtros
    st.subheader("🎛️ Filtros")
    categorias = ["Todas"] + list(st.session_state.contenidos['cat'].unique())
    categoria_filtro = st.selectbox("Categoría", categorias)
    
    precio_min, precio_max = st.slider(
        "💰 Rango de precio",
        0, 15000, (0, 15000),
        format="$%d"
    )
    
    ordenar_por = st.selectbox(
        "📊 Ordenar por",
        ["Más vendidos", "Mejor valorados", "Precio: menor a mayor", "Precio: mayor a menor", "Más recientes"]
    )
    
    st.divider()
    st.caption("© 2024 AhoraSI Marketplace")
    st.caption("Creado con ❤️ en Chile")

# 4. FUNCIONES AUXILIARES
def mostrar_estrellas(rating):
    estrellas_llenas = int(rating)
    media_estrella = 1 if rating - estrellas_llenas >= 0.5 else 0
    estrellas_vacias = 5 - estrellas_llenas - media_estrella
    return "⭐" * estrellas_llenas + "✨" * media_estrella + "☆" * estrellas_vacias

def filtrar_productos(df):
    # Filtrar por búsqueda
    if busqueda:
        df = df[df['titulo'].str.lower().str.contains(busqueda.lower()) | 
                df['descripcion'].str.lower().str.contains(busqueda.lower())]
    
    # Filtrar por categoría
    if categoria_filtro != "Todas":
        df = df[df['cat'] == categoria_filtro]
    
    # Filtrar por precio
    df = df[(df['precio'] >= precio_min) & (df['precio'] <= precio_max)]
    
    # Ordenar
    if ordenar_por == "Más vendidos":
        df = df.sort_values('ventas', ascending=False)
    elif ordenar_por == "Mejor valorados":
        df = df.sort_values('rating', ascending=False)
    elif ordenar_por == "Precio: menor a mayor":
        df = df.sort_values('precio', ascending=True)
    elif ordenar_por == "Precio: mayor a menor":
        df = df.sort_values('precio', ascending=False)
    
    return df

# ==================== VISTA 1: VITRINA PÚBLICA ====================
if menu == "🏪 Vitrina Pública":
    st.markdown("<h1 style='text-align: center; color: white;'>🚀 AhoraSI Marketplace</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>La vitrina de activos digitales para creadores de IA</h3>", unsafe_allow_html=True)
    
    # Métricas rápidas con estilo destacado
    total_productos = len(st.session_state.contenidos)
    total_creadores = len(st.session_state.usuarios[st.session_state.usuarios['estado'] == 'Activa'])
    total_ventas = st.session_state.contenidos['ventas'].sum()
    rating_promedio = st.session_state.contenidos['rating'].mean()
    
    st.markdown(f"""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; margin: 30px 0;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 20px; padding: 25px 40px; text-align: center; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3); min-width: 200px;
                    border: 2px solid rgba(255,255,255,0.2);">
            <div style="font-size: 3em; margin-bottom: 10px;">📦</div>
            <div style="font-size: 2.5em; font-weight: bold; color: white;">{total_productos}</div>
            <div style="font-size: 1.3em; color: rgba(255,255,255,0.9); font-weight: 600; margin-top: 5px;">PRODUCTOS</div>
        </div>
        <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                    border-radius: 20px; padding: 25px 40px; text-align: center; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3); min-width: 200px;
                    border: 2px solid rgba(255,255,255,0.2);">
            <div style="font-size: 3em; margin-bottom: 10px;">👥</div>
            <div style="font-size: 2.5em; font-weight: bold; color: white;">{total_creadores}</div>
            <div style="font-size: 1.3em; color: rgba(255,255,255,0.9); font-weight: 600; margin-top: 5px;">CREADORES</div>
        </div>
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    border-radius: 20px; padding: 25px 40px; text-align: center; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3); min-width: 200px;
                    border: 2px solid rgba(255,255,255,0.2);">
            <div style="font-size: 3em; margin-bottom: 10px;">🛒</div>
            <div style="font-size: 2.5em; font-weight: bold; color: white;">{total_ventas}</div>
            <div style="font-size: 1.3em; color: rgba(255,255,255,0.9); font-weight: 600; margin-top: 5px;">VENTAS TOTALES</div>
        </div>
        <div style="background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%); 
                    border-radius: 20px; padding: 25px 40px; text-align: center; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3); min-width: 200px;
                    border: 2px solid rgba(255,255,255,0.2);">
            <div style="font-size: 3em; margin-bottom: 10px;">⭐</div>
            <div style="font-size: 2.5em; font-weight: bold; color: white;">{rating_promedio:.1f}</div>
            <div style="font-size: 1.3em; color: rgba(255,255,255,0.9); font-weight: 600; margin-top: 5px;">RATING PROMEDIO</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Obtener productos de creadores activos
    df_activos = st.session_state.contenidos.merge(
        st.session_state.usuarios[st.session_state.usuarios['estado'] == 'Activa'],
        left_on='creador_id', right_on='id', suffixes=('', '_user')
    )
    
    # Aplicar filtros
    df_filtrado = filtrar_productos(df_activos)
    
    if len(df_filtrado) == 0:
        st.warning("😕 No se encontraron productos con esos filtros. Intenta con otros criterios.")
    else:
        st.subheader(f"📦 {len(df_filtrado)} productos disponibles")
        
        # Mostrar productos en grid
        cols = st.columns(3)
        for idx, (index, row) in enumerate(df_filtrado.iterrows()):
            with cols[idx % 3]:
                with st.container():
                    # Imagen del producto
                    st.image(row['imagen'], use_container_width=True)
                    
                    # Categoría badge
                    st.markdown(f"<span class='category-badge'>{row['cat']}</span>", unsafe_allow_html=True)
                    
                    # Título
                    st.markdown(f"### {row['titulo']}")
                    
                    # Descripción
                    st.caption(row['descripcion'][:100] + "...")
                    
                    # Rating y ventas
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown(f"{mostrar_estrellas(row['rating'])} ({row['rating']})")
                    with col_b:
                        st.markdown(f"🛒 {row['ventas']} ventas")
                    
                    # Precio
                    st.markdown(f"<span class='price-tag'>${row['precio']:,}</span>", unsafe_allow_html=True)
                    
                    # Vendedor
                    st.caption(f"👤 Por: **{row['nombre']}**")
                    
                    # Botones de acción
                    col1, col2 = st.columns(2)
                    with col1:
                        # Botón WhatsApp
                        wsp_msg = f"Hola {row['nombre']}, me interesa: {row['titulo']}"
                        wsp_link = f"https://wa.me/{row['wsp']}?text={wsp_msg.replace(' ', '%20')}"
                        st.markdown(f"""
                        <a href="{wsp_link}" target="_blank" class="whatsapp-btn">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                            </svg>
                            WhatsApp
                        </a>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        # Botón Chat Interno
                        if st.button("💬 Chat", key=f"chat_{row['id']}", use_container_width=True):
                            st.session_state['chat_activo'] = row['creador_id']
                            st.session_state['chat_producto'] = row['titulo']
                            st.session_state['chat_vendedor'] = row['nombre']
                    
                    # Botones secundarios
                    col3, col4 = st.columns(2)
                    with col3:
                        if st.button("❤️", key=f"fav_{row['id']}", help="Agregar a favoritos"):
                            if row['id'] not in st.session_state.favoritos:
                                st.session_state.favoritos.append(row['id'])
                                st.success("¡Agregado a favoritos!")
                            else:
                                st.info("Ya está en favoritos")
                    with col4:
                        if st.button("🛒", key=f"cart_{row['id']}", help="Agregar al carrito"):
                            st.session_state.carrito.append({
                                'id': row['id'],
                                'titulo': row['titulo'],
                                'precio': row['precio'],
                                'vendedor': row['nombre']
                            })
                            st.success("¡Agregado al carrito!")
                    
                    st.divider()
    
    # Modal de Chat (simulado con expander)
    if 'chat_activo' in st.session_state and st.session_state.chat_activo:
        st.divider()
        st.subheader(f"💬 Chat con {st.session_state.get('chat_vendedor', 'Vendedor')}")
        st.caption(f"Producto: {st.session_state.get('chat_producto', '')}")
        
        # Área de mensajes
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.mensajes_chat:
                if msg['tipo'] == 'enviado':
                    st.markdown(f"<div class='chat-message sent'>👤 Tú: {msg['texto']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='chat-message received'>🏪 {msg['texto']}</div>", unsafe_allow_html=True)
        
        # Input de mensaje
        col_msg, col_btn = st.columns([4, 1])
        with col_msg:
            nuevo_mensaje = st.text_input("Escribe tu mensaje...", key="chat_input", label_visibility="collapsed")
        with col_btn:
            if st.button("📤 Enviar", use_container_width=True):
                if nuevo_mensaje:
                    st.session_state.mensajes_chat.append({
                        'tipo': 'enviado',
                        'texto': nuevo_mensaje
                    })
                    # Respuesta automática simulada
                    respuestas = [
                        "¡Hola! Gracias por tu interés. ¿En qué puedo ayudarte?",
                        "Claro, puedo darte más detalles sobre este producto.",
                        "El producto incluye actualizaciones gratuitas por 1 año.",
                        "¿Te gustaría hacer la compra ahora? Acepto transferencia o WebPay."
                    ]
                    st.session_state.mensajes_chat.append({
                        'tipo': 'recibido',
                        'texto': random.choice(respuestas)
                    })
                    st.rerun()
        
        if st.button("❌ Cerrar chat"):
            st.session_state.chat_activo = None
            st.session_state.mensajes_chat = []
            st.rerun()

# ==================== VISTA 2: FAVORITOS ====================
elif menu == "❤️ Mis Favoritos":
    st.markdown("<h1>❤️ Mis Favoritos</h1>", unsafe_allow_html=True)
    
    if not st.session_state.favoritos:
        st.info("😕 No tienes productos en favoritos. ¡Explora la vitrina y agrega algunos!")
    else:
        df_favoritos = st.session_state.contenidos[st.session_state.contenidos['id'].isin(st.session_state.favoritos)]
        
        for idx, row in df_favoritos.iterrows():
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.image(row['imagen'], width=150)
            with col2:
                st.markdown(f"### {row['titulo']}")
                st.caption(row['descripcion'])
                st.markdown(f"**${row['precio']:,}**")
            with col3:
                if st.button("🗑️ Quitar", key=f"rem_fav_{row['id']}"):
                    st.session_state.favoritos.remove(row['id'])
                    st.rerun()
                if st.button("🛒 Al carrito", key=f"fav_cart_{row['id']}"):
                    st.session_state.carrito.append({
                        'id': row['id'],
                        'titulo': row['titulo'],
                        'precio': row['precio'],
                        'vendedor': 'Vendedor'
                    })
                    st.success("¡Agregado!")
            st.divider()

# ==================== VISTA 3: CARRITO ====================
elif menu == "🛒 Mi Carrito":
    st.markdown("<h1>🛒 Mi Carrito de Compras</h1>", unsafe_allow_html=True)
    
    if not st.session_state.carrito:
        st.info("😕 Tu carrito está vacío. ¡Agrega algunos productos!")
    else:
        total = 0
        for i, item in enumerate(st.session_state.carrito):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**{item['titulo']}**")
                st.caption(f"Vendedor: {item['vendedor']}")
            with col2:
                st.markdown(f"**${item['precio']:,}**")
                total += item['precio']
            with col3:
                if st.button("🗑️", key=f"rem_cart_{i}"):
                    st.session_state.carrito.pop(i)
                    st.rerun()
            st.divider()
        
        st.markdown(f"## Total: ${total:,}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💳 Pagar con WebPay", use_container_width=True, type="primary"):
                st.success("🎉 ¡Redirigiendo a WebPay! (Simulación)")
                st.balloons()
        with col2:
            if st.button("🏦 Pagar con Transferencia", use_container_width=True):
                st.info("""
                **Datos para transferencia:**
                - Banco: Banco Estado
                - Cuenta: 12345678
                - RUT: 12.345.678-9
                - Email: pagos@ahorasi.cl
                """)
        
        if st.button("🗑️ Vaciar carrito"):
            st.session_state.carrito = []
            st.rerun()

# ==================== VISTA 4: PANEL CREADOR ====================
elif menu == "👤 Mi Panel (Creadores)":
    st.markdown("<h1>👤 Panel del Creador</h1>", unsafe_allow_html=True)
    
    usuario_actual = st.selectbox("🔄 Simular sesión como:", st.session_state.usuarios['nombre'])
    datos_user = st.session_state.usuarios[st.session_state.usuarios['nombre'] == usuario_actual].iloc[0]
    
    # Info del usuario
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=" + usuario_actual, width=150)
    with col2:
        st.markdown(f"### {datos_user['nombre']}")
        st.caption(datos_user['bio'])
        if datos_user['estado'] == "Activa":
            st.success(f"✅ Suscripción {datos_user['plan']} activa")
        else:
            st.error("❌ Suscripción inactiva")
    
    st.divider()
    
    if datos_user['estado'] == "Activa":
        # Métricas del creador
        mis_productos = st.session_state.contenidos[st.session_state.contenidos['creador_id'] == datos_user['id']]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📦 Productos", len(mis_productos))
        with col2:
            st.metric("🛒 Ventas Totales", mis_productos['ventas'].sum())
        with col3:
            ingresos = (mis_productos['ventas'] * mis_productos['precio']).sum()
            st.metric("💰 Ingresos", f"${ingresos:,}")
        with col4:
            st.metric("⭐ Rating Promedio", f"{mis_productos['rating'].mean():.1f}")
        
        st.divider()
        
        # Tabs para organizar
        tab1, tab2, tab3 = st.tabs(["📦 Mis Productos", "➕ Nuevo Producto", "📊 Estadísticas"])
        
        with tab1:
            st.subheader("Mis productos publicados")
            for idx, row in mis_productos.iterrows():
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1:
                    st.image(row['imagen'], width=100)
                with col2:
                    st.markdown(f"**{row['titulo']}**")
                    st.caption(f"${row['precio']:,} • {row['ventas']} ventas • ⭐{row['rating']}")
                with col3:
                    st.button("✏️ Editar", key=f"edit_{row['id']}")
                    st.button("🗑️ Eliminar", key=f"del_{row['id']}")
                st.divider()
        
        with tab2:
            st.subheader("➕ Publicar Nuevo Producto")
            with st.form("nuevo_producto"):
                titulo = st.text_input("📝 Título del producto")
                descripcion = st.text_area("📄 Descripción")
                precio = st.number_input("💰 Precio (CLP)", min_value=0, step=500)
                categoria = st.selectbox("🏷️ Categoría", ["Guías IA", "Cursos", "Templates", "Automatización", "Diseño", "Marketing"])
                imagen_url = st.text_input("🖼️ URL de imagen", placeholder="https://...")
                
                if st.form_submit_button("🚀 Publicar Producto", type="primary"):
                    if titulo and descripcion and precio > 0:
                        nuevo_id = st.session_state.contenidos['id'].max() + 1
                        nuevo_producto = pd.DataFrame([{
                            "id": nuevo_id, 
                            "creador_id": datos_user['id'], 
                            "titulo": titulo,
                            "descripcion": descripcion,
                            "precio": precio, 
                            "cat": categoria, 
                            "ventas": 0, 
                            "rating": 0,
                            "imagen": imagen_url if imagen_url else "https://via.placeholder.com/400"
                        }])
                        st.session_state.contenidos = pd.concat([st.session_state.contenidos, nuevo_producto], ignore_index=True)
                        st.success("✅ ¡Producto publicado exitosamente!")
                        st.balloons()
                    else:
                        st.error("Por favor completa todos los campos")
        
        with tab3:
            st.subheader("📊 Estadísticas de Ventas")
            # Gráfico simple con métricas
            st.markdown("### 📈 Rendimiento del mes")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Productos más vendidos:**")
                top_productos = mis_productos.nlargest(3, 'ventas')[['titulo', 'ventas']]
                for idx, row in top_productos.iterrows():
                    st.markdown(f"• {row['titulo']}: **{row['ventas']}** ventas")
            with col2:
                st.markdown("**Mejor valorados:**")
                top_rating = mis_productos.nlargest(3, 'rating')[['titulo', 'rating']]
                for idx, row in top_rating.iterrows():
                    st.markdown(f"• {row['titulo']}: **{row['rating']}** ⭐")
    else:
        st.error("❌ Tu suscripción está inactiva. Contacta al administrador para renovar.")
        st.markdown("""
        ### 💳 Planes disponibles:
        - **Plan Básico** - $5.000/mes: Hasta 5 productos
        - **Plan Premium** - $10.000/mes: Productos ilimitados + destacados
        """)
        if st.button("📱 Contactar para renovar (WhatsApp)", type="primary"):
            st.markdown("[Abrir WhatsApp](https://wa.me/56912345678?text=Hola,%20quiero%20renovar%20mi%20suscripción)")

# ==================== VISTA 5: ADMIN DASHBOARD ====================
elif menu == "⚙️ Admin Dashboard":
    st.markdown("<h1>⚙️ Panel de Administración</h1>", unsafe_allow_html=True)
    st.caption("Control total de la plataforma AhoraSI")
    
    # Tabs de administración
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Dashboard", "👥 Usuarios", "📦 Productos", "💰 Transacciones", "⚙️ Configuración"
    ])
    
    # TAB 1: Dashboard General
    with tab1:
        st.subheader("📊 Resumen General")
        
        # KPIs principales
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(
                "💰 Ingresos del Mes", 
                f"${st.session_state.transacciones['monto'].sum():,}",
                delta="+12%"
            )
        with col2:
            st.metric(
                "👥 Usuarios Activos",
                len(st.session_state.usuarios[st.session_state.usuarios['estado'] == 'Activa']),
                delta="+2"
            )
        with col3:
            st.metric(
                "📦 Total Productos",
                len(st.session_state.contenidos),
                delta="+5"
            )
        with col4:
            completadas = len(st.session_state.transacciones[st.session_state.transacciones['estado'] == 'Completada'])
            st.metric(
                "✅ Ventas Completadas",
                completadas,
                delta="+3"
            )
        
        st.divider()
        
        # Gráficos simulados con datos
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📈 Ventas por Categoría")
            ventas_cat = st.session_state.contenidos.groupby('cat')['ventas'].sum().sort_values(ascending=True)
            st.bar_chart(ventas_cat)
        
        with col2:
            st.markdown("### 💵 Ingresos por Método de Pago")
            ingresos_metodo = st.session_state.transacciones.groupby('metodo')['monto'].sum()
            st.bar_chart(ingresos_metodo)
        
        st.divider()
        
        # Actividad reciente
        st.markdown("### 🕐 Actividad Reciente")
        st.dataframe(
            st.session_state.transacciones.sort_values('fecha', ascending=False).head(5),
            use_container_width=True,
            hide_index=True
        )
    
    # TAB 2: Gestión de Usuarios
    with tab2:
        st.subheader("👥 Gestión de Creadores")
        
        # Barra de búsqueda y filtros
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            buscar_user = st.text_input("🔍 Buscar usuario", key="buscar_user")
        with col2:
            filtro_estado = st.selectbox("Estado", ["Todos", "Activa", "Inactiva"])
        with col3:
            filtro_plan = st.selectbox("Plan", ["Todos", "Premium", "Básico"])
        
        # Agregar nuevo usuario
        with st.expander("➕ Agregar Nuevo Creador"):
            col1, col2 = st.columns(2)
            with col1:
                nuevo_nombre = st.text_input("Nombre completo")
                nuevo_wsp = st.text_input("WhatsApp (sin +)")
                nuevo_email = st.text_input("Email")
            with col2:
                nueva_bio = st.text_area("Biografía")
                nuevo_plan = st.selectbox("Plan inicial", ["Básico", "Premium"])
            
            if st.button("✅ Crear Usuario", type="primary"):
                if nuevo_nombre and nuevo_wsp and nuevo_email:
                    nuevo_id = st.session_state.usuarios['id'].max() + 1
                    nuevo_user = pd.DataFrame([{
                        "id": nuevo_id,
                        "nombre": nuevo_nombre,
                        "wsp": nuevo_wsp,
                        "estado": "Activa",
                        "bio": nueva_bio,
                        "email": nuevo_email,
                        "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
                        "plan": nuevo_plan,
                        "ventas": 0,
                        "rating": 0
                    }])
                    st.session_state.usuarios = pd.concat([st.session_state.usuarios, nuevo_user], ignore_index=True)
                    st.success(f"✅ Usuario {nuevo_nombre} creado exitosamente")
                    st.rerun()
        
        st.divider()
        
        # Lista de usuarios
        df_users = st.session_state.usuarios.copy()
        if buscar_user:
            df_users = df_users[df_users['nombre'].str.lower().str.contains(buscar_user.lower())]
        if filtro_estado != "Todos":
            df_users = df_users[df_users['estado'] == filtro_estado]
        if filtro_plan != "Todos":
            df_users = df_users[df_users['plan'] == filtro_plan]
        
        for i, row in df_users.iterrows():
            with st.container():
                col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
                with col1:
                    st.markdown(f"**{row['nombre']}**")
                    st.caption(f"📧 {row['email']}")
                with col2:
                    estado_color = "🟢" if row['estado'] == "Activa" else "🔴"
                    st.markdown(f"{estado_color} {row['estado']}")
                with col3:
                    st.markdown(f"📋 {row['plan']}")
                with col4:
                    st.markdown(f"🛒 {row['ventas']} ventas")
                with col5:
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        if st.button("🔄", key=f"toggle_{i}", help="Cambiar estado"):
                            nuevo_estado = "Inactiva" if row['estado'] == "Activa" else "Activa"
                            st.session_state.usuarios.at[i, 'estado'] = nuevo_estado
                            st.rerun()
                    with col_b:
                        if st.button("✏️", key=f"edit_user_{i}", help="Editar"):
                            st.session_state[f'editing_user_{i}'] = True
                    with col_c:
                        wsp_link = f"https://wa.me/{row['wsp']}"
                        st.markdown(f"[📱]({wsp_link})", help="Contactar por WhatsApp")
                
                # Formulario de edición expandible
                if st.session_state.get(f'editing_user_{i}', False):
                    with st.form(f"edit_form_{i}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            edit_plan = st.selectbox("Plan", ["Básico", "Premium"], 
                                index=0 if row['plan'] == "Básico" else 1)
                        with col2:
                            edit_bio = st.text_input("Bio", value=row['bio'])
                        
                        col_save, col_cancel = st.columns(2)
                        with col_save:
                            if st.form_submit_button("💾 Guardar"):
                                st.session_state.usuarios.at[i, 'plan'] = edit_plan
                                st.session_state.usuarios.at[i, 'bio'] = edit_bio
                                st.session_state[f'editing_user_{i}'] = False
                                st.rerun()
                        with col_cancel:
                            if st.form_submit_button("❌ Cancelar"):
                                st.session_state[f'editing_user_{i}'] = False
                                st.rerun()
                
                st.divider()
    
    # TAB 3: Gestión de Productos
    with tab3:
        st.subheader("📦 Gestión de Productos")
        
        # Estadísticas rápidas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Productos", len(st.session_state.contenidos))
        with col2:
            st.metric("Productos Activos", len(st.session_state.contenidos[
                st.session_state.contenidos['creador_id'].isin(
                    st.session_state.usuarios[st.session_state.usuarios['estado'] == 'Activa']['id']
                )
            ]))
        with col3:
            st.metric("Ventas Totales", st.session_state.contenidos['ventas'].sum())
        
        st.divider()
        
        # Filtros
        col1, col2 = st.columns(2)
        with col1:
            filtro_cat_admin = st.selectbox("Filtrar por categoría", 
                ["Todas"] + list(st.session_state.contenidos['cat'].unique()))
        with col2:
            ordenar_admin = st.selectbox("Ordenar por", 
                ["Más vendidos", "Mejor rating", "Precio mayor", "Precio menor"])
        
        # Tabla de productos
        df_productos = st.session_state.contenidos.copy()
        if filtro_cat_admin != "Todas":
            df_productos = df_productos[df_productos['cat'] == filtro_cat_admin]
        
        if ordenar_admin == "Más vendidos":
            df_productos = df_productos.sort_values('ventas', ascending=False)
        elif ordenar_admin == "Mejor rating":
            df_productos = df_productos.sort_values('rating', ascending=False)
        elif ordenar_admin == "Precio mayor":
            df_productos = df_productos.sort_values('precio', ascending=False)
        else:
            df_productos = df_productos.sort_values('precio', ascending=True)
        
        # Mostrar productos editables
        edited_df = st.data_editor(
            df_productos[['titulo', 'cat', 'precio', 'ventas', 'rating']],
            use_container_width=True,
            num_rows="dynamic",
            column_config={
                "titulo": st.column_config.TextColumn("Título", width="large"),
                "cat": st.column_config.SelectboxColumn("Categoría", 
                    options=list(st.session_state.contenidos['cat'].unique())),
                "precio": st.column_config.NumberColumn("Precio", format="$%d"),
                "ventas": st.column_config.NumberColumn("Ventas"),
                "rating": st.column_config.NumberColumn("Rating", format="%.1f ⭐")
            }
        )
    
    # TAB 4: Transacciones
    with tab4:
        st.subheader("💰 Historial de Transacciones")
        
        # Métricas
        col1, col2, col3, col4 = st.columns(4)
        completadas = st.session_state.transacciones[st.session_state.transacciones['estado'] == 'Completada']
        pendientes = st.session_state.transacciones[st.session_state.transacciones['estado'] == 'Pendiente']
        
        with col1:
            st.metric("💰 Total Recaudado", f"${completadas['monto'].sum():,}")
        with col2:
            st.metric("✅ Completadas", len(completadas))
        with col3:
            st.metric("⏳ Pendientes", len(pendientes))
        with col4:
            st.metric("💵 Monto Pendiente", f"${pendientes['monto'].sum():,}")
        
        st.divider()
        
        # Filtros de transacciones
        col1, col2, col3 = st.columns(3)
        with col1:
            filtro_estado_trans = st.selectbox("Estado", ["Todas", "Completada", "Pendiente"])
        with col2:
            filtro_metodo = st.selectbox("Método de pago", ["Todos", "Transferencia", "WebPay"])
        with col3:
            buscar_comprador = st.text_input("Buscar comprador")
        
        # Aplicar filtros
        df_trans = st.session_state.transacciones.copy()
        if filtro_estado_trans != "Todas":
            df_trans = df_trans[df_trans['estado'] == filtro_estado_trans]
        if filtro_metodo != "Todos":
            df_trans = df_trans[df_trans['metodo'] == filtro_metodo]
        if buscar_comprador:
            df_trans = df_trans[df_trans['comprador'].str.lower().str.contains(buscar_comprador.lower())]
        
        # Mostrar transacciones
        for i, row in df_trans.iterrows():
            with st.container():
                col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 1])
                with col1:
                    st.markdown(f"**{row['comprador']}**")
                    st.caption(f"📅 {row['fecha']}")
                with col2:
                    producto = st.session_state.contenidos[st.session_state.contenidos['id'] == row['producto_id']]
                    if len(producto) > 0:
                        st.markdown(f"📦 {producto.iloc[0]['titulo'][:30]}...")
                with col3:
                    st.markdown(f"**${row['monto']:,}**")
                with col4:
                    estado_emoji = "✅" if row['estado'] == "Completada" else "⏳"
                    st.markdown(f"{estado_emoji} {row['estado']}")
                with col5:
                    if row['estado'] == "Pendiente":
                        if st.button("✅ Confirmar", key=f"conf_{i}"):
                            st.session_state.transacciones.at[i, 'estado'] = "Completada"
                            st.success("¡Transacción confirmada!")
                            st.rerun()
                st.divider()
        
        # Exportar datos
        if st.button("📥 Exportar a CSV"):
            csv = st.session_state.transacciones.to_csv(index=False)
            st.download_button(
                "💾 Descargar CSV",
                csv,
                "transacciones.csv",
                "text/csv"
            )
    
    # TAB 5: Configuración
    with tab5:
        st.subheader("⚙️ Configuración de la Plataforma")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💳 Configuración de Pagos")
            st.text_input("Cuenta bancaria", value="12345678", key="cuenta_banco")
            st.text_input("RUT empresa", value="12.345.678-9", key="rut_empresa")
            st.text_input("Email de notificaciones", value="pagos@ahorasi.cl", key="email_pagos")
            st.number_input("Comisión plataforma (%)", value=10, min_value=0, max_value=50, key="comision")
        
        with col2:
            st.markdown("### 📱 Configuración WhatsApp")
            st.text_input("Número principal", value="56912345678", key="wsp_principal")
            st.text_area("Mensaje de bienvenida", 
                value="¡Hola! Gracias por contactar a AhoraSI Marketplace. ¿En qué podemos ayudarte?",
                key="msg_bienvenida")
        
        st.divider()
        
        st.markdown("### 🎨 Personalización")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.color_picker("Color primario", value="#667eea", key="color_primario")
        with col2:
            st.color_picker("Color secundario", value="#764ba2", key="color_secundario")
        with col3:
            st.color_picker("Color de acento", value="#25D366", key="color_acento")
        
        st.divider()
        
        st.markdown("### 📧 Plantillas de Email")
        plantilla = st.selectbox("Seleccionar plantilla", 
            ["Bienvenida nuevo usuario", "Confirmación de pago", "Suscripción por vencer", "Recordatorio de pago"])
        st.text_area("Contenido de la plantilla", 
            value="Estimado {nombre},\n\nGracias por ser parte de AhoraSI Marketplace...",
            height=150)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Guardar Configuración", type="primary", use_container_width=True):
                st.success("✅ Configuración guardada exitosamente")
        with col2:
            if st.button("🔄 Restaurar valores por defecto", use_container_width=True):
                st.info("Valores restaurados")
        
        st.divider()
        
        # Herramientas de mantenimiento
        st.markdown("### 🛠️ Herramientas de Mantenimiento")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🗑️ Limpiar caché", use_container_width=True):
                st.cache_data.clear()
                st.success("Caché limpiado")
        with col2:
            if st.button("📊 Generar reporte", use_container_width=True):
                st.info("Generando reporte...")
        with col3:
            if st.button("🔒 Backup de datos", use_container_width=True):
                st.success("Backup creado: backup_2024-03-15.json")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>🚀 <strong>AhoraSI Marketplace</strong> v2.0</p>
    <p>Creado con ❤️ en Chile | © 2024</p>
</div>
""", unsafe_allow_html=True)
