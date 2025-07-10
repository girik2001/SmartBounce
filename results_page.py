import streamlit as st
from home_page import home_page

def callback():
    for key in st.session_state.keys():
        del st.session_state[key]

def results_page():
    st.balloons()
    st.write(f'<p style = "color:Tomato; text-align:center; font-family: Serif; font-size:90px; font-weight:bold; margin: 0; display: inline;">You Scored: </p><p style = "color:white; text-align:center; font-family: Serif; font-size:90px; font-weight:bold; margin: 0; display: inline;">{st.session_state.data['correct/wrong'].value_counts().get('correct', 0)}/20</p>', unsafe_allow_html=True)
    st.dataframe(data=st.session_state.data, use_container_width=True, hide_index=True, height=500)
    st.download_button(
        "Download Results",
        data = st.session_state.data.to_csv().encode('utf-8'),
        file_name="Result.csv",
        on_click=callback,
        use_container_width=True,
        type='primary'
    )