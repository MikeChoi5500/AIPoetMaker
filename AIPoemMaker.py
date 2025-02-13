import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY is not set in .env file. Please set it and restart.")
    st.stop()

# Set OpenAI API key
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("AI 시 생성기 🌟")
st.write("특정 단어를 입력하면, AI가 해당 언어로 멋진 시를 작성해 드립니다!")

# 사용자 입력
user_input = st.text_input("시를 생성하고 싶은 단어나 주제를 입력하세요:", "")

# 버튼 클릭 시 처리
if st.button("시 생성"):
    if user_input.strip():
        with st.spinner("AI가 시를 작성 중입니다..."):
            try:
                # OpenAI ChatCompletion으로 언어 감지 및 시 생성
                response = client.chat.completions.create(
                    model="gpt-4",  # 또는 "gpt-3.5-turbo"
                    messages=[
                        {"role": "system", "content": "You are a poet who writes poems in the language of the user's input."},
                        {"role": "user", "content": f"Write a poem about '{user_input}'."}
                    ],
                    temperature=0.7,
                    max_tokens=150
                )
                # 결과 가져오기
                poem = response.choices[0].message.content.strip()
                # 결과 출력
                st.subheader("생성된 시:")
                st.write(poem)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("단어를 입력하세요!")

# 추가 정보
st.markdown("---")
st.info("OpenAI의 GPT 모델을 사용하여 생성된 시입니다. 입력한 언어에 맞게 작성됩니다.")
