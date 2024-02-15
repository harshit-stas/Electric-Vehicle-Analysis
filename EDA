#importing python libraries like pandas ,numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#loading our dataset using pandas
db=pd.read_csv(r"C:\Users\hrama\Downloads\Electric_Vehicle_Population_Data.csv")


#exploring data
db.head()
db.columns
db.dtypes

db[['Model Year','Legislative District','2020 Census Tract']].skew()

#trying to find out number of unique values in each column by iterating column
values={}
for col in db.columns:
    unique_count=db[col].nunique()
    values[col]=unique_count
    print(values)
db.isnull().sum()


#dropping unnecessary columns
db=db.drop(columns=["VIN (1-10)","Postal Code","DOL Vehicle ID"])
db['Legislative District'].count()
db=db.dropna(subset=["Legislative District"])
db=db.dropna(subset=["Vehicle Location"])
db['Electric Vehicle Type'].unique()
db['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].unique()
db=db.drop(columns=['State'])
db.dtypes
db['Legislative District'].describe()


#for checking ev distribution we have made new variable
ev_dist=db[["Model Year",'Make',"Model"]]



#distribution of ev by make
top_makes=ev_dist['Make'].value_counts().nlargest(20).sort_values()
plt.figure(figsize=(10,8))
top_makes.plot(kind='bar')
plt.title("Distribution of EVs by make ")
plt.xlabel("EV's make")
plt.xticks(rotation=30)
for index,value in enumerate(top_makes):
    plt.text(index,value,str(value),ha='center',va='bottom')
plt.show()

#distribution of ev by model
model_dist=db['Model'].value_counts().nlargest(20)
plt.figure(figsize=(10,8))
sorted_values=model_dist.sort_values()
sorted_values.plot(kind='bar')
plt.title("distribution of EVs by model")
plt.xticks(rotation=30)
for index,value in enumerate(sorted_values):
    plt.text(index,value,str(value),ha='center',va='bottom')
plt.show()



#distribution of EVs by year
plt.figure(figsize=(10,8))
sorted_counts=db['Model Year'].value_counts().nlargest(10).sort_values()
sorted_counts.plot(kind='bar')
for index,values in enumerate(sorted_counts):
    plt.text(index,values,str(values),ha='center',va='bottom')
plt.title("Distribution of EVs by year")
plt.show()



# Group by 'Model Year' and 'Make' and count the number of occurrences
make_l=db[['Model Year','Make']].value_counts().nlargest(20).sort_values()
make_l=make_l.reset_index()
make_l.columns=['Model Year','Make','count']
pivot_df = make_l.pivot(index='Model Year', columns='Make', values='count')
pivot_df.plot(kind='line', stacked=True)
plt.xlim(left=2014,right=2023)
plt.xlabel('Model Year')
plt.ylabel('Count')
plt.title('Count of Each Make Over the Model Year')
plt.show()
