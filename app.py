from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Rover Simulator", layout="wide")

# Hide Streamlit's own menu and footer so the simulator fills the page.
st.markdown(
    """
    <style>
      #MainMenu, header, footer { visibility: hidden; }
      .block-container { padding: 0.5rem 1rem 0 1rem; max-width: 100%; }
      iframe { height: calc(100vh - 1rem) !important; min-height: 480px; }
    </style>
    """,
    unsafe_allow_html=True,
)

simulator = (Path(__file__).parent / "simulator.html").read_text(encoding="utf-8")
components.html(simulator, height=860, scrolling=False)
