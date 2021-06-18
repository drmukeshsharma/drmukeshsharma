import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('StudentsPerformance.csv')
data
data.dtypes #to get data types
data.head() #to see the first 5 rows
data.tail() # to see the last 5 rows
data.describe()
data.info()
data.columns # to get the column headings
data.shape # to get the shape
data.nunique() # to get the unique values
data['gender'].unique() # to get the unique values in gender column
data.isnull()
data.isnull().sum() # to find the number of null values
data.rename(columns={"race/ethnicity":"race_ethnicity",
                   "parental level of education":"education_level",
                   "test preparation course":"prep_course",
                   "math score":"math_score",
                   "reading score":"reading_score",
                   "writing score":"writing_score"}) # to rename the column names
data
data.describe()
df=data.drop(['race/ethnicity','parental level of education'], axis=1)
df
corre=df.corr() # to find correlation
corre
sns.heatmap(corre,xticklabels=corre.columns, yticklabels=corre.columns,annot=True) # to get the heatmap of correlation
sns.pairplot(df)
sns.boxplot(x=df['math score'])
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df['math score'], df['reading score'])
ax.set_xlabel('math score')
ax.set_ylabel('reading score')
plt.show()
plt.rcParams['figure.figsize'] = (20, 10)
sns.countplot(df['math score'], palette = 'dark')
plt.title('Math Score',fontsize = 20)
plt.show()
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)
plt.subplot(141)
plt.title('Math Scores')
sns.violinplot(y='math score',data=df,color='m',linewidth=2)
plt.show()
plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)
plt.subplot(131)
plt.title('Math Scores')
sns.barplot(x="gender", y="math score", data=df)
df['total marks']=df['math score']+df['reading score']+df['writing score']
df['percentage']=df['total marks']/300*100
def determine_grade(scores):
    if scores >= 85 and scores <= 100:
        return 'Grade A'
    elif scores >= 70 and scores < 85:
        return 'Grade B'
    elif scores >= 55 and scores < 70:
        return 'Grade C'
    elif scores >= 35 and scores < 55:
        return 'Grade D'
    elif scores >= 0 and scores < 35:
        return 'Grade E'
    
df['grades']=df['percentage'].apply(determine_grade)
df.shape
df
df['grades'].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()
duplicate_rows_df= df[df.duplicated()]
print("number of duplicate rows: ",duplicate_rows_df.shape)
