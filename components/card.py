# Cardのパラメータを定義するファイル

from streamlit_elements import mui, media

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


# * Graph カード
def card_graph(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Graph")