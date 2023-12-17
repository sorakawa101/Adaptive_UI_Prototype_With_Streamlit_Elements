# srcからのget関数ファイル

import src.texts as srct
import src.images as srci
import src.videos as srcv

# srcからテキスト情報を取得する関数
def get_texts(recipe, task_feature_set):

    # Sample選択時
    if recipe == "sample" and task_feature_set == "abstract":
        return srct.abstract_list0
    elif recipe == "sample" and task_feature_set == "detail":
        return srct.detail_list0

    # Recipe1選択時
    elif recipe == "recipe1" and task_feature_set == "abstract":
        return srct.abstract_list1
    elif recipe == "recipe1" and task_feature_set == "detail":
        return srct.detail_list1

    # Recipe2選択時
    elif recipe == "recipe2" and task_feature_set == "abstract":
        return srct.abstract_list1
    elif recipe == "recipe2" and task_feature_set == "detail":
        return srct.detail_list1

    else:
        pass


# srcから画像URLを取得する関数
def get_images(recipe):

    # Sample選択時
    if recipe == "sample":
        return srci.image_list0

    # Recipe1選択時
    elif recipe == "recipe1":
        return srci.image_list1

    # Recipe2選択時
    elif recipe == "recipe2":
        return srci.image_list2

    else:
        pass


# srcから動画URLを取得する関数
def get_videos(recipe):

    # Sample選択時
    if recipe == "sample":
        return srcv.video_list0

    # Recipe1選択時
    elif recipe == "recipe1":
        return srcv.video_list1

    # Recipe2選択時
    elif recipe == "recipe2":
        return srcv.video_list2

    else:
        pass