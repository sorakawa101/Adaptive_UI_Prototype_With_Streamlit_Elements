# レイアウトのパラメータを定義するファイル

from streamlit_elements import dashboard


def get_selected_layout(selected_layout):
    if "Single Column" in selected_layout:
        return layout_single_column
    if "Multi Column" in selected_layout:
        return layout_multi_column
    if "Grid" in selected_layout:
        return layout_grid
    else:
        pass


# * デモ用のレイアウト
layout_demo = [
    # Editor item is positioned in coordinates x=0 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # Media item is positioned in coordinates x=0 and y=2, and takes 12/12 columns and has a height of 4 and is draggable and resizable.
    dashboard.Item("media", 0, 1, 12, 4, isDraggable=True, isResizable=True, moved=False)
]

# * Single Column レイアウト
layout_single_column = [
    dashboard.Item("a_text", 0, 0, 12, 2, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("a_image", 0, 1, 12, 2, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("a_video", 0, 2, 12, 2, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("a_graph", 0, 3, 12, 2, isDraggable=False, isResizable=True, moved=False)
]


# * Multi Column レイアウト
layout_multi_column = [
    dashboard.Item("a_text", 0, 0, 3, 5, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("a_image", 3, 0, 3, 5, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("a_video", 6, 0, 3, 5, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("a_graph", 9, 0, 3, 5, isDraggable=False, isResizable=True, moved=False)
]


# * Grid レイアウト
layout_grid = [
    dashboard.Item("a_text", 0, 0, 6, 2.5, isDraggable=True, isResizable=True, moved=False),
    dashboard.Item("a_image", 6, 0, 6, 2.5, isDraggable=True, isResizable=True, moved=False),
    dashboard.Item("a_video", 0, 1, 6, 2.5, isDraggable=True, isResizable=True, moved=False),
    dashboard.Item("a_graph", 6, 1, 6, 2.5, isDraggable=True, isResizable=True, moved=False)
]