import streamlit as st

st.title("✉️ Обратная связь")

st.write("Заполните форму, и мы свяжемся с вами в ближайшее время.")

with st.form("msg_form", clear_on_submit=True):
    name  = st.text_input("Ваше имя")
    email = st.text_input("Email")
    text  = st.text_area("Сообщение")
    sent  = st.form_submit_button("Отправить")

if sent:
    st.session_state.messages.append(
        {"from": name, "email": email, "text": text}
    )
    st.success("Сообщение отправлено! Спасибо за обращение.")

st.header("Контакты")
st.write("""
**Адрес:** г. Amsterdam, Vetstraat 5  
**Тел.:** +31 20 123 45 67  
**Email:** info@vetcare.nl  
**Часы работы:** 08:00-22:00 ежедневно
""")
