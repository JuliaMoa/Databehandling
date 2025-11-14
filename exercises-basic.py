
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

 

data_dict = {
    "kommun" : ["Malmö", "Stockholm", "Uppsala", "Göteborg"],
    "population" : [347949, 975551, 233839, 583056]
}
df = pd.DataFrame(data_dict)
Göteborg_row = df[df["kommun"] == "Göteborg"] #filtering for only the row which has Göteborg in the column 
df.sort_values(by="population", ascending=False, inplace=True)
three_biggest = df.nlargest(3, 'population')

df["Population(%)"] = (df["population"] / 10379295) * 100 
df["Population(%)"] = df["Population(%)"].round

# 2
data = r"C:\Users\jubel\REPON\Databehandling\komtopp50_2020.xlsx"

#b
df = pd.read_excel(data, sheet_name="Totalt", skiprows=6)
df.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]

#c - sort from largest to smallest
df.sort_values("Folkmängd 2020", ascending=False , inplace=True)
df.reset_index(drop=True, inplace=True) #updates the index to the sorted list, drop takes away the old index
print(df)

#d - print out 5 smallest
print(df.tail())
print(df.iloc[-5:])
print(df.apply(pd.Series))

#e
population_2019 = df["Folkmängd 2019"].sum()
print(f"The population in Sweden 2019 was {population_2019}")
print(f"The population in Sweden 2020 was {df["Folkmängd 2020"].sum()}")

#f Plot a bar chart for the five largest cities and the five smallest cities.

biggest_five = df.head(5)
sns.set_style('darkgrid')
sns.barplot(x="Kommun", y="Folkmängd 2020", data=biggest_five, palette='hot')
plt.title("Figgest five kommuner")
plt.show()

smallest_five = df.tail(5)
sns.set_style('darkgrid')
sns.barplot(x="Kommun", y="Folkmängd 2020", data=smallest_five, palette='hot')
plt.title("Smallest five kommuner")
plt.show()

