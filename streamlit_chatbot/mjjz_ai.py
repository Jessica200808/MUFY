import streamlit as st
import random
from datetime import datetime
from openai import OpenAI


# ======================================
# OPENAI API KEY
# ======================================

# Replace with your OpenAI API key
# Get one from:
# https://platform.openai.com/

client = OpenAI(
    api_key="YOUR_API_KEY_HERE"
)


# ======================================
# PAGE SETTINGS
# ======================================

st.set_page_config(
    page_title="My Life App",
    page_icon="🌟"
)


# ======================================
# APP TITLE
# ======================================

st.title("🌟 My Life App")

st.write(
    "Journal your thoughts, complete goals, "
    "and talk to AI for support."
)


# ======================================
# SESSION STORAGE
# ======================================

# Save journals temporarily
if "journals" not in st.session_state:
    st.session_state.journals = []

# Save goals temporarily
if "goals" not in st.session_state:
    st.session_state.goals = []


# ======================================
# POSITIVE QUOTES
# ======================================

quotes = [

    "You are stronger than you think.",

    "Keep going. You are improving.",

    "Believe in yourself.",

    "Every day is a fresh start.",

    "You can do hard things.",

    "Small progress still matters."
]


# ======================================
# AI FUNCTION
# ======================================

def ask_ai(user_message):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content": (
                    "You are a kind and supportive AI friend. "
                    "Help users feel motivated, calm, and supported."
                )
            },

            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response.choices[0].message.content


# ======================================
# CREATE TABS
# ======================================

tab1, tab2, tab3 = st.tabs([
    "📔 Journal",
    "🎯 Bucket List",
    "🤖 AI Support"
])


# ======================================
# JOURNAL TAB
# ======================================

with tab1:

    st.header("Daily Journal")

    journal_text = st.text_area(
        "Write about your day"
    )

    mood = st.selectbox(
        "Choose your mood",
        [
            "😊 Happy",
            "😐 Okay",
            "😔 Sad",
            "😡 Angry"
        ]
    )

    if st.button("Save Journal"):

        st.session_state.journals.append({

            "date": str(datetime.now()),

            "mood": mood,

            "text": journal_text
        })

        st.success("Journal saved!")


    # Show previous journals
    st.subheader("Previous Entries")

    for entry in reversed(st.session_state.journals):

        st.markdown(f"### 📅 {entry['date']}")

        st.write(entry["mood"])

        st.write(entry["text"])

        st.divider()


# ======================================
# BUCKET LIST TAB
# ======================================

with tab2:

    st.header("Bucket List")

    goal = st.text_input(
        "Enter a new goal"
    )

    if st.button("Add Goal"):

        st.session_state.goals.append({

            "goal": goal,

            "completed": False
        })

        st.success("Goal added!")


    # Show goals
    st.subheader("Your Goals")

    for i, item in enumerate(st.session_state.goals):

        checked = st.checkbox(
            item["goal"],
            value=item["completed"],
            key=i
        )

        # If completed
        if checked and not item["completed"]:

            st.balloons()

            quote = random.choice(quotes)

            st.success(
                f"🎉 Goal completed!\n\n✨ {quote}"
            )

        # Update status
        st.session_state.goals[i]["completed"] = checked


# ======================================
# AI SUPPORT TAB
# ======================================

with tab3:

    st.header("Talk to AI")

    st.write(
        "Share your problems, stress, or feelings."
    )

    user_message = st.text_area(
        "What would you like help with?"
    )

    if st.button("Ask AI"):

        if user_message != "":

            with st.spinner("AI is thinking..."):

                ai_reply = ask_ai(user_message)

            st.markdown("### 🤖 AI Reply")

            st.write(ai_reply)

        else:

            st.warning("Please type something first.")