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
# SESSION STATE
# =====================================================

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = ""

if "journals" not in st.session_state:
    st.session_state.journals = []

if "goals" not in st.session_state:
    st.session_state.goals = []


# =====================================================
# SIGN UP FUNCTION
# =====================================================

def signup():

    st.subheader("📝 Create Account")

    new_username = st.text_input(
        "Create Username"
    )

    new_password = st.text_input(
        "Create Password",
        type="password"
    )

    if st.button("Sign Up"):

        if new_username in st.session_state.users:

            st.error("Username already exists")

        elif new_username == "" or new_password == "":

            st.warning("Please fill all fields")

        else:

            st.session_state.users[new_username] = new_password

            st.success("Account created successfully!")


# =====================================================
# LOGIN FUNCTION
# =====================================================

def login():

    st.subheader("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username in st.session_state.users
            and
            st.session_state.users[username] == password
        ):

            st.session_state.logged_in = True

            st.session_state.current_user = username

            st.success("Login successful!")

            st.rerun()

        else:

            st.error("Invalid username or password")


# =====================================================
# AUTHENTICATION PAGE
# =====================================================

if not st.session_state.logged_in:

    st.title("🌟 Student Wellness App")

    option = st.selectbox(
        "Choose Option",
        ["Login", "Sign Up"]
    )

    if option == "Login":
        login()

    else:
        signup()

    st.stop()


# =====================================================
# LOGOUT BUTTON
# =====================================================

st.sidebar.success(
    f"Logged in as {st.session_state.current_user}"
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.session_state.current_user = ""

    st.rerun()


# =====================================================
# APP TITLE
# =====================================================

st.title("🌟 Student Productivity & Wellness App")

st.write(
    "Helping students manage stress, productivity, "
    "and motivation."
)


# =====================================================
# QUOTES
# =====================================================

quotes = [

    "You are stronger than you think.",

    "Keep going, you are improving.",

    "Believe in yourself.",

    "Small progress still matters.",

    "You can do difficult things.",

    "Stay consistent and positive."
]


# =====================================================
# MUSIC SECTION
# =====================================================

st.sidebar.title("🎧 Music")

music_choice = st.sidebar.selectbox(

    "Choose Music",

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

    st.header("📔 Daily Journal")

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

                "user": st.session_state.current_user,

                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),

                "mood": mood,

                "text": text
            })

            st.success("Journal saved!")

        else:

            st.warning("Write something first")


    st.subheader("Previous Journals")

    for j in reversed(st.session_state.journals):

        if j["user"] == st.session_state.current_user:

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

                "user": st.session_state.current_user,

                "goal": goal,

                "done": False
            })

            st.success("Goal added!")

        else:

            st.warning("Enter a goal first")


    st.subheader("Your Goals")


    for i, g in enumerate(st.session_state.goals):

        if g["user"] == st.session_state.current_user:

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