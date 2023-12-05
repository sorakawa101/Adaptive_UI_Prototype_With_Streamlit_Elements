# Cardのパラメータを定義するファイル

from streamlit_elements import mui

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
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                mui.Typography(text)

        if "Image" in media_list:
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                mui.Typography(image)

        if "Video" in media_list:
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                mui.Typography(video)

        else:
            pass


# # * Text カード
# def card_text(kw):
#     with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
#         mui.CardHeader(title="Text")


# # * Image カード
# def card_image(kw):
#     with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
#         mui.CardHeader(title="Image")


# # * Video カード
# def card_video(kw):
#     with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
#         mui.CardHeader(title="Video")