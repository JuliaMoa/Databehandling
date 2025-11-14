import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

data = r"C:\Users\jubel\REPON\Databehandling\komtopp50_2020.xlsx"

df_totalt = pd.read_excel(data, sheet_name="Totalt", skiprows=6)
df_totalt.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]

def load_and_clean_sheet (data, sheet, kön):
    df = pd.read_excel(data, sheet_name=sheet, skiprows=6)
    df.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]
    df["Kön"] = kön 
    return df 

#använder funktionen för att läs in de andra, med en extra kolumn
df_kvinnor = load_and_clean_sheet(data, "Kvinnor", "Kvinna")
df_män = load_and_clean_sheet(data, "Män", "Man")

#b) Merge the male and female DataFrames vertically and set index to "Kommun". Note that there now should be 580 rows now.

df_kvinnorochmän = pd.concat([df_män, df_kvinnor], ignore_index=True) 
df_kvinnorochmän = df_kvinnorochmän.drop(columns=["Rang 2020", "Rang 2019"])
df_kvinnorochmän.set_index("Kommun", inplace=True)
print(df_kvinnorochmän)

# c) Extract and change column name from the total DataFrame so that the head look like this: 
df_totalt.drop(columns=["Rang 2020", "Rang 2019"], inplace=True)
df_totalt.rename(columns={"Folkmängd 2020":"Total Pop 2020", "Folkmängd 2019":"Total Pop 2019", "Förändring":"Total förändring"}, inplace=True)
print(df_totalt)

# d) Merge this data with the data in b) so that the head look like this: (*)
df_total_and_alreadymerged = pd.merge(df_kvinnorochmän, df_totalt, on="Kommun")
df_total_and_alreadymerged.sort_values("Total Pop 2020", ascending=False, inplace=True, ignore_index=True)
print(df_total_and_alreadymerged.head())

# e) Create BARPLOTS showing the gender populations of Swedens 10 largest and 10 smallest cities

biggest_ten = df_total_and_alreadymerged.head(20)
sns.set_style('darkgrid')
sns.barplot(y="Kommun", x="Folkmängd 2020", data=biggest_ten, hue="Kön", palette='hot', orient="h")
plt.title("Gender population of biggest ten kommuner")

smallest_ten = df_total_and_alreadymerged.tail(20)
sns.set_style('darkgrid')
sns.barplot(y="Kommun", x="Folkmängd 2020", data=smallest_ten, hue="Kön", palette='hot', orient="h")
plt.title("Gender population of the smallest ten kommuner")

# f) Create a PIE CHART showing the total male and female population in Sweden 2020.
sns.set_style('whitegrid')
plt.figure(figsize=(6,6))

kvinnor = df_total_and_alreadymerged[df_total_and_alreadymerged["Kön"]=="Kvinna"] 
total_kvinnor = kvinnor["Total Pop 2020"].sum()

män = df_total_and_alreadymerged[df_total_and_alreadymerged["Kön"]=="Män"] 
total_män = män["Total Pop 2020"].sum()

data = [män, total_kvinnor] 
labels = ['men', 'women']
colors = sns.color_palette('pastel')[0:2]

plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
plt.show()

#g) Create a barplot showing the cities with the five largest percentual gender difference in 2020. (**)

#h) Create a barplot showing the top 5 cities with largest populational growth from 2019 to 2020 (**)




