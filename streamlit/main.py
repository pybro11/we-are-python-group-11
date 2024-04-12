import streamlit as st 

st.title('트렌드를 분석하는 11조입니다.💫')

import column12

import sidebar

import ploty

import webinput

from whisper_stt import whisper_stt

text = whisper_stt(openai_api_key="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", language = 'en')  
if text:
    st.write(text)

# import audio
# if 'recording_started' not in st.session_state:
#     st.session_state.recording_started = False

# if st.button("음성 녹음 시작", key='start_rec'):
#     st.session_state.recording_started = True

# if st.session_state.recording_started:
#     audio.audiorec_demo_app()
