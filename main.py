import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

linkedin_job_posting = pd.read_csv('./linkedin_job_posting_skills.csv')
list_country = linkedin_job_posting['search_country']
selected_country = st.selectbox("Chọn quốc gia", list_country.unique())
selected_country_jobs = linkedin_job_posting[list_country == selected_country]

# count of each unique job title in the selected_country_jobs DataFrame.
job_counts = selected_country_jobs['job_title'].value_counts()
# new data frame, contains top 10 job titles
top_10_country_jobs = job_counts.head(10)

# creating a horizontal bar graph
top_10_country_jobs_values = top_10_country_jobs.index.tolist()
top_10_country_jobs_titles = top_10_country_jobs.tolist()

fig, ax = plt.subplots()
ax.barh(top_10_country_jobs_values, top_10_country_jobs_titles)
ax.set(title=f'Top 10 nhu cầu việc làm ở {selected_country}',
       xlabel='Số lượng bài đăng tuyển', ylabel="Công việc")
ax.invert_yaxis()
st.pyplot(fig)
