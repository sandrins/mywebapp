import streamlit as st

st.title("Web App für Technik")

start_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)

pg = st.navigation(
        {
            "Home": [start_page], #about_page, projektarbeit_page, logout_page
            #"Die Formel 1": [formel1_page, drivers_page],
            #"Analyse Q3 Silverstone 2024": [gp_page,
            #                                track_page,
            #                                speed_page,
            #                                krümmungsradius_page,
            #                                az_fz_page,
            #                                haftreibung_page,
            #                                faero_page],
        }
    )

pg.run()