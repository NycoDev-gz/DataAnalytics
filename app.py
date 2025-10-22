import streamlit as st
import os
from dotenv import load_dotenv
from index import leerdoc, calcular_promedio

#Cargar entorno
load_dotenv()
DATA_PATH = os.getenv("data_path")

# 2️⃣ inicializa estado de la pagina
st.session_state.setdefault("page", "home")

# 3️⃣ Definir páginas válidas
VALID_PAGES = ["home", "tabla", "barras", "estadisticas"]

# 4️⃣ Cargar los datos una sola vez
@st.cache_data
def cargar_datos(path):
    try:
        return leerdoc(path)
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        return None

doc = cargar_datos(DATA_PATH)

# 5️⃣ Sidebar
st.sidebar.title("📚 Navegación")
st.sidebar.write("Página actual:", st.session_state.page)

# El selectbox actualiza st.session_state.page automáticamente
st.sidebar.selectbox(
    "Ir a:",
    VALID_PAGES,
    key="page",
)

# 6️⃣ Contenido principal según página
if st.session_state.page == "home":
    st.title("🏠 Bienvenido")
    if doc is not None:
        st.success("Datos cargados correctamente.")
        st.write("Usa el menú lateral para navegar entre vistas.")
    else:
        st.warning("No se pudo cargar el archivo. Verifica la ruta en .env")

elif st.session_state.page == "tabla":
    st.title("📊 Vista de Tabla")
    if doc is not None:
        st.dataframe(doc)
    else:
        st.warning("No hay datos cargados.")

elif st.session_state.page == "barras":
    st.title("📈 Gráficos de barras")
    if doc is not None:
        # Aquí podrías poner tus visualizaciones
        st.write("Próximamente: gráfico de barras...")
    else:
        st.warning("No hay datos cargados.")

elif st.session_state.page == "estadisticas":
    st.title("📉 Estadísticas")
    if doc is not None:
        colpromedio = st.selectbox("Selecciona la columna para calcular el promedio:", doc.columns)
        promedio = calcular_promedio(doc, colpromedio)
        st.write("Promedio:", promedio)
    else:
        st.warning("No hay datos cargados.")
