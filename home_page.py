import streamlit as st

def challenge_yourself_button_clicked():
    st.session_state.current_page = "quiz_page"

def home_page():
    st.write("""<p style = "color:Tomato; text-align:center; font-family: Serif; font-size:90px; font-weight:bold; margin: 0">Smart Bounce.</p>
    <h2 style = "color:white; text-align:center; margin:0;">BOUNCE BACK SMARTER FROM MISTAKES</h2>""", unsafe_allow_html=True)

    st.text("")
    st.text("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.link_button('Python', use_container_width=True, url='https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
    with col2:
        st.link_button('DSA using Python', use_container_width=True, url='https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/')
    with col3:
        st.link_button('Machine Learning', use_container_width=True, url='https://www.geeksforgeeks.org/machine-learning/machine-learning/')
    with col4:
        st.link_button('Data Science', use_container_width=True, url='https://www.geeksforgeeks.org/data-science/data-science-for-beginners/')

    st.text("")
    st.text("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.button('Challenge Yourself', use_container_width=True, type="primary", on_click=challenge_yourself_button_clicked)