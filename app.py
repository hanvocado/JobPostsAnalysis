import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Xu hướng tuyển dụng', 
                   page_icon='📊', 
                   layout='centered',
                   initial_sidebar_state='expanded')
st.subheader('Xu hướng kỹ năng')
st.markdown('##')

fig, ax = plt.subplots()
df = pd.read_csv('top_skills_job.csv')
print(df.shape)
jobs = ['store manager', 'store leader']
jobs = df[df['job_title'].str.fullmatch(r'[a-z\s]+')]
print(jobs.shape)

st.sidebar.header('Lọc')
selected_job = st.sidebar.selectbox('Chọn công việc', options = jobs)
filtered_df = df[df['job_title'] == selected_job]

def top_skills_chart():
    print(selected_job)
    filtered_df = df[df['job_title'] == selected_job]
    top_skills = list(filtered_df['job_skills'])
    top_skills = eval(top_skills[0])
    skills, counts = zip(*top_skills)
    plt.barh(skills, counts)
    plt.xlabel('')
    plt.ylabel('Kỹ năng')
    plt.title(f'Top 5 Kỹ Năng được yêu cầu cho vị trí {selected_job}')
    ax.set_xticklabels([])
    ax.invert_yaxis()
    st.pyplot(fig, use_container_width=True)

top_skills_chart()