import pandas as pd
df = pd.read_csv("studentmarks.csv")

pass_marks = {
    'math_score': 50,
    'reading_score': 60,
    'writing_score': 55,
    'science_score': 60,
    'history_score': 60
}

for subject, pass_mark in pass_marks.items():
    df = df[df[subject] >= pass_mark]
    
df['total_marks'] = df[['math_score', 'reading_score', 'writing_score', 'science_score', 'history_score']].sum(axis=1)
    
# print(df[['student_name','total_marks']])

df_sorted = df.sort_values(by='total_marks',ascending=False)
# print(df_sorted)
print(df_sorted.head(3))
