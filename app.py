#Necessary File Imports
from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css = current_dir/"styles"/"main.css"
resume = current_dir/"assets"/"CV.pdf"
photo = current_dir/"assets"/"avatar.png"

#general setting 
TITLE = "Digital CV | Mo Alim"
PAGE_ICON = ":wave:"
NAME = "Alim Mo"
DESCRIPTION =  """ 
Front-End Developer | Data Analyst
"""
EMAIL = "alimalim77@gmail.com"

SOCIAL_MEDIA = {
    "Youtube" : "https://youtube.com/@codebroski",
    "LinkedIn" : "https://linkedin.com/in/alimalim77",
}

PROJECTS = {
    "Drink Water Notifier - Desktop App to notify the user" : "",
    "User Profile Generator - Web App to fetch user information" : "",
    "Restaurant Management System" : "Review feature, User authentication and order tracking",

}

st.set_page_config(page_title=TITLE,page_icon =PAGE_ICON)
st.title("Hola Amigoz!")

#--Load CSS, PDF and PIC
with open(css) as styleFile:
    st.markdown("<style>{}<style>".format(styleFile.read()),unsafe_allow_html=True)
with open(resume,"rb") as resumeFile:
    pdf = resumeFile.read()
    image = Image.open(photo)

#INFO SECTION
c1,c2 = st.columns(2,gap="small")
with c1:
    st.image(image,width=230)

with c2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=pdf,
        file_name=resume.name,
        mime="application/octet-stream",
    )
    st.write("Connect @ ",EMAIL)


#SOCIAL HANDLES
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#EXPERIENCE
st.write("#")
st.subheader("Experience and Qualifications")
st.write("""
:one: Worked as a Technical Content Engineer @ GeeksForGeeks \n
:two: Worked as a Mentor @ GeeksforGeeks
""")


#SKILLS
st.write("#")
st.subheader("Hard Skills")
st.write("""
-*Programming Languages* - Python, C++, Javascript \n
-*Libraries* - Numpy, Pandas, Flask, Streamlit, React \n
-*Databases* - MySQL, Postgre 
""")


#PROJECTS
st.write("#")
st.subheader("Projects")

for project, link in PROJECTS.items():
    st.write(f"[{project}](link)")

