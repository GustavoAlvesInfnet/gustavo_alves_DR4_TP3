import json
import streamlit as st
import matplotlib.pyplot as plt

with open('.\\data\\noticias.json') as f:
    noticias = json.load(f)

noticias_lista = []
for noticia in noticias['noticias']:
    noticias_lista.append({
        'categoria': noticia['categoria'],
        'subcategoria': noticia['subcategoria'],
        'sentimento': noticia['sentimento']
    })

categorias_contagem = {}
for noticia in noticias_lista:
    categoria = noticia['categoria']
    subcategoria = noticia['subcategoria']
    if categoria not in categorias_contagem:
        categorias_contagem[categoria] = {}
    if subcategoria not in categorias_contagem[categoria]:
        categorias_contagem[categoria][subcategoria] = 0
    categorias_contagem[categoria][subcategoria] += 1

categorias_proporcao = {}
for categoria, subcategorias in categorias_contagem.items():
    total = sum(subcategorias.values())
    categorias_proporcao[categoria] = {subcategoria: contagem / total for subcategoria, contagem in subcategorias.items()}

st.title("Análise de Sentimento de Notícias")

categorias = list(categorias_proporcao.keys())
proporcoes = [sum(categorias_proporcao[categoria].values()) for categoria in categorias]

fig, ax = plt.subplots()
ax.pie(proporcoes, labels=categorias, autopct='%1.1f%%')
ax.axis('equal')

st.pyplot(fig)
