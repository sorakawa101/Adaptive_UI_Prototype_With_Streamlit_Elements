import streamlit as st

# ページ設定
def set_page_config():
    st.set_page_config(
        page_title="Adaptive UI Prototype",
        page_icon="🍴",
        layout="wide",
    )


from streamlit_elements import elements, dashboard
import components.sidebar as cs

def view_sidebar():
    cs.sidebar()


import components.layout as cl
import components.card as cc

def view_contents():

    with elements("contents"):

        with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
            cc.view_selected_media_card(cs.get_value_from_the_session_state("navigation"))

def main():
    set_page_config()
    view_sidebar()
    view_contents()



if __name__ == '__main__':
    main()