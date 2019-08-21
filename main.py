import argparse
import json
import datetime

from pandas.io.json import json_normalize
from folium.plugins import HeatMap

import folium

def parse_timestamp(ts):
    '''
    Specific int parsing for the timestamp provided by Google by truncating the last 3 digits.
    '''
    try:
        ts = int(ts)//1000
    except Exception:
        ts = 0
    return ts 


parser = argparse.ArgumentParser()

parser.add_argument('--locationsfile', 
        type=str,
        help='Path to file downloaded from Google Timeline. Should be a json with the locations history',
        metavar='Path to locations history file',
        required=True)

args = parser.parse_args()

with open(args.locationsfile, 'r') as f:
    try:
        locations_data = json.load(f)
        print("Finished reading the locations file")
    except Error as e:
        print(e)
        exit()

data = json_normalize(locations_data, 'locations')

data = data[['timestampMs','latitudeE7','longitudeE7']]
data['timestampMs'] = data['timestampMs'].apply(parse_timestamp)
data['latitudeE7'] = data['latitudeE7'].apply(lambda x: x/1e7)
data['longitudeE7'] = data['longitudeE7'].apply(lambda x: x/1e7)
data['date'] = data.timestampMs.apply(lambda ms: datetime.datetime.fromtimestamp(ms))


data['unified'] = list(zip(data['latitudeE7'], data['longitudeE7']))
data['date'] = data.timestampMs.apply(lambda ms: datetime.datetime.fromtimestamp(ms))
data = data.dropna(axis=0)

assert data.isnull().any().all() == False, "Data must not have nulls"

print("Processed the data")

m = folium.Map([46.81, 8.22],tiles='stamentoner', zoom_start=6)
print("Created the map")

# make sure unified column doesn't have nans
_ = HeatMap(data['unified'], min_opacity=1, radius=10).add_to(m)
print("Created the heat layer")

_ = m.save('goloheat.html')
print("Saved the heatmap")
