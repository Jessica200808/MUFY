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

st.write(
    "A simple app to help students manage stress, "
    "stay productive, and stay motivated."
)


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
# SIDEBAR (MUSIC + NAV)
# =====================================================

st.sidebar.title("🎧 Settings")

play_music = st.sidebar.checkbox("Play calming music")

st.sidebar.write("Navigate using tabs below 👇")


# OPTIONAL MUSIC
if play_music:
    st.sidebar.success("Focus mode ON 🎧")

    st.audio(
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    )


# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3 = st.tabs([
    "📔 Journal",
    "🎯 Bucket List",
    "✨ Motivation"
])


# =====================================================
# JOURNAL TAB
# =====================================================

with tab1:

    st.header("📔 Daily Journal")

    mood = st.selectbox(
        "How are you feeling?",
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

            st.success("Journal saved!")
            st.balloons()

        else:
            st.warning("Please write something first")


    st.divider()

    st.subheader("Previous Journals")

    for j in reversed(st.session_state.journals):

        st.markdown(f"**{j['mood']} | {j['date']}**")
        st.write(j["text"])
        st.divider()


# =====================================================
# BUCKET LIST TAB
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
# MOTIVATION TAB
# =====================================================

with tab3:

    st.header("✨ Daily Motivation")

    st.write("Click to get motivation")

    if st.button("Generate Quote"):

        st.success(random.choice(quotes))

    st.info("Take care of your mental health. You matter 💙")