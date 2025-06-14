import streamlit as st

def next_question_button_clicked(question, options, explanation, answer, captured_answer):
    st.session_state.question_number+=1
    try:
        if options.index(captured_answer)==answer:
            answer_check = True
        else:
            answer_check = False
    except:
        answer_check = False

def quiz_game(question = "Dummy Question", options = ["a", "b", "c", "d"], explanation = "Explanation", answer = 0):
    progress_bar = st.progress(st.session_state.question_number/20, text=f"Quiz Completion Percentage: {st.session_state.question_number}/20")
    with st.container(border=True):
        generated_question = st.write(f'<p style="font-family: Serif; margin: 0; font-size: 25px">{question}</p>', unsafe_allow_html=True)
        captured_answer = st.radio("options : ", options=options, label_visibility="hidden", index=None, key=st.session_state.question_number)
        with st.expander("Explanation", expanded=False):
            st.write(f"{explanation}")
        st.button("next", on_click=next_question_button_clicked, args=(question, options, explanation, answer, captured_answer))