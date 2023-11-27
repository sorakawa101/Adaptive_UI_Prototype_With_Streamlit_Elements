import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Adaptive UI Prototype",
    page_icon="🍴",
    layout="wide",
)


from streamlit_elements import elements, dashboard, mui


with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Define URL for media player.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")


import components.layout as ll
import components.card_demo as ccd

with elements("demo"):

    with dashboard.Grid(ll.layout_demo):

        ccd.card_demo('media')
        ccd.card_demo('editor')