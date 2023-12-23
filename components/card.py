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
        set_card_step("step"+str(i), media_list, ff.get_texts(recipe, task_feature_set)[i], font_size, font_color, "image"+str(i), ff.get_videos(recipe)[i])


# Full Screen用の表示関数
def view_selected_media_card_on_tab(media_list, task_feature_set, font_size, font_color, image, video, recipe, i):
    set_card_step("step"+str(i), media_list, ff.get_texts(recipe, task_feature_set)[i], font_size, font_color, image, ff.get_videos(recipe)[i])


# * デモ用のカード
def card_demo(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
        mui.CardHeader(title="Media Player")

        with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
            mui.Typography("Hello world")


# * 手順カード
def set_card_step(kw, media_list, text, text_size, text_color, image, video_url):
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
                    mui.CardMedia(component="img", image="https://lh3.googleusercontent.com/pw/ABLVV86Jtwvai7vs5RNXp2oYaCz7VZSndSSLaCWuzwJMUdkbnEF4gMvwUWeKw2x33LdpglHhv2-XFl3dVyro5t4rWbaUeJNLpu4-t3ipBrAYdBg2EvtoM5TJB7k5BIYt_7ZuWiIsFozlKgyhZK1GTuC_U72UeXTSW2bXrKLAKJX5dA_xL4P1dCMP1D0SI9HjoxVrJG9c021I3rqye_PRNpjXZKZQrUH2hWJ1i3Z8iMWC5ln4kCtXxzu8lyzjGOalQK6itXJD2t8PiI9D1dVvEVx-j7mT-U5c_EAawTs9FWK2_XParBpO3l-NSOdB0wjTwOxI2q_RZaMc-RzYHWKqAXPYsa0efvS4vl_eLWOxST_Nyw0ENgu_QL4WP9PU6aSRG6BQ-p9Io2ghW8B_MzqvD7b6BzQpyMfAw06TFvdhSyQ9IuhskSZpbjzuzuxziuHx3sJ90uvK08_tMu1KpECk9z_1pSVoFtEoxjjTaLR43emhCTfVHaPVwP_SY7pTdKR6z2FlS8JDgXelSJYyoVgzJBY0SzNbHvlpm9AvgCPCrzYwA-mqMmXOGSYhBuhW4e5wLfNSIXk6or2zBL2M7_l2GdBnAf3ZBNMjAiQD2G9AJvaY2UxskLtpYjVrlLX7-p71nG7LCSAgQdgW0rW7htXwqp0-PgmFSxDnGhJBaG0tgztLcFj-JrGimk8qfRrRK_FKT02C_YNSojsRqtpy3cmuwYIDAGnZPvepuHtbyzzkhX2fsNE0ISU6zjGvoMMtcHjMp8Y5UGVUT-gsDBjwyv3J-q_ehhpe7vjCCtQ7X-1AnLPE3oFU-3SLHRpUHlaFGuHwZeuZ_3WdkpTjPfka-YdlitloCjA1K9N6uNpFUL0nVnRSXA3tpyiCCG3mQzLdSjBUOaH7a60kgQ=w1920-h1080-s-no-gm?authuser=0", width="100%", height="100%",)
                    # with mui.CardContent(sx={"height": "200px", "width": "400px"}):
                    mui.CardMedia(component="img", image="https://lh3.googleusercontent.com/pw/ABLVV85J-2AJ7wot9oRH7oz54JMOjADZfFf936QebgWBVuIYLZhJY8PvEuplvH-2QL1P2b_m4hjp10ggriYU1gXvZouKexm6ShnCcKFu2Ni-cpMjK402mXQnt6RvYb5mjEKWKLo8ZVNM-YptzB0_ds667SaNvv0-Cf_zEzjb-Gi18KfFyPR3UkGqzF4_i4jl5bRgJk0Q0jxrTVFALpUTWRoLVOqrR61foyZcoTGJQQD8udCYQSeU2Nn9nEKpXVKfez3zfFQPOEGd2Z__vAZSrEsPP_1lhlSLBUMh69Yix6KgbnHxTIhWmJCTx48t2w3u1v8MSFuq7JE0dPLxLrXjnb1mix4NXaQBG-Eo8L-7CiE1G9tq3gApvyFkv3Ly4677X1a2NpNGo4oiH-b5OvEJsyQ_NjBIM4BD1UszXkVkpS1L__5_dLxHSEpFxKJGmtmf0QEDhFxVGYjehJcBzzJw4BB-aKohXlDPX67yuAdHfdpZ9xfz93tu14yT1fsxH1dWaXitWDFol2F_7GVCsmFk6LeX3Kl1HxNrxjdaWEl8CoGIdhkarNr6mMmbwSaCUZnojAcuRBU6mccAO765ZuylnWcnHsgbZB5LTwSqwVMCL5rI3dI90frMWBWHajDC9PClXNyRNTDSk-Gg64etK_YolbVYuak2MvwsUD2Mp4te5xriOAt20QbggOfOFm8g4xM2dA2N4OMlhiLou3WdAuxsNko10xd2bdIqhkp-KwbEwP5vKE51p6r-T6t__RkialpsdvxWZ6PolqQ_YW2r1L6PCSnflPhPuv6PRceLxuBoatZ5K5ys4_LuNiKhpCbBREZebhKusos00gcSiYRttc6wPWL1u6_obknd9N9120Nbt4R4K2i4YcVLnvrzXYwa485FaHIMd6qYCw=w1920-h1080-s-no-gm?authuser=0", width="100%", height="100%",)
                    # with mui.CardContent(sx={"height": "200px", "width": "400px"}):
                    mui.CardMedia(component="img", image="https://lh3.googleusercontent.com/pw/ABLVV84dYpdw1_Qo5rXFZtDTv0vdDwROg9uYlTf4uQ3LzeBJxREBTvI-2wh0MelH4HBDRWOBFtdB33bDbWlSt-LgfaLqtXkQUt97J-ln2e0goRwoWZlEAHBWRS3-Lv-OB2wbcncqXYNIDwRcp-EzZ5JNrr5a1aFd40GAVhlU5MrEl1LkIikepm_Y0Cn92NstWreN5l0qdxKwGThZK1w0Nov_VL7IFQjpN-V-B5CaE0lUw7VrnJ_wxW9IrfsgtiuqMgEef8cU5nWUHw3MpjdY2aCZ9KHSVyudhDseZIp4mp7Oe8RL5_SeYv1ExzIBnb7YxQSY5hHL131rGuTjBfQAtm3osFqm3IJDuxI5S-am07gwPvi4G1NaHu7Xj1ZhjYI5YmkS5KSMkG2h7FZRkSTFhiR2gW7BX0uGRT9zcyMpTiSm7g2tLrWpGUKhM4GrGFx5ZLPZzJrxTRw5S1ZgOqqbMEIWwsbSmKytJUTT3HMK-LIRlgscu6rh007NQXUV19qGzYqD1NaEKs-Krvt_HfvqqZMPM58w94ysly2lsNXMhQXjFjt0vVZjEbU4HE-2Ykl_H6Oy5wUrywlKSQbsT5K0IzhWcWgUynNMxRsRQsUtaemH3iuQ0-gp3weJ9fttF2I4x1ZP6qRisXfyJrTPkdKldbISvvgtQyJeSDzhuyQiZx7TQnKJyr-EUNgrcT2aFjC3blEJy7m2Eu7lt0gXK1JFrVJk4U0Waxk2xB7OtvvFGMV9lS-8H26HE7HqXadGI3bhcLYssEgmFwI2D_XzOHtqJJEKY5cKe7qIN6seUyIIwqwoS5DePYJWNxPnxuPP5b82xyPQthPfWy_KX4Qx8hAFVCUu3VpYicDZ7LeaWkTssQagYBRtx4EVh5-gRVoQXE_clAcA7yPj1Q=w1920-h1080-s-no-gm?authuser=0", width="100%", height="100%",)

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
