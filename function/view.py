import streamlit as st
from streamlit_elements import elements, dashboard

import components.card as cc
import components.layout as cl
import components.sidebar as cs


# ページ設定
def set_page_config():
    st.set_page_config(
        page_title="Adaptive UI Prototype",
        page_icon="🍴",
        layout="wide",
    )


def view_contents():
    with elements("contents"):

        with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
            cc.view_selected_media_card(cs.get_value_from_the_session_state("media"))


def view_sidebar():
    cs.sidebar()