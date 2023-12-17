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
        set_card_step("step"+str(i), media_list, ff.get_texts(recipe, task_feature_set)[i], font_size, font_color, "image"+str(i), "video"+str(i))


# Full Screen用の表示関数
def view_selected_media_card_on_tab(media_list, task_feature_set, font_size, font_color, image, video, recipe, i):
    set_card_step("step"+str(i), media_list, ff.get_texts(recipe, task_feature_set)[i], font_size, font_color, image, video)


# * デモ用のカード
def card_demo(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Media Player")

        with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
            mui.Typography("Hello world")


# * 手順カード
def set_card_step(kw, media_list, text, text_size, text_color, image, video):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column", "color":f'{text_color}'}):
        mui.CardHeader(title=kw)
        if "Text" in media_list:
            with mui.CardContent():
                with mui.Typography:
                    set_card_step_text_size(text, text_size)

        with mui.CardContent(sx={"display": "flex", "flexDirection": "row"}):
            if "Image" in media_list:
                with mui.CardContent(sx={"height": "300px", "width": "600px"}):
                    mui.CardMedia(component="img", image="https://lh3.googleusercontent.com/pw/ABLVV87xjVCQpik8RgIU5Rp8ouPNk7nPV8fe4fuGMMvVcWvsALxHMrLBzmRjXHTomGYNKMdAU-PT6gbLnIlSMFx0DdUEmg-brbhAtK_PYFBVnmmetwsXMP7rW6dL4Am9oNGhDxOu9WF_eMIQjERd9fGl8BfAV23YS1P1ixbGvvY-nqBhZH99YG5wCOpopAgTjebFMZrNsWa-ArXnXu5Bjc6wYIdJ7DQlJD92kgaO58-Dfb9Tjr_5er5jmPqqdCTtSsXvBcX1MK_XDWID4l_32okbpmw2azsH5UKbP2BThNOgUFDpxOHsqFQ55fyQRCc1ug4rCaHRRcEvFBKdnD_nm3TSOHXZDzghBsCnRH7LardLcDJ45t-Otkn8a2tHU09wIwt6X48taCy9lJQEL58sL7lUsd30dnQ3UDhMLsELNktilEpr3F_nzkYvSb6--BqWR3n2kzOeKr2_p6oAeXxi3VA7UDKg_7JptuH1f1xnxm2CZ47urqmTKkhpmPc0T-eUtZenesCCdr-n5DmDQsv_bZ-kvFZT1eWzC0VuibzdRWGYtTqfDwjSK5DYYguE2uKj2VCr9Tik6YFIug2zdbeiny28J6BaOFPAInnjaGpFQGPKiRNS3s4ivFzDr3AnkafD10LCdGvq3TVX4b82nsgKe4T9yPqaiBjKvETsl-oj9V_8ZLi6arKqzhTLeZPJNYZ5BDSxvrwsz8byl5RXmW7Ou6jlQTn0AlsMqKXjK0qa60RkCT2ue02m6quRgELwBjNdajfqijCqQkGNpV-p5IDklLST-j_j-NumVD-gue_M_-2rTjyjqi3E2j8dZaRQMW5BL4Egadh-EgCYXlfEfhQiGn-o60x8SCH_jzLuVPxgMWKj0vkY3rCOU3tEEE9u6dECr7sDGrDGyg=w1174-h1566-s-no-gm?authuser=0", alt="img1")

            if "Video" in media_list:
                with mui.CardContent(sx={"height": "300px", "width": "600px"}):
                    media.Player(url="https://youtu.be/j4lVwCwN4kI", width="100%", height="100%", controls=True)


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
