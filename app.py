import streamlit as st

start_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
about_page = st.Page("pages/about.py", title="About", icon=":material/info:")
projektarbeit_page = st.Page("pages/f1_start.py", title="Projektbeschreibung", icon=":material/sports_motorsports:")

pg = st.navigation(
    {
        "Home": [start_page, about_page], #projektarbeit_page, logout_page
        "Projekt Formel 1": [projektarbeit_page],
    }
)

pg.run()