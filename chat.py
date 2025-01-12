import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response

load_dotenv()

#페이지 title, favicon 설정
st.set_page_config(page_title='챗봇', page_icon="👼")

#화면의 타이틀, 설명
st.title("👼 인프런 강의 챗봇")
st.caption("무엇이든물어보세요")

#메시지를 저장하기 위해 세션 스테이트에 리스트를 설정
#리스트가 없으면 빈 리스트 생성
if 'message_list' not in st.session_state :
    st.session_state.message_list = []

#리스트에 있는 메세지들을 그려줌
for message in st.session_state.message_list :
    with st.chat_message(message['role']):
        st.write(message['content'])

#질문 받아서 리스트에 저장
if user_question := st.chat_input(placeholder='소득세에 관련된 내용을 물어보세요~~'):
    with st.chat_message('user'):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner('답변 생성하는 중..'):
        ai_resopnse = get_ai_response(user_question)
        with st.chat_message('ai'):
            ai_message = st.write_stream(ai_resopnse)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})    
    


