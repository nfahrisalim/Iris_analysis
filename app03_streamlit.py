import io
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from hdfs import InsecureClient
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Iris Analyzer", page_icon="🌸", layout="wide")

@st.cache_data
def load_data():
    # client = InsecureClient('http://localhost:9870')
    # with client.read('/Iris.csv', encoding='utf-8') as reader:
    #     df = pd.read_csv(reader)
    # Pakai ini saja kalau mau lewat Hadoop
    df = pd.read_csv('Iris.csv')
    return df


# Load
df = load_data()
species_list = df['Species'].unique()

with st.sidebar:
    selected = option_menu(
        "Iriz Analyzer",
        ["Beranda", "Data", "Statistik", "Visualisasi", "Korelasi", "Tentang"],
        icons=["house", "table", "graph-up", "bar-chart", "activity", "info-circle"],
        menu_icon="flower2",
        default_index=0
    )
    st.markdown("---")
    selected_species = st.multiselect("🔎 Filter Species", species_list, default=species_list)

filtered_df = df[df['Species'].isin(selected_species)]

if selected == "Beranda":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Aplikasi Analisis Data iris")
        st.write(
            """
            Dataset Iris adalah salah satu dataset klasik dalam dunia pembelajaran mesin.
            Aplikasi ini menyediakan fitur eksplorasi dan visualisasi interaktif terhadap dataset tersebut.
            """
        )
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", use_container_width=True)

elif selected == "Data":
    st.header("Tabel Data")
    with st.expander("Lihat Dataframe"):
        st.dataframe(filtered_df, use_container_width=True)

    with st.expander("Ringkasan Info"):
        buffer = io.StringIO()
        filtered_df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    search_name = st.text_input("🔎 Cari berdasarkan nama species:")
    if search_name:
        result = df[df['species'].str.contains(search_name, case=False)]
        st.dataframe(result)

elif selected == "Statistik":
    st.header("Statistik Data")

    st.subheader("Statistik Deskriptif")
    st.dataframe(filtered_df.describe(), use_container_width=True)

    st.subheader("Statistik Spesifik")
    feature = st.selectbox("Pilih kolom numerik", df.columns[:-1])
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("📉 Min", float(filtered_df[feature].min()))
        st.metric("📈 Max", float(filtered_df[feature].max()))
    with col2:
        st.metric("📊 Mean", float(filtered_df[feature].mean()))
        st.metric("📏 Std", float(filtered_df[feature].std()))

elif selected == "Visualisasi":
    st.header("Visualisasi Data")

    tabs = st.tabs(["Histogram", "Boxplot", "Scatter Matrix", "Plotly 3D"])

    with tabs[0]:
        st.subheader("Distribusi Histogram")
        col = st.selectbox("Pilih Fitur", df.columns[:-1])
        fig, ax = plt.subplots()
        sns.histplot(filtered_df[col], kde=True, ax=ax)
        st.pyplot(fig)

    with tabs[1]:
        st.subheader("Boxplot per Species")
        col = st.selectbox("Fitur untuk Boxplot", df.columns[:-1], key="box")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x='species', y=col, data=filtered_df, ax=ax2)
        st.pyplot(fig2)

    with tabs[2]:
        st.subheader("Pairplot Matrix")
        fig3 = sns.pairplot(filtered_df, hue='species')
        st.pyplot(fig3)
    
    with tabs[3]:
        st.subheader("3D Scatter Plot (Plotly)")
        fig4 = px.scatter_3d(filtered_df, x='sepal_length', y='sepal_width', z='petal_length',
                            color='species', size='petal_width', title='3D Plot of Iris Dataset', template='plotly_white')
        st.plotly_chart(fig4, use_container_width=True)

elif selected == "Korelasi":
    st.header("Korelasi Antar-fitur")
    corr = filtered_df.iloc[:, :-1].corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

elif selected == "Tentang":
    st.title("👨‍💻 Tentang Dashboard Ini")
    st.markdown(
        """
        **Dibuat oleh**: [Naufal](https://github.com/nfahrisalim)  
        **Framework**: [Streamlit](https://streamlit.io/)  
        **Dataset**: [Iris – UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/iris)

        Aplikasi ini merupakan demo **analisis data interaktif** menggunakan Python dan Streamlit,  
        dengan dataset `Iris.csv` yang disimpan di sistem HDFS.  
        
        Anda dapat menjelajahi data, menampilkan statistik deskriptif, visualisasi interaktif, dan korelasi antar fitur.
        """
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", caption="Iris versicolor", use_container_width=True)
