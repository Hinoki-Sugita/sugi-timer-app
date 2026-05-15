import streamlit as st
import time

two   = st.checkbox("2人")
three = st.checkbox("3人")
four  = st.checkbox("4人")
five  = st.checkbox("5人")

placeholder = st.empty()

for remaining in range(120, -1, -1):
    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        placeholder.write("終了")
    else:
        placeholder.write(f"{minutes:02}:{seconds:02}")

    if two:
        if remaining == 60:
            st.write("2人のとこ、1回目")
    if three:
        if remaining == 80:
            st.write("3人のとこ、1回目")
        if remaining == 40:
            st.write("3人のとこ、2回目")
    if four:
        if remaining == 90:
            st.write("4人のとこ、1回目")
        if remaining == 60:
            st.write("4人のとこ、2回目")
        if remaining == 30:
            st.write("4人のとこ、3回目")
    if five:
        if remaining == 96:
            st.write("5人のとこ、1回目")
        if remaining == 72:
            st.write("5人のとこ、2回目")
        if remaining == 48:
            st.write("5人のとこ、3回目")
        if remaining == 24:
            st.write("5人のとこ、4回目")

    time.sleep(1)