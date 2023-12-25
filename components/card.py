# Cardのパラメータを定義するファイル
from streamlit_elements import mui, media, html

import function.func as ff

# Single ColumnとGrid用の表示関数
def view_selected_media_card(media_list, task_feature_set, font_size, font_color, recipe):
    if recipe == "sample":
        recipe_steps = 4
    else:
        recipe_steps = 10

    for i in range(recipe_steps):
        set_card_step("step"+str(i), media_list, ff.get_texts(recipe, task_feature_set)[i], font_size, font_color, ff.get_images(recipe)[i], ff.get_videos(recipe)[i])


# Full Screen用の表示関数
def view_selected_media_card_on_tab(media_list, task_feature_set, font_size, font_color, recipe, i):
    set_card_step("step"+str(i), media_list, ff.get_texts(recipe, task_feature_set)[i], font_size, font_color, ff.get_images(recipe)[i], ff.get_videos(recipe)[i])


# * デモ用のカード
def card_demo(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Media Player")

        with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
            mui.Typography("Hello world")


# * 手順カード
def set_card_step(kw, media_list, text, text_size, text_color, image_url, video_url):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column", "color":f'{text_color}'}):
        # mui.CardHeader(title=kw)
        if "Text" in media_list:
            with mui.CardContent():
                with mui.Typography:
                    set_card_step_text_size(text, text_size)

        with mui.CardContent(sx={"display": "flex", "flexDirection": "row", "height": "100%"}):
            if "Image" in media_list:
                with mui.CardContent(sx={"height": "90%", "width": "30%", "display": "flex", "flexDirection": "column"}):

                    # with mui.CardContent(sx={"height": "200px", "width": "400px"}):
                    mui.CardMedia(component="img", image=image_url[0], width="100%", height="100%",)
                    # with mui.CardContent(sx={"height": "200px", "width": "400px"}):
                    mui.CardMedia(component="img", image=image_url[1], width="100%", height="100%",)
                    # with mui.CardContent(sx={"height": "200px", "width": "400px"}):
                    mui.CardMedia(component="img", image=image_url[2], width="100%", height="100%",)

            if "Video" in media_list:
                with mui.CardContent(sx={"height": "80%", "width": "70%"}):
                    media.Player(url=video_url, width="100%", height="100%", controls=True)


def set_card_step_text_size(text, size):
    if size == 1:
        html.h1(text)
    elif size == 2:
        html.h2(text)
    elif size == 4:
        html.h4(text)
    elif size == 5:
        html.h5(text)
    else:
        html.h3(text)
