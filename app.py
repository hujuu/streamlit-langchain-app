import streamlit as st

st.title("langchain-streamlit-app")

prompt = st.chat_input("What is up?")

if prompt:  # 入力された文字列がある(Noneでも空文字列でもない)場合
    # ユーザーのアイコンで
    with st.chat_message("user"):
        # promptをマークダウンとして整形して表示
        st.markdown(prompt)
    # AIのアイコンで
    with st.chat_message("assistant"):
        response = "こんにちは"  # 固定の応答を用意して
        st.markdown(response) # 応答をマークダウンとして整形して表示
