
'''
Genre-Region Heatmap Build a heatmap showing the preference intensity for each genre across the four regions.
Normalize by region (so each region sums to 100%) to see relative preferences rather than absolute sales.
'''

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loading csv file & creating dataframe
data = pd.read_csv("vgsales.csv")
#To ensure there is no error in reading the csv file, ensure the csv file is in the
#same folder as the .py
print(data.head())
#Viewing first 5 rows of the data to check whether the data is loaded correclty
#If you see >>> in the terminal, means you are in Python shell. Exit/quit the terminal
#And start the terminal again. I tried to run in Python shell and faced several errors despite the codes are correct.

df = pd.DataFrame(data)
#Dataframe is like a spreadsheet

print(df.head())
#similary, quick check on whether the data is loaded correclty
df.info()
#Checking the features (ie column names), number of empty/NaN cells, data type.


genre_regional = df.groupby('Genre')[['NA_Sales','EU_Sales',
                                      'JP_Sales']].sum()
print(genre_regional.head())

#Creating genre_region "table" showing total sales of each region, group by genre

genre_global = df.groupby('Genre')['Global_Sales'].sum()
print(genre_global.head())
#Creating genre_global "table" for purpose of normalizing genre_regional values

genre_global = genre_global.reindex(genre_regional.index)
#Probably unnecessary but had this thought whether the two dfs have matching genre.
#So did this reindexing to ensure both tables have matching genres.

genre_regional_normalized = genre_regional.div(genre_global, axis = 0)
print(genre_regional_normalized)

#Crediting Chatgpt. Have to use .div function instead of the regular / so we can dictate how divide action to be done.

#Generating heatmap
heatmap = sns.heatmap(genre_regional_normalized, annot = True, cmap = "Blues", fmt =".1f")
#Creating heatmap using seaborn.
#annot - Allowing annotations
#cmap - "Colormap". I just use Chatgpt to find out the available options.
#fmt - # of decimal places, with .1f meanig 1 decimal place
column_names = genre_regional_normalized.columns
#Extracting the region names to be used in title later
plt.title(f"Heatmap across {', '.join(column_names)}")
#creating title for the heatmap
plt.xlabel("Regions")
#Creating X-Axis name. For ease, I would do plt.show to determine the X-axis.
plt.ylabel("Genres")
#Same for the y-Axis
plt.tight_layout()
#Using .tight_layout to tided up the chart, minimizing overlaps of annotations
plt.show()
#This is to show the ploted heatmap