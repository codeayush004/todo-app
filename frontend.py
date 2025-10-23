# frontend.py
import streamlit as st
import requests

st.set_page_config(page_title="Todo App", page_icon="📝", layout="centered")

st.title("📝 Todo App sUUUU")
st.caption("A minimal Streamlit UI connected to your FastAPI backend")

# 🧠 Replace this with your backend’s public IP if running remotely
API_URL = "http://85.211.157.90"

# Add a new todo
todo = st.text_input("Enter a new task:")
if st.button("Add Todo"):
    if todo:
        res = requests.post(f"{API_URL}/todos", json={"task": todo})
        if res.status_code == 200:
            st.success(f"✅ Task added: {todo}")
        else:
            st.error("❌ Failed to add task. Check backend.")
    else:
        st.warning("Please enter a task.")

# View todos
if st.button("Refresh Todos"):
    res = requests.get(f"{API_URL}/todos")
    if res.status_code == 200:
        todos = res.json()
        if todos:
            st.subheader("📋 Your Todos:")
            for t in todos:
                st.write(f"- {t['task']}")
        else:
            st.info("No todos yet. Add one above!")
    else:
        st.error("Failed to fetch todos.")
