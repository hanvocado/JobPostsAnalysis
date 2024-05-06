import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]

st.set_page_config(page_title='Xu hướng tuyển dụng',
                   page_icon='📊',
                   layout='centered',
                   initial_sidebar_state='expanded')

colors = ['#1b9e77', '#a9f971', '#fdaa48', '#6890F0', '#A890F0']

df_top_jobs = pd.read_csv('top_jobs_country.csv')
df_top_skills = pd.read_csv('top_skills_job.csv')

selected_country = st.sidebar.selectbox('Quốc gia', options=df_top_jobs['search_country'], index=None)
st.sidebar.divider()
job_input = st.sidebar.text_input(label='Công việc', placeholder='Teacher')

job_input = job_input.lower()
filtered_jobs = df_top_skills[df_top_skills['job_title'].str.startswith(job_input)]
selected_job = ''
if filtered_jobs.shape[0] > 0:
    jobs = {s: levenshtein_distance(s, job_input) for s in filtered_jobs['job_title']}
    selected_job = min(jobs, key=jobs.get)

def top_skills_chart(selected_job):
    job = df_top_skills[df_top_skills['job_title'] == selected_job].iloc[0]
    top_skills = eval(job['job_skills'])
    skills, counts = zip(*top_skills)

    fig, ax = plt.subplots()
    plt.grid(color='#f0f2f6', linestyle='--', alpha=0.7)
    ax.barh(skills, counts, color=colors, height=0.6)
    ax.set_xlabel('Độ cần thiết')
    ax.set_ylabel('Kỹ năng')
    ax.set_title(f'Top 5 Kỹ Năng được yêu cầu cho vị trí {selected_job.upper()}')
    ax.set_xticklabels([])
    ax.invert_yaxis()
    st.pyplot(fig, use_container_width=True)

def top_jobs_chart(selected_country):
    filtered_df_country = df_top_jobs[df_top_jobs['search_country'] == selected_country]
    top_jobs = list(filtered_df_country['job_title'])
    top_jobs = eval(top_jobs[0])
    jobs, counts = zip(*top_jobs)

    fig, ax = plt.subplots()
    plt.grid(color='#f0f2f6', linestyle='--', alpha=0.7)
    ax.barh(jobs, counts, color=colors)
    ax.set_xlabel('Số lượng bài đăng tuyển')
    ax.set_ylabel('Công việc')
    ax.set_title(f'Top 10 công việc được đăng tuyển tại {selected_country.capitalize()}')
    ax.invert_yaxis()
    st.pyplot(fig, use_container_width=True)

tab1, tab2 = st.tabs(["Việc làm", "Kĩ năng"])

with tab1:
    st.subheader('Xu hướng việc làm')
    if selected_country != None:
        top_jobs_chart(selected_country)
    else:
        st.text('Vui lòng chọn quốc gia để xem')

with tab2:
    st.subheader('Xu hướng kỹ năng')
    if selected_job != '':
        top_skills_chart(selected_job)
    elif selected_job == '' and job_input != '':
        st.text('Không tìm thấy công việc này, vui lòng thử lại.')