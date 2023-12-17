# srcからのget関数ファイル

import src.texts as srct

def get_texts(recipe, task_feature_set):
    if recipe == "sample" and task_feature_set == "abstract":
        return srct.abstract_list0
    elif recipe == "sample" and task_feature_set == "detail":
        return srct.detail_list0
    else:
        pass