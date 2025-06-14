import streamlit as st

def toggle_button_clicked(value):
    st.session_state.quiz_page = value

def start_quiz_button_clicked():
    if st.session_state.quiz_page == "choose_topic":
        st.session_state.start_quiz_topic = True
    if st.session_state.quiz_page == "upload_doc":
        st.session_state.start_quiz_doc = True

def quiz_page():
       
    col1, col2 = st.columns(2)

    with col1:
        st.button("Master a Topic", use_container_width=True, type="primary", on_click=toggle_button_clicked, args=["choose_topic"])
    with col2:
        st.button("Master a Document", use_container_width=True, on_click=toggle_button_clicked, args=["upload_doc"])

    if st.session_state.quiz_page == "choose_topic":
        topic_selectbox = st.selectbox('topic', options=["Python", "DSA using Python", "Machine Learning", "Data Science"], label_visibility = "hidden", index=0)
        st.button("Start Quiz", on_click=start_quiz_button_clicked)
        if st.session_state.start_quiz_topic:
            st.write("quiz started for topic")
    elif st.session_state.quiz_page == "upload_doc":
        file_uploader = st.file_uploader('file', label_visibility="hidden", accept_multiple_files=False, type=['pdf'])
        st.button("Start Quiz", on_click=start_quiz_button_clicked)
        if st.session_state.start_quiz_doc:
            st.write("quiz started for doc")