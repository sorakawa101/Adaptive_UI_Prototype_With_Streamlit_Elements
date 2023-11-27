# レイアウトのパラメータを定義するファイル

from streamlit_elements import dashboard


# * デモ用のレイアウト
layout_demo = [
    # Editor item is positioned in coordinates x=0 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # Media item is positioned in coordinates x=0 and y=2, and takes 12/12 columns and has a height of 4 and is draggable and resizable.
    dashboard.Item("media", 0, 1, 12, 4, isDraggable=True, isResizable=True, moved=False)
]

# * Single Column レイアウト
# * Multi Column レイアウト
# * Grid レイアウト
