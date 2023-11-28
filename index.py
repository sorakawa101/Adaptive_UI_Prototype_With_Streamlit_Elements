import streamlit as st
import function.view as fv


def main():
    # ページ設定
    fv.set_page_config()
    # サイドバー
    fv.view_sidebar()
    # コンテンツ
    fv.view_contents()


if __name__ == '__main__':
    main()