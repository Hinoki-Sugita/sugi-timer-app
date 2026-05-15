import streamlit as st
import time

two   = st.checkbox("2人")
three = st.checkbox("3人")
four  = st.checkbox("4人")
five  = st.checkbox("5人")

placeholder = st.empty()

for remaining in range(20, -1, -1):
    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        placeholder.write("終了")
    else:
        placeholder.write(f"{minutes:02}:{seconds:02}")
    time.sleep(1)

    if remaining == 10:
        st.write("10秒")
