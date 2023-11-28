import streamlit as st

# ページ設定
def set_page_config():
    st.set_page_config(
        page_title="Adaptive UI Prototype",
        page_icon="🍴",
        layout="wide",
    )


from streamlit_elements import elements, dashboard

def view_sidebar():
    with st.sidebar:
        st.title("🗓️ #30DaysOfStreamlit")
        st.header("Day 27 - Streamlit Elements")
        st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
        st.write("---")


import components.layout as ll
import components.card_demo as ccd

def view_contents():

    with elements("contents"):

        # with dashboard.Grid(ll.layout_single_column):
        with dashboard.Grid(ll.layout_multi_column):
        # with dashboard.Grid(ll.layout_grid):

            ccd.card_text('text')
            ccd.card_image('image')
            ccd.card_video('video')
            ccd.card_graph('graph')


def main():
    set_page_config()
    view_sidebar()
    view_contents()



if __name__ == '__main__':
    main()