import streamlit as st
from Services.genai import generate_question
import time

answer_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3
}

def next_question_button_clicked(question, options, explanation, answer):
    try:
        if options.index(st.session_state.captured_answer)==answer_dict[answer]:
            if st.session_state.difficulty_level == "Easy":
                st.session_state.difficulty_level = "Medium"
            elif st.session_state.difficulty_level == "Medium":
                st.session_state.difficulty_level = "Hard"
            st.session_state.data.loc[len(st.session_state.data)] = [question, *options, options[answer_dict[answer]], st.session_state.captured_answer, "correct", explanation]
        else:
            if st.session_state.difficulty_level == "Hard":
                st.session_state.difficulty_level = "Medium"
            elif st.session_state.difficulty_level == "Medium":
                st.session_state.difficulty_level = "Easy"
            st.session_state.data.loc[len(st.session_state.data)] = [question, *options, options[answer_dict[answer]], st.session_state.captured_answer, "wrong", explanation]
    except:
        if st.session_state.difficulty_level == "Hard":
            st.session_state.difficulty_level = "Medium"
        elif st.session_state.difficulty_level == "Medium":
            st.session_state.difficulty_level = "Easy"
        st.session_state.data.loc[len(st.session_state.data)] = [question, *options, answer, st.session_state.captured_answer, "wrong", explanation]
    st.session_state.question_number+=1

def submit_quiz_button_clicked():
    st.session_state.current_page = "results_page"

def quiz_game(question = "Dummy Question", options = ["A", "B", "C", "D"], explanation = "Explanation", answer = "A"):
    st.progress(st.session_state.question_number/20, text=f"Question No.: {st.session_state.question_number}/20 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:blue-background[{st.session_state.difficulty_level}]")
    with st.form(key=str(st.session_state.question_number), border=True, clear_on_submit=False, enter_to_submit=False):
        call_function =  generate_question()
        question, options, answer, explanation = call_function['question'], call_function['options'], call_function['correct_option'], call_function['explanation']
        st.write(f'<p style="font-family: Serif; margin: 0; font-size: 25px">{question}</p>', unsafe_allow_html=True)
        captured_answer = st.radio("options : ", options=options, label_visibility="hidden", index=None, key="captured_answer")
        st.text("")
        print(captured_answer)
        col1, col2 = st.columns(2)
        with col1:
            st.form_submit_button("next", on_click=next_question_button_clicked, args=(question, options, explanation, answer), disabled=not st.session_state.disable_elements, use_container_width=True)
        with col2:
            st.form_submit_button("Submit", on_click=submit_quiz_button_clicked, disabled=st.session_state.disable_elements, use_container_width=True)