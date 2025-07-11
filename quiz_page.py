import streamlit as st
from quiz_game import quiz_game

def toggle_button_clicked(value):
    st.session_state.quiz_page = value

def start_quiz_button_clicked():
    if st.session_state.quiz_page == "choose_topic":
        st.session_state.start_quiz_topic = True
        st.session_state.disable_elements = True
    if st.session_state.quiz_page == "upload_doc":
        st.session_state.start_quiz_doc = True
        st.session_state.disable_elements = True

def quiz_page():
       
    col1, col2 = st.columns(2)

    with col1:
        st.button("Master a Topic", use_container_width=True, type="primary", on_click=toggle_button_clicked, args=["choose_topic"], disabled=st.session_state.disable_elements)
    with col2:
        st.button("Master a Document", use_container_width=True, on_click=toggle_button_clicked, args=["upload_doc"], disabled=True)

    if st.session_state.quiz_page == "choose_topic":            
        topic_selectbox = st.selectbox('topic', options=["Python", "DSA using Python", "Machine Learning", "Data Science"], label_visibility = "hidden", index=0, disabled=st.session_state.disable_elements)
        st.session_state.selected_topic = topic_selectbox
        st.button("Start Quiz", on_click=start_quiz_button_clicked, disabled=st.session_state.disable_elements)
        if st.session_state.start_quiz_topic:
            quiz_game()
    elif st.session_state.quiz_page == "upload_doc":
        file_uploader = st.file_uploader('file', label_visibility="hidden", accept_multiple_files=False, type=['pdf'])
        st.button("Start Quiz", on_click=start_quiz_button_clicked, disabled=True)
        if st.session_state.start_quiz_doc:
            quiz_game()