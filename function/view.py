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

    if cs.get_value_from_the_session_state("layout") == "Full Screen":
        tab1, tab2, tab3 = st.tabs(["Step1", "Step2", "Step3"])

        with tab1:
            with elements("contents"):

                with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
                    cc.view_selected_media_card_on_tab(cs.get_value_from_the_session_state("media"), "text1", "image1", "video1")

        with tab2:
            with elements("contents2"):

                with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
                    cc.view_selected_media_card_on_tab(cs.get_value_from_the_session_state("media"), "text2", "image2", "video2")
        with tab3:
            with elements("contents3"):

                with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
                    cc.view_selected_media_card_on_tab(cs.get_value_from_the_session_state("media"), "text3", "image3", "video3")


    else:
        with elements("contents"):

            with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
                cc.view_selected_media_card(cs.get_value_from_the_session_state("media"))


def view_sidebar():
    cs.sidebar()