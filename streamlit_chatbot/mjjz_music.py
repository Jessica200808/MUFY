import streamlit as st
import random
from datetime import datetime


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Student Wellness App",
    page_icon="🌟",
    layout="centered"
)


# =====================================================
# SIMPLE USER ACCOUNT
# =====================================================

# Example account
USERNAME = "student"
PASSWORD = "1234"


# =====================================================
# LOGIN SESSION
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =====================================================
# LOGIN FUNCTION
# =====================================================

def login():

    st.title("🔐 Login System")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True

            st.success("Login successful!")

            st.rerun()

        else:

            st.error("Wrong username or password")


# =====================================================
# IF NOT LOGGED IN
# =====================================================

if not st.session_state.logged_in:

    login()

    st.stop()


# =====================================================
# LOGOUT BUTTON
# =====================================================

st.sidebar.success("Logged in")

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()


# =====================================================
# APP TITLE
# =====================================================

st.title("🌟 Student Productivity & Wellness App")

st.write(
    "Helping students manage stress, goals, "
    "and motivation."
)


# =====================================================
# SESSION STORAGE
# =====================================================

if "journals" not in st.session_state:
    st.session_state.journals = []

if "goals" not in st.session_state:
    st.session_state.goals = []


# =====================================================
# QUOTES
# =====================================================

quotes = [

    "You are stronger than you think.",

    "Small progress still matters.",

    "Believe in yourself.",

    "Keep going.",

    "Your future is bright.",

    "You can do difficult things."
]


# =====================================================
# MUSIC SECTION
# =====================================================

st.sidebar.title("🎧 Music")

music_choice = st.sidebar.selectbox(

    "Choose music",

    [
        "None",
        "🌿 Calm",
        "😊 Happy",
        "✨ Satisfying"
    ]
)


music_links = {

    "🌿 Calm":
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",

    "😊 Happy":
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",

    "✨ Satisfying":
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
}


if music_choice != "None":

    st.sidebar.success(f"Playing {music_choice}")

    st.audio(music_links[music_choice])


# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3 = st.tabs([

    "📔 Journal",

    "🎯 Bucket List",

    "✨ Motivation"
])


# =====================================================
# JOURNAL
# =====================================================

with tab1:

    st.header("📔 Journal")

    mood = st.selectbox(

        "Mood",

        [
            "😊 Happy",
            "😐 Okay",
            "😔 Sad",
            "😡 Angry",
            "😵 Stressed"
        ]
    )

    text = st.text_area("Write your thoughts")


    if st.button("Save Journal"):

        if text.strip():

            st.session_state.journals.append({

                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),

                "mood": mood,

                "text": text
            })

            st.success("Journal saved!")

        else:

            st.warning("Write something first")


    st.subheader("Previous Journals")

    for j in reversed(st.session_state.journals):

        st.write(f"**{j['mood']} | {j['date']}**")

        st.write(j["text"])

        st.divider()


# =====================================================
# BUCKET LIST
# =====================================================

with tab2:

    st.header("🎯 Bucket List")

    goal = st.text_input("Add a goal")


    if st.button("Add Goal"):

        if goal.strip():

            st.session_state.goals.append({

                "goal": goal,

                "done": False
            })

            st.success("Goal added!")

        else:

            st.warning("Enter a goal first")


    st.subheader("Your Goals")


    for i, g in enumerate(st.session_state.goals):

        checked = st.checkbox(

            g["goal"],

            value=g["done"],

            key=i
        )

        if checked and not g["done"]:

            st.balloons()

            st.success(random.choice(quotes))

        st.session_state.goals[i]["done"] = checked


# =====================================================
# MOTIVATION
# =====================================================

with tab3:

    st.header("✨ Motivation")

    if st.button("Generate Quote"):

        st.success(random.choice(quotes))

    st.info(
        "Take care of your mental health 💙"
    )