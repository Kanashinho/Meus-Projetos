import streamlit as st
import dados

st.title('Animes')

nome = st.text_input('Nome de Anime')
ano = st.number_input('Ano do Anime', min_value=1970, max_value=2025)
nota = st.slider('Nota do Anime', min_value= 0.0, max_value= 10.0)

if st.button('Adicionar'):
    dados.insere_dados(nome, ano , nota)
    st.success('Anime Cadastrado')

animes = dados.listar_dados()
st.header("Lista de animes")
st.table(animes)