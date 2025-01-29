import streamlit as st

st.set_page_config(layout="wide")

# Home
start_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
about_page = st.Page("pages/about.py", title="About", icon=":material/info:")
download_page = st.Page("pages/download_page.py", title="Downloads", icon=":material/download:")

# Projekt Formel 1
projektarbeit_page = st.Page("pages/f1_start.py", title="Projektbeschreibung")
drivers_page = st.Page("pages/drivers.py", title="Fahrer", icon=":material/sports_motorsports:")

pg = st.navigation(
    {
        "Home": [start_page, about_page, download_page], #projektarbeit_page, logout_page
        "Projekt Formel 1": [projektarbeit_page, drivers_page],
    }
)

pg.run()