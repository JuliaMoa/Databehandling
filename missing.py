import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from data_utils import barplot_with_missing_values_columns

data = r"\Users\jubel\REPON\Databehandling\student-mat-missing-data.csv"
df = pd.read_csv(data)

#c)Create a function that takes in a DataFrame as input parameter and plots a barplot with the columns that have missing values. 
#Put this function into a file called data_utils.py. ---> done

#d) Now import your function from the module data_utils and use it to visualize NaNs in your dataset.
#barplot_with_missing_values_columns(df)

#e) Find all rows where the freetime is NaN. 

nan_freetime = df[df["freetime"].isna()]

#f) Find all rows where the freetime or the age is NaN.
nan_freetime_or_age = df[df[["freetime", "age"]].isna().any(axis=1)]
print(nan_freetime_or_age) 

#g) You will notice that some rows have several NaNs. Now compute the proportion that these rows constitute of the whole dataset.

rows_with_more_than_one_nan = df[df.isna().sum(axis=1) > 1]
proportion_several_missing = len(rows_with_more_than_one_nan) / len(df)
print(f"The proportion of rows with more than one missing value is: {proportion_several_missing :.4f}")

# a) As you have conversed with a domain expert you both agree that there are too many missing data to fill in 
# and the proportion is small enough to be safe to just remove.
# Now remove these rows and use your missing-value utility function visualize the remaining NaNs.

df = df[df.isna().sum(axis=1) <= 1].reset_index(drop=True) #keep only the rows with one or less Nan per row
print(df)

#bThe domain expert has told you that you have to fill in the missing age values. 
# Start with visualising the age distribution in the dataset using a histogram.

sns.set_style("darkgrid")
sns.histplot(x = "age", data = df)
plt.show()

#c) Check which columns there are in the dataset to see what can be utilised in determining the age.
print(df.columns)

#d) The column higher seems interesting. Let's see which unique values it can have.
print(df["higher"].unique())

# e) Let's see if we can see some connection between age distribution and higher. Make 3 subplots of age histograms:
fig, axes = plt.subplots(1, 3, figsize=(13,4)) # one sinlge row with 3 columns/plots next to each other
# fig representerar hela figuren. axes är en lista med 
# Plot 1: same as b)
sns.histplot(df["age"], bins=20, ax=axes[0])
axes[0].set_title("overall age distribution")

#Plot 2: age distribution when higher is yes
sns.histplot(df[df["higher"]=="yes"]["age"], bins=20, ax=axes[1])
axes[1].set_title("age distribution higher=yes")

#Plot 3: age distribution when higher is no'
sns.histplot(df[df["higher"]=="no"]["age"], bins=20, ax=axes[2])
axes[2].set_title("age distribution higher=no")

plt.tight_layout() #undviker öpperlappning
plt.show()

#f) That was hard to find a connection. When reading dataset source we find alcohol consumption, 
# maybe there is some connection between age and alcohol consumption.
#Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
#Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
#Start with creating a new column called Alcohol, which is a sum of Dalc and Walc columns
df["Alcohol"] = df["Dalc"] + df["Walc"]

# g) Make a barchart for alcohol consumption vs age.
plt.figure(figsize=(8,5))
sns.barplot(x="age", y= "Alcohol", data= df, palette='viridis')
plt.title("Alcohol consumption vs age")
plt.xticks(rotation=45, ha="right")
plt.show()

#filling the freetime missing values
print(df["freetime"].unique())

