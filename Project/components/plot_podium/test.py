from plot_podium import PlotPodium
import pandas as pd

df= pd.read_csv("C:/Users/carbe/Documents/Data Science/DS4A/DS4A/Project/src/data/final_schools.csv")
df= df.head(10)
x= PlotPodium(df)
x.plot_podium()

