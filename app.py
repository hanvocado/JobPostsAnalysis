# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(page_title='Xu hướng tuyển dụng',
#                    page_icon='📊',
#                    layout='centered',
#                    initial_sidebar_state='expanded')

# tab1, tab2 = st.tabs(["Việc làm", "Kĩ năng"])
# with tab1:
#     st.subheader('Xu hướng việc làm')
#     st.markdown('##')

#     fig, ax = plt.subplots()
#     df_top_jobs = pd.read_csv('top_jobs_country.csv')
#     top_jobs_chart()

# with tab2:
#     st.subheader('Xu hướng kỹ năng')
#     st.markdown('##')

#     fig, ax = plt.subplots()
#     df = pd.read_csv('top_skills_job.csv')
#     print(df.shape)
#     jobs = ['store manager', 'store leader']
#     jobs = df[df['job_title'].str.fullmatch(r'[a-z\s]+')]
#     print(jobs.shape)
#     top_skills_chart()

# #Side bar
# st.sidebar.header('Lọc')
# countries = df_top_jobs['search_country']
# selected_country = st.sidebar.selectbox('Chọn quốc gia', options=countries.unique())
# filtered_df_country = df_top_jobs[countries == selected_country]

# selected_job = st.sidebar.selectbox('Chọn công việc', options=jobs)
# filtered_df = df[df['job_title'] == selected_job]

# def top_skills_chart():
#     print(selected_job)
#     filtered_df = df[df['job_title'] == selected_job]
#     top_skills = list(filtered_df['job_skills'])
#     top_skills = eval(top_skills[0])
#     skills, counts = zip(*top_skills)
#     plt.barh(skills, counts)
#     plt.xlabel('')
#     plt.ylabel('Kỹ năng')
#     plt.title(f'Top 5 Kỹ Năng được yêu cầu cho vị trí {selected_job}')
#     ax.set_xticklabels([])
#     ax.invert_yaxis()
#     st.pyplot(fig, use_container_width=True)

# def top_jobs_chart():
#     print(selected_country)
#     top_jobs = list(filtered_df_country['job_title'])
#     top_jobs = eval(top_jobs[0])
#     jobs, counts = zip(*top_jobs)
#     plt.barh(jobs, counts)
#     plt.xlabel('Số lượng bài đăng tuyển')
#     plt.ylabel('Công việc')
#     plt.title(f'Top 10 công việc được đăng tuyển tại {str(selected_country).capitalize()}')
#     ax.invert_yaxis()
#     st.pyplot(fig, use_container_width=True)

# top_jobs_chart()
# top_skills_chart()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Config Page
st.set_page_config(page_title='Xu hướng tuyển dụng',
                   page_icon='📊',
                   layout='centered',
                   initial_sidebar_state='expanded')

# Read Data
df_top_jobs = pd.read_csv('top_jobs_country.csv')
df = pd.read_csv('top_skills_job.csv')

# Sidebar
st.sidebar.header('Lọc')
countries = df_top_jobs['search_country']
selected_country = st.sidebar.selectbox('Chọn quốc gia', options=countries.unique())
filtered_df_country = df_top_jobs[df_top_jobs['search_country'] == selected_country]

jobs = ['store manager', 'store leader']
jobs = df[df['job_title'].str.fullmatch(r'[a-z\s]+')]
print(jobs.shape)
selected_job = st.sidebar.selectbox('Chọn công việc', options=jobs)
filtered_df = df[df['job_title'] == selected_job]

# Visualize function
def top_skills_chart(selected_job, df):
    print(selected_job)
    filtered_df = df[df['job_title'] == selected_job]
    top_skills = list(filtered_df['job_skills'])
    top_skills = eval(top_skills[0])
    skills, counts = zip(*top_skills)

    fig, ax = plt.subplots()
    ax.barh(skills, counts)
    ax.set_xlabel('')
    ax.set_ylabel('Kỹ năng')
    ax.set_title(f'Top 5 Kỹ Năng được yêu cầu cho vị trí {selected_job}')
    ax.set_xticklabels([])
    ax.invert_yaxis()
    st.pyplot(fig, use_container_width=True)


def top_jobs_chart(selected_country, filtered_df_country):
    top_jobs = list(filtered_df_country['job_title'])
    top_jobs = eval(top_jobs[0])
    jobs, counts = zip(*top_jobs)

    fig, ax = plt.subplots()
    ax.barh(jobs, counts)
    ax.set_xlabel('Số lượng bài đăng tuyển')
    ax.set_ylabel('Công việc')
    ax.set_title(f'Top 10 công việc được đăng tuyển tại {selected_country.capitalize()}')
    ax.invert_yaxis()
    st.pyplot(fig, use_container_width=True)


# Create tabs
tab1, tab2 = st.tabs(["Việc làm", "Kĩ năng"])

with tab1:
    st.subheader('Xu hướng việc làm')
    top_jobs_chart(selected_country, filtered_df_country)

with tab2:
    st.subheader('Xu hướng kỹ năng')
    top_skills_chart(selected_job, df)
