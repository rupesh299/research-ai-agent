import streamlit as st
from agent import research

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔍"
)

st.title("🔍 AI Research Agent")

query = st.text_input(
    "Enter research topic"
)

if st.button("Research"):

    with st.spinner("Researching..."):

        report = research(query)

        st.markdown(report)