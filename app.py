from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "mokhles_profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Mokhles Abdelmonem CV"
PAGE_ICON = ":wave:"
NAME = "Mokhles Abdelmonem"
DESCRIPTION = """
Mid Senior Python Developer.
"""
EMAIL = "mokhlesabdelmonem@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/Mokhles-Abdelmonem",
    "LinkedIn": "https://www.linkedin.com/in/mokhles-hussain-52ba91183/",
    "hackerrank": "https://www.hackerrank.com/profile/mokhlesabdelmon1",
    "Twitter": "https://twitter.com/MokhlesAbdelmo1",

}
PROJECTS = {
    "🏆 DATA Analysis": "https://github.com/Mokhles-Abdelmonem/DATA",
    "🏆 Streamlite Visualization App": "https://github.com/Mokhles-Abdelmonem/StreamliteApp",
    "🏆 Chess Game  & TicTacToi & Rock Paper Scissors ": "hhttps://github.com/Mokhles-Abdelmonem/fastapi-react--socketio-mui-games",
}

CERTIFICATIONS = {
    "🏆 Programming for Everybody (python)": "https://drive.google.com/file/d/15O1bt95XFz7LU0nqF3POzuNfgfiEw3cH/view?usp=share_link",
    "🏆 Python Data Structures": "https://drive.google.com/file/d/1tcgmpWQyrLc319PqERIo7VNGr19-YOYC/view?usp=sharing",
    "🏆 Using Python to Access Web Data": "https://drive.google.com/file/d/1X4YiTmM8nlgBKhRRL_bukr-MsU16spR_/view?usp=sharing",
    "🏆 AI For Everyone": "https://drive.google.com/file/d/1ZnGj8qjCA0A7yAhGsCktLRdHGIu2EQCB/view?usp=sharing",

    "🏆 Python Programming Basics": "https://drive.google.com/file/d/1iCW6Bk-F7vIYynnDpxEAZwXDR4wagivU/view?usp=sharing",
    "🏆 Database Fundamentals": "https://drive.google.com/file/d/1c1i6R4pJ2A01jFGlmONletp5qxjGA5wZ/view?usp=sharing",
    "🏆 Web development challenger": "https://drive.google.com/file/d/1c6MLR_xhT1K1s50dk-c1Hw7q6SSFGkue/view?usp=sharing",
    "🏆 Data challenger track": "https://drive.google.com/file/d/1qujgmq36VSqE4-hE4JQRjXWNKZIqdQxT/view?usp=sharing",

    "🏆 Advanced Data Analysis": "https://drive.google.com/file/d/1Xmrd0BLzY0hKmsduz_CkazsOMECU1sfb/view?usp=sharing",
    "🏆 Data Analysis Professional": "https://drive.google.com/file/d/1oiyejQd6nZcLBbYahQZ7Ii0PBxDMOMUQ/view?usp=sharing",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince python backend developer
- ✔️ Strong hands on experience and knowledge in Python native
- ✔️ Good understanding of statistics and data analysis principles
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 📚 Frameworks/Libs: Django, fastapi, JQuery, React
- 👩‍💻 Tools/Libs: Git, Celery, Scrapy, selenium, pandas, NumPy, streamlit, socketio
- 👩‍💻 Advanced tools: microservices architecture, grpcs, websocket, redis, kafka
- 📊 Data Visulization: matplotlib, streamlit, tableau
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Backend Developer | Tawasol Map**")
st.write("February 2023 – Present")
st.write(
    """
- ► live streaming for a stratigic game similar to mafia city.
- ► Used python websocket and redis to create backend server with MVC structure built in from scratch.
- ► applyed microservices architecture using grpcs framework.
- ► handling scheduler events by built in event system.
- ► asynchronous programing
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**FreeLancing & self project**")
st.write("no specific timeline")
st.write(
    """
- ► Data Analysis: Web Project apply data analysis principles (cleaning & visualization)
- ► Simulator: delivery drivers with steaming live  data of the location, google api integration and socketio
- ► Fixing & updates: Educational django app
- ► odoo app: erp system
- ► ai applications: face recognition & verification,  
- ► Neural Networks learning: building micrograd, building makemore
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Backend Developer | Duty ltd**")
st.write("Jan 2022 - October 2022")
st.write(
    """
- ► developing web project deliver a sets of Cyber security tools that test the security of the websites and tracking the founded Security vulnerabilities
- ► applyed tools: Django , Rest Api , celery for handling heavy tasks, channels, elasticsearch, beautifulsoup4, httpx, Scrapy, selenium, the main tools executed by bash commands
"""
)


# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write("---")
st.write(
    """
Bachelor of agricultural engineering – jun 2020
Cairo University GPA 2.8
"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
for project, link in CERTIFICATIONS.items():
    st.write(f"[{project}]({link})")



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
