import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize session state
if "reply" not in st.session_state:
    st.session_state.reply = ""

def get_response(prompt):
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat.choices[0].message.content

def send_message(user_input):
    if user_input.strip():
        with st.spinner("Thinking..."):
            st.session_state.reply = get_response(user_input)

# Page setup
st.set_page_config(
    page_title="Free AI Chatbot",
    page_icon="💬",
    layout="wide"
)

# Background styling (UNCHANGED)
st.markdown("""
    <style>
        .main {background-color: #000000;}
        .chat-box {
            border-radius: 12px;
            background: white;
            padding: 22px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.07);
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            font-size: 15px;
            color: #555;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            margin-top: 50px;
            color: #888;
        }
        div[data-testid="stForm"] {
        border: none;
        padding: 0;
        background: transparent;
}

    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💬 ChatSphere</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your personal AI conversation world</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Made with ❤️ using Streamlit and Groq API</div>", unsafe_allow_html=True)
st.write("")

# Chat UI layout
with st.container():

    with st.form("chat_form", clear_on_submit=True):

        user_input = st.text_input(
            "Your message",
            placeholder="Type your message here..."
        )

        submitted = st.form_submit_button(
            "Send",
            type="primary",
            use_container_width=True
        )

        if submitted:
            send_message(user_input)

    if st.session_state.reply:
        st.write("### Response")
        st.success(st.session_state.reply)

st.markdown("""
<div style='text-align:center; color:#000000; margin-top:45px; font-size:14px;'>
✨ Created by <span style='color:#000000;'>Utkarsh Srivastav</span> ✨
</div>
""", unsafe_allow_html=True)
