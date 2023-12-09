# Cardのパラメータを定義するファイル
import streamlit as st
from streamlit_elements import mui, media

def view_selected_media_card(media_list):
    card_step("step1", media_list, "text1", "image1", "video1")
    card_step("step2", media_list, "text2", "image2", "video2")
    card_step("step3", media_list, "text3", "image3", "video3")


def view_selected_media_card_on_tab(media_list, text, image, video):
    card_step("a_step", media_list, text, image, video)


# * デモ用のカード
def card_demo(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Media Player")

        with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
            mui.Typography("Hello world")


# * 手順カード
def card_step(kw, media_list, text, image, video):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title=kw)
        if "Text" in media_list:
            with mui.CardContent():
                mui.Typography(text)

        with mui.CardContent(sx={"display": "flex", "flexDirection": "row"}):
            if "Image" in media_list:
                with mui.CardContent(sx={"height": "300px", "width": "600px"}):
                    media.Player(url="https://www.youtube.com/watch?v=vIQQR_yq-8I", width="100%", height="100%", controls=True)

            if "Video" in media_list:
                with mui.CardContent(sx={"height": "300px", "width": "600px"}):
                    media.Player(url="https://www.youtube.com/watch?v=vIQQR_yq-8I", width="100%", height="100%", controls=True)