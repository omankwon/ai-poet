# from dotenv import load_dotenv
# load_dotenv('key.env')

from langchain_openai import ChatOpenAI
import streamlit as st


# 객체 생성
llm = ChatOpenAI(
    temperature=1.0,  # 창의성 (0.0 ~ 2.0)
    model_name="gpt-4o-mini",  # 모델명
)

st.title('인공지능 시인')
content = st.text_input('시의 주제를 제시하세요')

if st.button('눌러서 요청'):
    with st.spinner('Wait for it...'):    
        result = llm.predict(content +"에 대한 시를 서줘")
        st.write(result)


# 실행 commnad C:\JININFRA\LLM\STD\STD1> streamlit run main.py