import folium
import json
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import date, datetime, time, timezone
from folium.plugins import HeatMap


df = pd.read_csv("covid-vaccination-doses-per-capita.csv")
df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)

covid_c = df.groupby(['Entity'])

total_df = covid_c.sum()

center = [43.47487307978007, 76.77008277826954]

m = folium.Map(location=center, zoom_start=2,
               min_zoom=1, max_zoom=84,
               max_lat=84, min_lon=175, max_lon=187,
               )

geo_path = "countries.geo.json"

json_data = json.load(open(geo_path))
# print(json_data['features'][0]['properties'])
folium.Choropleth(geo_data=json_data,
                  data=total_df,
                  columns=(total_df.index, 'total_vaccinations_per_hundred'),
                  key_on='properties.name',
                  fill_color='RdYlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  ).add_to(m)

folium.LayerControl().add_to(m)

m.save('map.html')
