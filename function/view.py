# コンテンツを表示する関数ファイル

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

# 選択されたレシピに応じてコンテンツを選択的に表示する関数
def view_contents():
    selected_recipe = cs.get_value_from_the_session_state("recipe")

    if selected_recipe == "Recipe1":
        view_contents_recipe1()
    elif selected_recipe == "Recipe2":
        view_contents_recipe2()
    else:
        view_contents_sample()

# サンプルレシピを表示する関数
def view_contents_sample():

    if cs.get_value_from_the_session_state("layout") == "Full Screen":
        tab0, tab1, tab2, tab3 = st.tabs(["Step0", "Step1", "Step2", "Step3"])

        with tab0:
            view_contents_tab_element("sample", 0)

        with tab1:
            view_contents_tab_element("sample", 1)

        with tab2:
            view_contents_tab_element("sample", 2)

        with tab3:
            view_contents_tab_element("sample", 3)

    else:
        with elements("contents"):

            with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):

                cc.view_selected_media_card(cs.get_value_from_the_session_state("media"), cs.get_value_from_the_session_state("task_feature_set"), cs.get_value_from_the_session_state("font_size"), cs.get_value_from_the_session_state("font_color"),  "sample")


# Full Screenにおけるタブの中身を表示する関数
def view_contents_tab_element(recipe, i):
    with elements("contents"+str(i)):
        with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
            cc.view_selected_media_card_on_tab(cs.get_value_from_the_session_state("media"), cs.get_value_from_the_session_state("task_feature_set"), cs.get_value_from_the_session_state("font_size"), cs.get_value_from_the_session_state("font_color"), "image"+str(i), "video"+str(i), recipe, i)


def view_contents_recipe1():
    if cs.get_value_from_the_session_state("layout") == "Full Screen":
        tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Step0", "Step1", "Step2", "Step3", "Step4", "Step5", "Step6", "Step7", "Step8", "Step9"])

        with tab0:
            view_contents_tab_element("recipe1", 0)

        with tab1:
            view_contents_tab_element("recipe1", 1)

        with tab2:
            view_contents_tab_element("recipe1", 2)

        with tab3:
            view_contents_tab_element("recipe1", 3)

        with tab4:
            view_contents_tab_element("recipe1", 4)

        with tab5:
            view_contents_tab_element("recipe1", 5)

        with tab6:
            view_contents_tab_element("recipe1", 6)

        with tab7:
            view_contents_tab_element("recipe1", 7)

        with tab8:
            view_contents_tab_element("recipe1", 8)

        with tab9:
            view_contents_tab_element("recipe1", 9)

    else:
        with elements("contents"):

            with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):

                cc.view_selected_media_card(cs.get_value_from_the_session_state("media"), cs.get_value_from_the_session_state("task_feature_set"), cs.get_value_from_the_session_state("font_size"), cs.get_value_from_the_session_state("font_color"),  "recipe1")


def view_contents_recipe2():
    st.write("recipe2")


def view_sidebar():
    cs.sidebar()