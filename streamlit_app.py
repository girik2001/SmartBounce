import streamlit as st

from home_page import home_page
from quiz_page import quiz_page

if "current_page" not in st.session_state:
    st.session_state['current_page'] = "home_page"

if "quiz_page" not in st.session_state:
    st.session_state['quiz_page'] = "choose_topic"

if "start_quiz_topic" not in st.session_state:
    st.session_state['start_quiz_topic'] = False

if "start_quiz_doc" not in st.session_state:
    st.session_state['start_quiz_doc'] = False

if "question_number" not in st.session_state:
    st.session_state['question_number'] = 0

if st.session_state['current_page'] == "home_page":
    home_page()

if st.session_state['current_page'] == "quiz_page":
    quiz_page()