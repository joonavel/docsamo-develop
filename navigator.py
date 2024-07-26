import streamlit as st
from utils import switch_page, show_sidebar


if st.button("Choice"):
    switch_page("choice")

show_sidebar()