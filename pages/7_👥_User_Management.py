import streamlit as st

# Проверка роли
user = st.session_state.get("current_user")
if not user or user["role"] not in ("admin", "employee"):
    st.error("Доступ разрешён только сотрудникам клиники.")
    st.stop()

st.title("👥 Управление пользователями")

users = st.session_state.users
cols = st.columns((2, 1, 1))
cols[0].write("**Логин**")
cols[1].write("**Роль**")
cols[2].write("**✖**")

for login, data in users.items():
    cols = st.columns((2, 1, 1))
    cols[0].write(login)
    cols[1].write(data["role"])
    if login not in ("admin", "employee"):  # базовых удалить нельзя
        if cols[2].button("Удалить", key=f"del_{login}"):
            del users[login]
            st.experimental_rerun()

st.markdown("---")
st.subheader("➕ Создать нового пользователя")

with st.form("create_user", clear_on_submit=True):
    new_login = st.text_input("Логин")
    new_pwd   = st.text_input("Пароль", type="password")
    new_role  = st.selectbox("Роль", ("user", "employee"))
    ok        = st.form_submit_button("Создать")

if ok:
    if new_login in users:
        st.warning("Такой логин уже существует.")
    else:
        users[new_login] = {"password": new_pwd, "role": new_role}
        st.success("Пользователь добавлен.")
