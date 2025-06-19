import streamlit as st

st.set_page_config(page_title="Страница не найдена", page_icon="⚠️")
st.title("⚠️ 404")
st.error("Извините, запрошенная страница не существует.")

# ➜ аргумент page должен идти первым, label — вторым/ключевым
st.page_link("Home", label="🏠 Вернуться на главную")

