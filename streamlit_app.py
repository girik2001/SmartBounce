import streamlit as st

from home_page import home_page
from quiz_page import quiz_page

if "current_page" not in st.session_state:
    st.session_state['current_page'] = "home_page"

if st.session_state['current_page'] == "home_page":
    home_page()

if st.session_state['current_page'] == "quiz_page":
    quiz_page()