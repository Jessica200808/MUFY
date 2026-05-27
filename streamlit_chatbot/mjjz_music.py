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
# TITLE
# =====================================================

st.title("🌟 Student Productivity & Wellness App")

st.write("Manage stress, goals, and motivation in one place.")


# =====================================================
# SESSION STATE
# =====================================================

if "journals" not in st.session_state:
    st.session_state.journals = []

if "goals" not in st.session_state:
    st.session_state.goals = []


# =====================================================
# QUOTES
# =====================================================

quotes = [
    "You are doing better than you think.",
    "Small progress is still progress.",
    "Believe in yourself.",
    "Keep going, you are improving.",
    "You can do hard things.",
    "Your future is bright.",
    "Stay consistent and strong."
]


# =====================================================
# SIDEBAR - MUSIC SECTION
# =====================================================

st.sidebar.title("🎧 Focus Music")

music_choice = st.sidebar.selectbox(
    "Choose music mood",
    ["None", "🌿 Calm", "😊 Happy", "✨ Satisfying"]
)


# =====================================================
# MUSIC LINKS (SIMPLE & SAFE)
# =====================================================

music_links = {
    "🌿 Calm": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "😊 Happy": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "✨ Satisfying": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
}


if music_choice != "None":

    st.sidebar.success(f"Playing: {music_choice}")

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
        ["😊 Happy", "😐 Okay", "😔 Sad", "😡 Angry", "😵 Stressed"]
    )

    text = st.text_area("Write your thoughts")

    if st.button("Save Journal"):

        if text.strip():

            st.session_state.journals.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mood": mood,
                "text": text
            })

            st.success("Saved!")
            st.balloons()

        else:
            st.warning("Write something first")


    st.divider()

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

    goal = st.text_input("Add a new goal")

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

    st.info("Take care of your mental health 💙") 