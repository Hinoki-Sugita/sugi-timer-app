import streamlit as st
import time

#two   = st.checkbox("2人")
three = st.checkbox("3人")
four  = st.checkbox("4人")
five  = st.checkbox("5人")

placeholder = st.empty()

for remaining in range(1200, -1, -1):
    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        placeholder.write("終了")
    else:
        placeholder.write(f"{minutes:02}:{seconds:02}")

    #if two:
   #     if remaining == 600:
   #         print("2人のとこ、1回目")
    if three:
        if remaining == 800:
            print("3人のとこ、1回目")
        if remaining == 400:
            print("3人のとこ、2回目")
    if four:
        if remaining == 900:
            print("4人のとこ、1回目")
        if remaining == 600:
            print("4人のとこ、2回目")
        if remaining == 300:
            print("4人のとこ、3回目")
    if five:
        if remaining == 960:
            print("5人のとこ、1回目")
        if remaining == 720:
            print("5人のとこ、2回目")
        if remaining == 480:
            print("5人のとこ、3回目")
        if remaining == 240:
            print("5人のとこ、4回目")

    time.sleep(0.12)