import streamlit as st
from openai import OpenAI


# =====================================
# OPENAI CLIENT
# =====================================

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


# =====================================
# PAGE SETTINGS
# =====================================

st.set_page_config(
    page_title="AI Friend",
    page_icon="🤖"
)


# =====================================
# TITLE
# =====================================

st.title("🤖 AI Friend App")

st.write(
    "Talk to your AI assistant."
)


# =====================================
# USER INPUT
# =====================================

user_message = st.text_area(
    "Type your message"
)


# =====================================
# AI FUNCTION
# =====================================

def ask_ai(message):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content": (
                    "You are a kind, supportive, "
                    "and motivational AI friend."
                )
            },

            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content


# =====================================
# BUTTON
# =====================================

if st.button("Ask AI"):

    if user_message != "":

        with st.spinner("AI is thinking..."):

            reply = ask_ai(user_message)

        st.success("AI Reply")

        st.write(reply)

    else:

        st.warning("Please type a message.")