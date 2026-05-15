import streamlit as st
import time

placeholder = st.empty()

for remaining in range(600, -1, -1):
    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        placeholder.write("終了")
    else:
        placeholder.write(f"{minutes:02}:{seconds:02}")

    time.sleep(1)
