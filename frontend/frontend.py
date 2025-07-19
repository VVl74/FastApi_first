import streamlit as st
import requests

# Настройки
BACKEND_URL = "http://localhost:8000"  # URL вашего FastAPI-бэкенда
st.title("FastAPI Frontend на Python")

# 1. Эндпоинт: GET /
st.header("Главная страница")
if st.button("Вызвать GET /"):
    try:
        response = requests.get(f"{BACKEND_URL}/")
        st.code(f"234: {response.text}324123", language="text")
    except Exception as e:
        st.error(f"Ошибка: {e}")

# 2. Эндпоинт: GET /health
st.header("Health Check")
if st.button("Вызвать GET /health"):
    try:
        response = requests.get(f"{BACKEND_URL}/health")
        st.json(response.json())
    except Exception as e:
        st.error(f"Ошибка: {e}")

# 3. Эндпоинт: GET /echo/{text}
st.header("Echo Service")
text_input = st.text_input("Введите текст", "Привет")
if st.button("Вызвать GET /echo/{text}"):
    try:
        response = requests.get(f"{BACKEND_URL}/echo/{text_input}")
        st.json(response.json())
    except Exception as e:
        st.error(f"Ошибка: {e}")