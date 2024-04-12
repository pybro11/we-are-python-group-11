from st_audiorec import st_audiorec
import streamlit as st 
import json
from google.cloud import speech
from google.oauth2 import service_account
import openai

# Load the JSON secret
service_account_info = {
  "type": "service_account",
  "project_id": "steam-cache-420106",
  "private_key_id": "90ec9d24e7ecb765b189e9eb6cde776ef2e95ed4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCaoKLqjAsyovAB\n5t7/D8lR9a9zL9qDj068xJwFejFroFUM2sDBNObsFhfOSBEkeaaX2x4FcDzPge8B\ngAIAzoGdmjEksFSI716vbrAN0Bphp2QvKKCMiG/HXEelKMGZ5Z8VSIeVqorKKlzq\n9fIP1rL6PBpsZlhRdqQhHPNE7HY7nfuRL8re2s3tlYmRm7KG44GAXc3MsBRJMQT1\nZbj3TNYoYjVij94GS07ZFHorI3lxnA2z+nHlIZ53Yg4rvHaI0NjUgnxfTEpLwu9w\nQqxdcJOggxC5H1KDMJ1qYUw8qtFuPSQxJQJhQXw8R98xRhkJZnwieyzHrBvz0UI+\nkJ6ozd4bAgMBAAECggEAQrupFAi0nHntkySMgQ/TFugtfEzexYCHvrgrjcGaqpRb\noFyYa8nlD2bJh2Fa5J8L4uXSIw65b+TnvYH9W1PEZLwzEV54XVDRUG041f1GJXcU\nqbWi9IO9mhCdaw4X389VxN20hkc/9tgpmc3jViqWu6BM1xOkciP92byg0NIshLWS\nG4USXKbcwel5ENkpmA17qwihLl6iQs4vEPwBaKOceZWlgo99V9D4H3UVkjniRZCg\nraRDNGVIhmH65o8ctzW+f1NWFER8EsXJoEH96AMcPgyWuTy4n5tYeJcNOwbAN2qV\nOUBVbSeZNvqiFJuVWFtRiV93T7BFiP/EmTeZSZbDwQKBgQDMpPhL3BiA78eHehlD\nuOl/MqjM+G25yjJP4sVayoX9ro7AT5hRKdo1mhtuzmqsrbD7CeROoR29ziS5EAYR\nyNzNFYHnoyEP2TbPbGwrr7lBIWKh16RyYjGlCRtFJTXr9ClUlECDCLaHnggVRsZM\nhqqgv2g9nnkhnzETrttEcZaKgwKBgQDBbmog+QuQuPXXkSv0fuo5+x9eiOI5wSLS\nemVn3y6Pg3ksFaMWMKHB9Cn7sSewWZiwIddspUqcvrjixT0UbYe+XjY5Ec4JG5qs\n8IIgkw+DbycyQiZ3daRHKTKRzq+y6ond/MiPTGe1F7c3g1ad892w1z6ElVhLFzYp\nVsspLzbqiQKBgQDEcDL7tqk603AnhrfLvys78yf/oRTKu+Gxt0+USEV4buAOkBj5\nCACzZVuh8LiLSytQvn0OUTAYa1Hq5wu8dKAmqNeKv5dT/EDVuRDYmpRshZyFGFd9\niO54qhYoOIDbHwOxcaG/ZlS4N6Uwr0BYYwhUx4dLZtyFvqbAax+FQrer+wKBgQCY\n1WsZnm2a7emhZ9z5FAZxxY+lnDZTN90RvQ++oMMjNdhaEsaHU+mbXBaH/hPD7ScN\nk8+o0nk/nBptYza9m0V0DvB86yqGW789AdNvdYL+cKbhuQ63uMYSS+Te/BYrIdHJ\nCmBViSMwHQrw299mcjcp8Qg+rdnTiwWKaD+hzOJxMQKBgQC97etgD5Hr9HsuvMNb\nw40c9KZ63GvEN1IFtDBGEjeLlMiItdoXUDw9JvDeDDRet7gauqJ++rCahbtDmQ29\nxvQ416HqQ1z+SAo7+GkbDQIQcYjt+ao3z07vxqAclR6kgLWjyzVeUAQ9N2eIubQ/\nRqYdhv2AtdMTWjRkv16TvBvf4A==\n-----END PRIVATE KEY-----\n",
  "client_email": "lucypothesis@steam-cache-420106.iam.gserviceaccount.com",
  "client_id": "110045906642819557227",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/lucypothesis%40steam-cache-420106.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Create the SpeechClient with the loaded credentials
credentials = service_account.Credentials.from_service_account_info(service_account_info)
client = speech.SpeechClient(credentials=credentials)

# DESIGN implement changes to the standard streamlit UI/UX
# --> optional, not relevant for the functionality of the component!

# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode

def query_gpt(text, model="text-davinci-002"):
    """Query OpenAI GPT using the provided text and return the response."""
    openai.api_key = st.secrets["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"]
    response = openai.Completion.create(
        model=model,
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def transcribe_google(audio_bytes):
    """Google Cloud Speech-to-Text를 사용하여 오디오 바이트를 텍스트로 변환합니다."""
    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        audio_channel_count=2,
        language_code="ko-KR"  # 여기서 언어 설정을 조정할 수 있습니다.
    )
    # API 요청 및 응답
    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript
    return transcription

def audiorec_demo_app():
    """오디오 녹음하고 텍스트로 변환합니다."""
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')

        transcription = transcribe_google(wav_audio_data)
        st.text_area("Transcription", transcription, height=100)
        response_text = query_gpt(transcription)
        st.text_area("GPT Response", response_text, height=150)
