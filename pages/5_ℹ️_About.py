import streamlit as st

st.title("ℹ️ О клинике")

st.write(
    """
    **VetCare Clinic** основана в 2005 году командой ветеринарных врачей-энтузиастов.
    Наш приоритет — доказательная медицина и этичное отношение к животным.
    """
)

st.image(
    "https://plus.unsplash.com/premium_photo-1677165327781-1c0b7c458821?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D=crop&w=600&q=40",
    caption="Наша команда",
    use_container_width=True,
)

st.header("Наши принципы")
principles = [
    "✅ Индивидуальный подход к каждому пациенту",
    "✅ Современные протоколы лечения",
    "✅ Прозрачное ценообразование",
    "✅ Поддержка владельцев 24/7",
]
for p in principles:
    st.write(p)
