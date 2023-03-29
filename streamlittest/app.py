import streamlit as st

st.title('This is a title')

st.markdown('This is a markdown')

number_inp = st.number_input('Number Input', min_value=10)
selbox = st.selectbox('Select Box', ('1','2','3'))

if st.button('Plus'):
    st.markdown(f'{int(number_inp)+int(selbox)}')

if st.button('Minus'):
    st.markdown(f'{int(number_inp)-int(selbox)}')

