import streamlit as st

st.set_page_config(page_title="Formulario")
st.title("What's your problem?")

st.sidebar.header("Formulário de reclamações")


d = {}
with st.form("Formulário de reclamação:"):
    a, b = st.columns(2)
    d['nome'] = a.text_input('Nome:')
    d['sobrenome'] = b.text_input('Sobrenome:')

    d['email'] = st.text_input('E-mail: ')
    d['endereco'] = st.text_input('Endereço')

    d['comentário'] = st.text_area('Um comentário: ')

    st.form_submit_button('Enviar')