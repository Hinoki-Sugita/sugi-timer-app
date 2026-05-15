import streamlit as st
import time


def explode():
    audio_placeholder.audio(
        audio_bytes,
        format="audio/mp3",
        autoplay=True)

two   = st.checkbox("2人")
three = st.checkbox("3人")
four  = st.checkbox("4人")
five  = st.checkbox("5人")

placeholder = st.empty()
audio_placeholder = st.empty()

audio_file = open("爆発.mp3", "rb")
audio_bytes = audio_file.read()

for remaining in range(1200, -1, -1):
    minutes = remaining // 60
    seconds = remaining % 60

    if remaining == 0:
        placeholder.write("終了")
    else:
        placeholder.write(f"{minutes:02}:{seconds:02}")

    if two:
        if remaining == 600:
            st.write("2人のとこ") ; explode()
    if three:
        if remaining in [800,400]:
            st.write("3人のとこ") ; explode()
    if four:
        if remaining in [900,300]:
            st.write("4人のとこ") ; explode()
        if remaining == 600 and not two:
            st.write("4人のとこ") ; explode()
    if five:
        if remaining in [960,720,480,240]:
            st.write("5人のとこ") ; explode()

    time.sleep(0.1)