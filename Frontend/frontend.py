import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Todo App", layout="wide")

# -------------------------
# SESSION STATE
# -------------------------
if "token" not in st.session_state:
    st.session_state.token = None

if "username" not in st.session_state:
    st.session_state.username = None


# -------------------------
# HELPER FUNCTIONS
# -------------------------
def get_headers():
    return {"Authorization": f"Bearer {st.session_state.token}"}


def login_user(username, password):
    data = {
        "username": username,
        "password": password,
    }

    return requests.post(
        f"{BASE_URL}/Auth/login",
        data=data
    )


def register_user(username, password):
    payload = {
        "username": username,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/Auth/register", json=payload)


# -------------------------
# AUTH SECTION
# -------------------------
if st.session_state.token is None:

    st.title("🔐 Todo App - Login / Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            res = login_user(username, password)

            if res.status_code == 200:
                token_data = res.json()
                st.session_state.token = token_data["access_token"]
                st.success("Login Successful ✅")
                st.rerun()
            else:
                st.error(res.json()["detail"])

    with tab2:
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")

        if st.button("Register"):
            res = register_user(new_username, new_password)

            if res.status_code == 200:
                st.success("User registered successfully 🎉")
            else:
                st.error(res.json()["detail"])

# -------------------------
# MAIN DASHBOARD
# -------------------------
else:
    st.sidebar.title("📌 Navigation")
    menu = st.sidebar.radio(
        "Choose Option",
        [
            "Create Task",
            "Get Task By ID",
            "Update Task",
            "Delete Task",
            "View All (Admin)"
        ]
    )

    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.rerun()

    st.title("📝 Todo Dashboard")

    # -------------------------
    # CREATE TASK
    # -------------------------
    if menu == "Create Task":
        st.subheader("Create New Task")

        task = st.text_input("Task Title")
        description = st.text_area("Task Description")

        if st.button("Create"):
            payload = {
                "Task": task,
                "Description": description
            }

            res = requests.post(
                f"{BASE_URL}/CRUD/v1/Create",
                json=payload,
                headers=get_headers()
            )

            if res.status_code == 200:
                st.success("Task Created Successfully ✅")
                st.json(res.json())
            else:
                st.error(res.text)

    # -------------------------
    # GET TASK BY ID
    # -------------------------
    elif menu == "Get Task By ID":
        st.subheader("Get Task By ID")

        task_id = st.number_input("Enter Task ID", min_value=1)

        if st.button("Fetch Task"):
            res = requests.get(
                f"{BASE_URL}/CRUD/v1/task/{task_id}",
                headers=get_headers()
            )

            if res.status_code == 200:
                st.success("Task Found ✅")
                st.json(res.json())
            else:
                st.error(res.json()["detail"])

    # -------------------------
    # UPDATED PATCH ENDPOINT
    # -------------------------
    elif menu == "Update Task":
        st.subheader("Update Task (Partial Update - PATCH)")

        task_id = st.number_input("Task ID", min_value=1)

        new_title = st.text_input("New Title (leave empty to keep same)")
        new_description = st.text_area("New Description (leave empty to keep same)")

        if st.button("Update Task"):
            payload = {}

            # Only send fields if user filled them
            if new_title.strip():
                payload["title"] = new_title

            if new_description.strip():
                payload["description"] = new_description

            if not payload:
                st.warning("Please provide at least one field to update.")
            else:
                res = requests.patch(
                    f"{BASE_URL}/CRUD/v1/tasks/{task_id}",
                    json=payload,
                    headers=get_headers()
                )

                if res.status_code == 200:
                    st.success("Task Updated Successfully ✅")
                    st.json(res.json())
                else:
                    st.error(res.text)

    # -------------------------
    # DELETE TASK
    # -------------------------
    elif menu == "Delete Task":
        st.subheader("Delete Task")

        task_id = st.number_input("Task ID to Delete", min_value=1)

        if st.button("Delete"):
            res = requests.delete(
                f"{BASE_URL}/CRUD/v1/{task_id}",
                headers=get_headers()
            )

            if res.status_code == 200:
                st.success("Deleted Successfully 🗑️")
            else:
                st.error(res.text)

    # -------------------------
    # ADMIN VIEW
    # -------------------------
    elif menu == "View All (Admin)":
        st.subheader("Admin: View All Tasks")

        res = requests.get(
            f"{BASE_URL}/CRUD/v1/tasks",
            headers=get_headers()
        )

        if res.status_code == 200:
            st.success("Tasks Loaded ✅")
            st.json(res.json())
        else:
            st.error(res.text)
