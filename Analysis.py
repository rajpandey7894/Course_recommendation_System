import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('course_learning_dataset.csv')

# Set the style
sns.set(style='whitegrid', palette='pastel')

# Calculate metrics
avg_rating = df.groupby('course_id')['rating'].mean().reset_index().rename(columns={'rating': 'avg_rating'})
popularity = df.groupby('course_id').size().reset_index(name='num_ratings')
avg_time_spent = df.groupby('course_id')['time_spent_hours'].mean().reset_index().rename(columns={'time_spent_hours': 'avg_time_spent'})

# Merge the data
course_insights = avg_rating.merge(popularity, on='course_id').merge(avg_time_spent, on='course_id')

# Prepare data for the top courses
top_rated = course_insights.sort_values(by='avg_rating', ascending=False).head(10)
most_popular = course_insights.sort_values(by='num_ratings', ascending=False).head(10)

# Create a dashboard layout
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# Top-rated courses plot
sns.barplot(y='course_id', x='avg_rating', data=top_rated, ax=axes[0, 0], palette='Blues_d')
axes[0, 0].set_title('Top 10 Rated Courses')
axes[0, 0].set_xlabel('Average Rating')
axes[0, 0].set_ylabel('Course ID')
axes[0, 0].invert_yaxis()

# Most popular courses plot
sns.barplot(y='course_id', x='num_ratings', data=most_popular, ax=axes[0, 1], palette='Greens_d')
axes[0, 1].set_title('Top 10 Most Popular Courses')
axes[0, 1].set_xlabel('Number of Ratings')
axes[0, 1].set_ylabel('Course ID')
axes[0, 1].invert_yaxis()

# Pie chart for time spent distribution among top-rated courses
time_data = top_rated['avg_time_spent']
time_labels = top_rated['course_id']
axes[1, 0].pie(time_data, labels=time_labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
axes[1, 0].set_title('Average Time Spent on Top 10 Rated Courses')

# Scatter plot for rating vs. time spent
sns.scatterplot(x='avg_rating', y='avg_time_spent', size='num_ratings', sizes=(20, 200), data=course_insights, ax=axes[1, 1], palette='cool')
axes[1, 1].set_title('Rating vs. Time Spent')
axes[1, 1].set_xlabel('Average Rating')
axes[1, 1].set_ylabel('Average Time Spent (hours)')

# Adjust layout
plt.tight_layout()
plt.suptitle('Course Insights Dashboard', y=1.02, fontsize=16)
plt.show()
