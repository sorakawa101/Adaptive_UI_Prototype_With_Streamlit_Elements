# Cardのパラメータを定義するファイル

from streamlit_elements import mui

def view_selected_media_card(media_list):
    if "Text" in media_list:
        card_text('a_text')
    if "Image" in media_list:
        card_image('a_image')
    if "Video" in media_list:
        card_video('a_video')
    else:
        pass


# * デモ用のカード
def card_demo(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Media Player")

        with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
            mui.Typography("Hello world")


# * Text カード
def card_text(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Text")


# * Image カード
def card_image(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Image")


# * Video カード
def card_video(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Video")