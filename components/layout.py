# レイアウトのパラメータを定義するファイル
from streamlit_elements import dashboard


def get_selected_layout(selected_layout):
    if "Single Column" in selected_layout:
        return get_layout_single_column()
    if "Full Screen" in selected_layout:
        return layout_full_screen
    if "Grid" in selected_layout:
        return get_layout_grid()
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
def get_layout_single_column():

    layout_single_column = [
        dashboard.Item("step0", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step1", 0, 1, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step2", 0, 2, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step3", 0, 3, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step4", 0, 4, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step5", 0, 5, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step6", 0, 6, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step7", 0, 7, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step8", 0, 8, 12, 4, isDraggable=False, isResizable=True, moved=False),
        dashboard.Item("step9", 0, 9, 12, 4, isDraggable=False, isResizable=True, moved=False),
    ]

    return layout_single_column


# * Grid レイアウト
def get_layout_grid():

    layout_grid = [
        dashboard.Item("step0", 0, 0, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step1", 6, 0, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step2", 0, 1, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step3", 6, 1, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step4", 0, 2, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step5", 6, 2, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step6", 0, 3, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step7", 6, 3, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step8", 0, 4, 6, 4, isDraggable=True, isResizable=True, moved=False),
        dashboard.Item("step9", 6, 4, 6, 4, isDraggable=True, isResizable=True, moved=False),

        # dashboard.Item("a_text", 0, 0, 4, 6, isDraggable=True, isResizable=True, moved=False),
        # dashboard.Item("a_image", 4, 0, 4, 6, isDraggable=True, isResizable=True, moved=False),
        # dashboard.Item("a_video", 8, 0, 4, 6, isDraggable=True, isResizable=True, moved=False),
    ]

    return layout_grid

# * Full Screen レイアウト
layout_full_screen = [
    dashboard.Item("step0", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step1", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step2", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step3", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step4", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step5", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step6", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step7", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step8", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),
    dashboard.Item("step9", 0, 0, 12, 4, isDraggable=False, isResizable=True, moved=False),

    # dashboard.Item("a_text", 0, 0, 12, 1, isDraggable=True, isResizable=True, moved=False),
    # dashboard.Item("a_image", 0, 1, 6, 5, isDraggable=True, isResizable=True, moved=False),
    # dashboard.Item("a_video", 6, 1, 6, 5, isDraggable=True, isResizable=True, moved=False)
]