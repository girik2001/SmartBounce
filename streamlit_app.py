import streamlit as st
import pandas as pd

from home_page import home_page
from quiz_page import quiz_page
from results_page import results_page

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

if st.session_state.question_number == 20:
    st.session_state.disable_elements = False

if "selected_topic" not in st.session_state:
    st.session_state['selected_topic'] = "Python"

if "disable_elements" not in st.session_state:
    st.session_state['disable_elements'] = False

if "data" not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=["question", "option1", "option2", "option3", "option4", "actual_answer", "your_selection", "correct/wrong", "explanation"])

if "difficulty_level" not in st.session_state:
    st.session_state['difficulty_level'] = "Easy"

if st.session_state['current_page'] == "home_page":
    home_page()

if st.session_state['current_page'] == "quiz_page":
    quiz_page()

if st.session_state['current_page'] == "results_page":
    results_page()