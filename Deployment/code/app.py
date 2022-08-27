import streamlit as st


st.title('Classification Model')
st.write('Logistic Regression')

slider_val = st.sidebar.slider('Slide me', min_value=0, max_value=10)
st.write(f'You selected {slider_val}')

radio_val = st.sidebar.radio('Radio', [1,2,3])
st.write(f'You selected {radio_val}')

select_val = st.sidebar.selectbox ('Select', ['Apple','Orange','Grapes'])
st.write(f'You selected {select_val}')
