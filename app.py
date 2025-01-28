import streamlit as st

#st.title("Web App für Technik")

start_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
about_page = st.Page("pages/about.py", title="About", icon=":material/info:")

pg = st.navigation(
    {
        "Home": [start_page, about_page], #projektarbeit_page, logout_page
        "Projekt Formel 1": [],
    }
)

pg.run()