import streamlit as st
from datetime import date

st.title("📰 Новости клиники")

news = [
    (date(2025, 6, 1),  "Открыт филиал в Северном районе"),
    (date(2025, 5, 20), "Закуплено новое УЗ-оборудование эксперт-класса"),
    (date(2025, 5, 5),  "Акция: бесплатная консультация терапевта в июне"),
    (date(2025, 4, 15), "Врачи клиники прошли международную сертификацию ISFM"),
    (date(2025, 3, 30), "Мы приняли 10 000-го пациента!"),
]

for dt, text in news:
    st.subheader(dt.strftime("%d.%m.%Y"))
    st.write(text)
    st.markdown("---")
