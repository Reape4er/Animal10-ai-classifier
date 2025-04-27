import streamlit as st
import requests

# Адрес твоего FastAPI сервера
FASTAPI_URL = "http://18.156.158.53:10000/predict"  # <-- измени на адрес своего сервера, если нужно

st.title("Классификация изображений")

uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Отображение загруженного изображения
    st.image(uploaded_file, caption="Загруженное изображение", use_column_width=True)

    # Кнопка отправки на сервер
    if st.button("Классифицировать"):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(FASTAPI_URL, files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Предсказанный класс: **{result['predicted_class']}**")
            st.info(f"Уверенность модели: **{result['confidence']:.2f}**")
        else:
            st.error("Ошибка при запросе к серверу. Проверьте его работу.")
