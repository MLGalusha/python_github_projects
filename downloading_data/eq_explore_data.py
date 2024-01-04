from pathlib import Path
import json

#Read data as a string and converet to python
path = Path('/Users/masongalusha/Downloads/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

path1 = Path('/Users/masongalusha/Desktop/python_work/GitHub/python_github_projects/downloading_data/again_new')
readable_contents = json.dumps(all_eq_data, indent=4)
path1.write_text(readable_contents)

