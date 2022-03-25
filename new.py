import streamlit as st

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

with st.sidebar:
    my_component(greeting="hello")