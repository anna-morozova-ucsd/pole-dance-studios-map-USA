import pandas as pd  # version 2.0.0
import plotly.express as px # version 5.14.1

# read in the CSV file
df = pd.read_csv('US_pole_studios.csv')

# set your Mapbox access token
# create account at https://www.mapbox.com/ to generate a token
mapbox_token = 'your_mapbox_access_token'

# customize the text on hover 
df['hover_text'] = df['name'] + '<br><span style="font-weight: normal;">' + df['address'] + '</span>'


# create the figure using plotly express
fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_name="hover_text", hover_data={ "longitude": False, "latitude": False}, #hover_name='name',
                        mapbox_style='dark', zoom=3, height=700)

# update the layout with your Mapbox access token
fig.update_layout(mapbox_accesstoken=mapbox_token)
fig.update_layout(title_text="Pole Dance Studios in the USA")

# show the plot
fig.show()
