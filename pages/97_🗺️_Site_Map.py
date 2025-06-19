import streamlit as st

st.title("🗺️ Карта сайта")

pages = {
    "🏠 Главная":             "Home",
    "🛠️ Услуги":             "Services",
    "📚 Статьи":             "Articles",
    "📰 Новости":            "News",
    "ℹ️ О клинике":          "About",
    "✉️ Контакты":           "Contact",
    "👥 Управление":         "User_Management (для сотрудников)",
    "⚠️ 404":                "404",
}

for label, page in pages.items():
    st.markdown(f"- [{label}](/?page={page})")
