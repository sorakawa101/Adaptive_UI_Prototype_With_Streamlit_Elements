# サイドバーを用意するファイル

import streamlit as st

def sidebar():
    with st.sidebar:
        username = input_username()
        set_value_to_the_session_state("username", username)

        recipe = input_recipe()
        set_value_to_the_session_state("recipe", recipe)

        st.header("カスタマイズ")

        media = input_media()
        set_value_to_the_session_state("media", media)

        layout = input_layout()
        set_value_to_the_session_state("layout", layout)

        font_size = input_font_size()
        set_value_to_the_session_state("font_size", font_size)

        font_color = input_font_color()
        set_value_to_the_session_state("font_color", font_color)

        task_feature_set = input_task_feature_set()
        set_value_to_the_session_state("task_feature_set", task_feature_set)

        st.write("⑥ 要素をドラッグして配置変更")
        st.write("⑦ 要素の右下からリサイズ")

        sidebar_io_result()


# サイドバーからの入出力結果一覧
# TODO 結果一覧をDBに送信
def sidebar_io_result():
    with st.expander("カスタマイズUI結果"):

        st.write("ユーザー名："+str(get_value_from_the_session_state("username")))
        st.write("⓪："+str(get_value_from_the_session_state("recipe")))
        st.write("①："+str(get_value_from_the_session_state("media")))
        st.write("②："+str(get_value_from_the_session_state("layout")))
        st.write("③："+str(get_value_from_the_session_state("font_size")))
        st.write("④："+str(get_value_from_the_session_state("font_color")))
        st.write("⑤："+str(get_value_from_the_session_state("task_feature_set")))



# keyを指定して，対応するsession_stateに入力値を格納する関数
def set_value_to_the_session_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = None

    if value:
        st.session_state[key] = value


# keyを指定して，対応するsession_stateから入力値を取得する関数
def get_value_from_the_session_state(key):
    return st.session_state[key]


def input_username():
    username = st.text_input("ユーザー名", "笹川")
    return username


# mediaの入力欄を設置し，入力値を返す関数
def input_recipe():
    recipe = st.selectbox(
        "⓪ レシピを選択",
        ("Sample", "Recipe1", "Recipe2"),
    )  # st.multiselect(label, selected, first-value)

    return recipe


# mediaの入力欄を設置し，入力値を返す関数
def input_media():
    media = st.multiselect(
        "① 必要なメディアを選択(複数可)",
        ["Text", "Image", "Video"],
        ["Text", "Image", "Video"],
    )  # st.multiselect(label, selected, first-value)

    return media


# layoutの入力欄を設置し，入力値を返す関数
def input_layout():
    layout = st.radio(
        "② レイアウトを指定",
        ["Single Column", "Full Screen", "Grid"],
        captions=["Single Column", "Full Screen", "Grid"],
    )  # st.radio(label, selected, captions)

    return layout


# font sizeの入力欄を設置し，入力値を返す関数
def input_font_size():
    font_size = st.slider(
        "③ フォントサイズを指定", 1, 5, 1
    )  # st.slider(label, min, max, step)

    return font_size


# colorの入力欄を設置し，入力値を返す関数
def input_font_color():
    font_color = st.color_picker(
        "④ 色を指定", "#000000"
    )  # st.color_pecker(label, first-value)

    return font_color


# task_feature_setの入力欄を設置し，入力値を返す関数
def input_task_feature_set():
    task_feature_set = st.toggle("⑤ 情報量を抑制")
    if task_feature_set:
        return "abstract"
    else:
        return "detail"
