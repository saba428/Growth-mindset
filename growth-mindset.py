#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="✨")
st.title("Growth Mindset Challenge: web App with streamlit ")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace Challenges , Learn from mistakes , and unlock your full potential. ths AI-powered app help you build a growth mindset with reflection, chalenges, and achievements!💰")

#quote section
st.header("💡 Today's Growth Journey!")
st.write("Success is not Final, Failure is not Fatal: it is the coutage to continue that counts.-Winston churchill")

st.header("🔧 what's Your chalenges Today?")
user_input = st.text_input("Describe a your're facing:")

#condition
if user_input:
    st.succes(f"💪You're facing:{user_input}. Keep pushing forward towards your goal!🚀 ")

#reflexing
st.header(" Reflect on your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"🌟Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience help you grow! share your difficulties")

#achievements
st.header("🏆 Celebrate Your wins!")
achievements = st.text_input("Share something you're recently accomplished:")

if achievements:
    st.success(f"🚀 Amazing! You achieved: {achievements}")
else:
    st.info("Big or small , every acheivements count! share one now 😇")


#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journy, not a destination! 🌟")
st.write("** ⛔ create by SABA NAZ**")
