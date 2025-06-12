import streamlit as st

def home_page():
    st.write("""<p style = "color:Tomato; text-align:center; font-family: Serif; font-size:100px; font-weight:bold; margin: 0">Smart Bounce.</p>
    <h2 style = "color:white; text-align:center; margin:0;">BOUNCE BACK SMARTER FROM MISTAKES</h2>""", unsafe_allow_html=True)

    st.text("")
    st.text("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.link_button('C', use_container_width=True, url='https://www.w3schools.com/c/index.php')
    with col2:
        st.link_button('C++', use_container_width=True, url='https://www.w3schools.com/cpp/default.asp')
    with col3:
        st.link_button('Java', use_container_width=True, url='https://www.w3schools.com/java/default.asp')
    with col4:
        st.link_button('Python', use_container_width=True, url='https://www.w3schools.com/python/default.asp')

    st.text("")
    st.text("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.button('Challenge Yourself', use_container_width=True, type="primary")