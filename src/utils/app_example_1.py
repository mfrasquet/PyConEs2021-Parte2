import billboard
import streamlit as st
from sentence_transformers import SentenceTransformer

from utils.similarity import visualize_similarity

# Sidebar settings

model_name = st.sidebar.text_input("Pon el modelo que quieres usar", "all-MiniLM-L12-v2")

valid_billboards = ["hot-100",
                    "streaming-songs",
                    "radio-songs",
                    "current-albums",
                    "soundtracks",
                    "summer-songs",
                    "billboard-global-excl-us",
                    "greatest-billboard-200-albums",
                    "greatest-hot-100-singles",
                    "greatest-hot-100-songs-by-women",
                    "greatest-billboard-200-albums-by-women",
                    "greatest-of-all-time-songs-of-the-summer",
                    "greatest-of-all-time-pop-songs"
]

chart_name = st.sidebar.selectbox(
    "Selecciona la lista que quieres usar", valid_billboards
)

sim_threshold = st.sidebar.slider(
    "Selecciona el valor mínimo de similitud",
    min_value=0.0,
    max_value=0.95,
    value=0.5,
    step=0.05,
)

# Main

chart = billboard.ChartData(chart_name)
model = SentenceTransformer(model_name)

sentences = [entry.title for entry in chart.entries]

embeddings = model.encode(sentences)

vis = visualize_similarity(
    embeddings_1=embeddings,
    embeddings_2=embeddings,
    labels_1=sentences,
    labels_2=sentences,
    plot_title="Matriz de similitud",
    threshold=sim_threshold,
)

try:
    st.bokeh_chart(vis, use_container_width=True)
except:
    st.write("No se pudo mostrar la matriz de similitud, prueba con un threshold más bajo")
