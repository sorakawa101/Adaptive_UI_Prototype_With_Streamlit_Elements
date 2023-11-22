from streamlit_elements import mui

def card_demo(kw):
    with mui.Card(key=kw, sx={"display": "flex", "flexDirection": "column"}):
                mui.CardHeader(title="Media Player", className="draggable")
                with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                    # This element is powered by ReactPlayer, it supports many more players other
                    # than YouTube. You can check it out there: https://github.com/cookpete/react-player#props

                    mui.Typography("Hello world")