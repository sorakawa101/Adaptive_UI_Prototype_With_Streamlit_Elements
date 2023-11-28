# サイドバーを用意するファイル

import streamlit as st
from streamlit_elements import mui

def sidebar():
    with st.sidebar:
        navigation = input_navigation()
        set_value_to_the_session_state("navigation", navigation)

        layout = input_layout()
        set_value_to_the_session_state("layout", layout)

        font_size = input_font_size()
        set_value_to_the_session_state("font_size", font_size)

        color = input_color()
        set_value_to_the_session_state("color", color)

        task_feature_set = input_task_feature_set()
        set_value_to_the_session_state("task_feature_set", task_feature_set)

        # TODO デバッグ用なので後でコメントアウト
        sidebar_io_test()


# サイドバーからの入出力の動作確認テスト
def sidebar_io_test():
    st.write(get_value_from_the_session_state("navigation"))
    st.write(get_value_from_the_session_state("layout"))
    st.write(get_value_from_the_session_state("font_size"))
    st.write(get_value_from_the_session_state("color"))
    st.write(get_value_from_the_session_state("task_feature_set"))



# keyを指定して，対応するsession_stateに入力値を格納する関数
def set_value_to_the_session_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = None

    if value:
        st.session_state[key] = value


# keyを指定して，対応するsession_stateから入力値を取得する関数
def get_value_from_the_session_state(key):
    return st.session_state[key]


# navigationの入力欄を設置し，入力値を返す関数
def input_navigation():
    navigation = st.multiselect(
        "What's your favorite navigation?",
        ["Text", "Image", "Video", "Graph"],
        ["Text", "Image", "Video", "Graph"],
    )  # st.multiselect(label, selected, first-value)

    return navigation


# layoutの入力欄を設置し，入力値を返す関数
def input_layout():
    layout = st.radio(
        "What's your favorite layout",
        ["Single Column", "Multi Column", "Grid"],
        captions=["Single Column", "Multi Column", "Grid"],
    )  # st.radio(label, selected, captions)

    return layout


# font sizeの入力欄を設置し，入力値を返す関数
def input_font_size():
    font_size = st.slider(
        "What's your favorite font size?", 0, 100, 5
    )  # st.slider(label, min, max, step)

    return font_size


# colorの入力欄を設置し，入力値を返す関数
def input_color():
    color = st.color_picker(
        "Pick your favorite Color", "#00f900"
    )  # st.color_pecker(label, first-value)

    return color


# task_feature_setの入力欄を設置し，入力値を返す関数
def input_task_feature_set():
    task_feature_set = st.toggle("More Suggested Amount")
    return task_feature_set

