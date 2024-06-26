import streamlit as st
import requests
from config import API_URL, GIT_INFO

st.set_page_config(
    page_title="InnoTrackify",
    menu_items={
        "About": GIT_INFO,
    },
)


def register(username, email, password):
    url = f"{API_URL}/users/"
    data = {
        "grant_type": "",
        "scope": "",
        "client_id": "",
        "client_secret": "",
        "username": username,
        "email": email,
        "password": password,
    }
    response = requests.post(url, json=data)
    return response.json()


def login(username, password):
    url = f"{API_URL}/login"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()


if "session_token" not in st.session_state:
    st.session_state["session_token"] = None

if "user_id" not in st.session_state:
    st.session_state["user_id"] = None

choice = st.selectbox("Login/Signup", ["Sign-up", "Login"])

if choice == "Login":
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        response = login(username, password)
        if "access_token" in response:
            print(response)
            session_token = response["access_token"]
            st.session_state["session_token"] = session_token
            st.session_state["user_id"] = response["client_id"]

            # Redirect to another page or perform other actions
            st.success("Login success. Now you can access other pages.")
        else:
            st.error(response["detail"])
else:
    username = st.text_input("Username:")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    if st.button("Sign up"):
        response = register(username, email, password)

        if "id" in response:
            st.success("You're officially registered. Go to login page.")
        else:
            st.error(response["detail"])
