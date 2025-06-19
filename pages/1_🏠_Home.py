import streamlit as st

st.title("🐾 VetCare Clinic")
st.image(
    "https://plus.unsplash.com/premium_photo-1677165327781-1c0b7c458821?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D=crop&w=600&q=40",
    use_container_width=True,
)
st.header("Добро пожаловать!")
st.write(
    """
    **VetCare Clinic** — современная ветеринарная клиника, где забота
    о здоровье вашего питомца стоит на первом месте.  
    Мы предлагаем широкий перечень услуг:
    профилактика, диагностика, хирургия, груминг
    и стационар круглосуточно.
    """
)

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.metric("20 +", "лет опыта")
    col2.metric("15 000 +", "успешных лечений")
    col3.metric("95 %", "клиентов приходят по рекомендации")
