"""Python file for whole data set process, to generate chart in html file. Be mindful that it may take a long time and occupy much space depends on the number of reviews for the requested Google play app. Eg, Whatsapp return around 12 millions reviews and 3GB data, the generated chart html for histogram chart for review score and date is over 320MB."""
#Import required libraries
import pandas as pd
import glob, os 

#enter path
path = r'./'   
#read all or selected csv to dataframe
all_csv = glob.glob(os.path.join(path, "reviews_*.csv"))   
df = (pd.read_csv(f) for f in all_csv)
df_all   = pd.concat(df, ignore_index=True)

#Check and inspect data frame.
print(df_all.shape)
print(df_all.head)
print(df_all.dtypes)

# import plotly package for interactive charts
import plotly
import plotly.express as px

# Histogram chart for Score, thumbsupcount data counts
fig = px.histogram(df_all, x='at', nbins=15, color="score",marginal='box',barmode='group',category_orders={"score":[5,4,3,2,1]})
plotly.offline.plot(fig, filename='3.2.histogram_all_01.html')
