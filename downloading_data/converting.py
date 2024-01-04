from pathlib import Path
import json

import plotly.express as px

#Read data as a string and converet to python
path = Path('/Users/masongalusha/Downloads/1.0_month.geojson.json')
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
    )
fig.show()
