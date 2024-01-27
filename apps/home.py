import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    Riverside Change Detection by Remote Sensing
    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
