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
            view_contents_sample_tab_element(0)

        with tab1:
            view_contents_sample_tab_element(1)

        with tab2:
            view_contents_sample_tab_element(2)

        with tab3:
            view_contents_sample_tab_element(3)

    else:
        with elements("contents"):

            with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):

                cc.view_selected_media_card(cs.get_value_from_the_session_state("media"), cs.get_value_from_the_session_state("task_feature_set"), cs.get_value_from_the_session_state("font_size"), "sample")


# Full Screenにおけるタブの中身を表示する関数
def view_contents_sample_tab_element(i):
    with elements("contents"+str(i)):
        with dashboard.Grid(cl.get_selected_layout(cs.get_value_from_the_session_state("layout"))):
            cc.view_selected_media_card_on_tab(cs.get_value_from_the_session_state("media"), cs.get_value_from_the_session_state("task_feature_set"), cs.get_value_from_the_session_state("font_size"), "image"+str(i), "video"+str(i), "sample", i)


def view_contents_recipe1():
    st.write("recipe1")


def view_contents_recipe2():
    st.write("recipe2")


def view_sidebar():
    cs.sidebar()