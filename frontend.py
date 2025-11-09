import streamlit as st
import requests

st.set_page_config(page_title="Todo App", page_icon="📝", layout="centered")
st.title("📝 Todo App AKS")
st.caption("A minimal Streamlit UI connected to your FastAPI backend")

# ✅ Use the service name (todo-service) instead of localhost
API_URL = "http://todo-service.default.svc.cluster.local"

# Add a new todo
todo = st.text_input("Enter a new task:")
if st.button("Add Todo"):
    if todo:
        try:
            res = requests.post(f"{API_URL}/todos", json={"task": todo})
            if res.status_code == 200:
                st.success(f"✅ Task added: {todo}")
            else:
                st.error("❌ Failed to add task. Check backend.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a task.")

# View todos
if st.button("Refresh Todos"):
    try:
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
    except Exception as e:
        st.error(f"Error: {e}")
