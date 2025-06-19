import streamlit as st
from pathlib import Path

# Импортируем модуль cli из web под именем stcli
from streamlit.web import cli as stcli
import sys
from streamlit import runtime

# Проверяем существование runtime
runtime.exists()


def main():
    # ─────────────────────────────  НАСТРОЙКИ ПРИЛОЖЕНИЯ  ────────────────────────────
    st.set_page_config(
        page_title="VetCare Clinic",
        page_icon="🐾",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # ────────────────────────────  ИНИЦИАЛИЗАЦИЯ SESSION  ────────────────────────────
    if "style" not in st.session_state:
        st.session_state.style = "Стандартный"

    if "users" not in st.session_state:
        # username: {password, role}
        st.session_state.users = {
            "admin":    {"password": "admin",    "role": "admin"},
            "employee": {"password": "employee", "role": "employee"},
            "guest":    {"password": "guest",    "role": "user"},
        }

    if "current_user" not in st.session_state:
        st.session_state.current_user = None  # {'username': str, 'role': str}

    if "messages" not in st.session_state:
        st.session_state.messages = []  # список словарей {from, email, text}

    # ───────────────────────────────  ЗАГРУЗКА СТИЛЕЙ  ──────────────────────────────
    def load_css():
        style_file = (
            "accessible.css"
            if st.session_state.style == "Для слабовидящих"
            else "style.css"
        )
        css_path = Path("static") / style_file
        with css_path.open(encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # ───────────────────────────  АУТЕНТИФИКАЦИЯ/АВТОРИЗАЦИЯ  ────────────────────────
    def login_block():
        st.sidebar.subheader("🔐 Авторизация")
        if st.session_state.current_user:
            u = st.session_state.current_user
            st.sidebar.success(f"Вы вошли как **{u['username']}** ({u['role']})")
            if st.sidebar.button("Выйти"):
                st.session_state.current_user = None
                st.rerun()
        else:
            with st.sidebar.form("login_form", clear_on_submit=False):
                login = st.text_input("Логин")
                pwd = st.text_input("Пароль", type="password")
                ok = st.form_submit_button("Войти")
            if ok:
                users = st.session_state.users
                if login in users and users[login]["password"] == pwd:
                    st.session_state.current_user = {
                        "username": login,
                        "role": users[login]["role"],
                    }
                    st.sidebar.success("Успешный вход")
                    st.rerun()
                else:
                    st.sidebar.error("Неверный логин или пароль")

    def register_block():
        st.sidebar.subheader("🆕 Регистрация")
        with st.sidebar.expander("Создать личный аккаунт"):
            with st.form("reg_form", clear_on_submit=True):
                new_login = st.text_input("Логин", key="reg_login")
                new_pwd = st.text_input("Пароль", key="reg_pwd", type="password")
                new_role = "user"
                sent = st.form_submit_button("Зарегистрироваться")
            if sent:
                if new_login in st.session_state.users:
                    st.warning("Такой логин уже существует")
                else:
                    st.session_state.users[new_login] = {
                        "password": new_pwd,
                        "role": new_role,
                    }
                    st.success("Аккаунт создан")

    # ────────────────────────────────  404 РЕДИРЕКТ  ────────────────────────────────
    _valid_pages = {
        "Home",
        "Services",
        "Articles",
        "News",
        "About",
        "Contact",
        "User_Management",
    }

    def redirect_unknown():
        # st.query_params — это объект-прокси (dict-like), его не вызываем
        qp = st.query_params
        if "page" in qp:
            label = qp["page"][0].replace("_", " ").split("/")[0]
            if label not in _valid_pages:
                # если пользователь вручную изменил URL
                st.switch_page("pages/99_⚠️_404.py")

    # ─────────────────────────────────  САЙДБАР  ─────────────────────────────────────
    with st.sidebar:
        style_choice = st.radio("🎨 Стилизация", ("Стандартный", "Для слабовидящих"))
        st.session_state.style = style_choice
        load_css()
        login_block()
        register_block()
        st.markdown("---")
        st.caption("© 2025 VetCare Clinic")

    # ───────────────────────────────  ЗАПУСК REDIRECT  ──────────────────────────────
    redirect_unknown()


# Если скрипт запускается напрямую
if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
