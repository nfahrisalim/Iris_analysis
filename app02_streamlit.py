import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from hdfs import InsecureClient

@st.cache_data
def load_data():
    client = InsecureClient('http://localhost:9870')
    with client.read('/Iris.csv', encoding='utf-8') as reader:
        df = pd.read_csv(reader)
    return df

# Load
df = load_data()
species_list = df['Species'].unique()

# Sidebar
st.sidebar.title("☘️ Iris Data Analyzer 🌸")
menu = st.sidebar.radio("Pilih Menu:", ["Beranda", "Statistik", "Visualisasi", "Tentang"])

st.sidebar.markdown("---")
selected_species = st.sidebar.multiselect("Filter Species", species_list, default=species_list)
filtered_df = df[df['Species'].isin(selected_species)]

if menu == "Beranda":
    st.title("Aplikasi Analisis Data Iris")
    st.markdown(
        """
        Dataset **Iris** adalah salah satu dataset klasik dalam dunia pembelajaran mesin.
        Aplikasi ini menyediakan fitur eksplorasi dan visualisasi interaktif terhadap dataset tersebut.
        """
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", width=300)

elif menu == "Statistik":
    st.header("📊 Statistik Deskriptif")
    st.dataframe(filtered_df.describe())

    if st.button("Tampilkan 5 Data Teratas"):
        if selected_species == []:
            st.markdown("Pilih minimal satu species terlebih dahulu")
        else:
            for species in selected_species:
                st.subheader(f"Lima Data Teratas untuk: {species}")
                st.dataframe(filtered_df[filtered_df['Species'] == species].head())

elif menu == "Visualisasi":
    st.header("📈 Visualisasi Data")

    st.subheader("Pairplot")
    fig1 = sns.pairplot(filtered_df, hue='Species', diag_kind='hist')
    st.pyplot(fig1)

    st.subheader("Boxplot")
    col = st.selectbox("Pilih Kolom Fitur", df.columns[1:-1])  # excluding 'Id' and 'Species'
    fig2, ax = plt.subplots()
    sns.boxplot(x='Species', y=col, data=filtered_df, ax=ax)
    st.pyplot(fig2)

elif menu == "Tentang":
    st.title("👨‍💻 Tentang Dashboard Ini")
    st.markdown(
        """
        Dibuat oleh: Naufal | Framework: [Streamlit](https://streamlit.io/) | Dataset: [Iris UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/iris)

        Aplikasi ini dibuat sebagai demo analisis interaktif menggunakan Python dan Streamlit
        dengan dataset Iris.csv yang berada di HDFS
        """
    )
