import streamlit as st

from components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## Hoe werkt De Lesplanner?\n"
            "1. Upload een pdf, docx, of txt file📄\n"
            "2. Stel je vraag over het document 💬\n"
            "3. Laat Berend je lesplan maken\n"
        )
        api_key_input = os.environ.get("OPENAI_API_KEY", None) or st.session_state.get("OPENAI_API_KEY", "") 
        
        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖Berend-Botje's - De Lesplanner helpt docenten bij het maken van een lesplan."
            "Hierbij kan Berend gebruik maken van de documenten die zijn toegevoegd.  "
        )
        st.markdown(
            "This tool is a work in progress. "
            )
        st.markdown("")
        st.markdown("---")

        faq()
