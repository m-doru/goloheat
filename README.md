# Google location history heatmap

Allows you to get map-based insights from Google Timeline data.

Implemented in Python using Pandas and Folium

Inspired by this Reddit post:
https://www.reddit.com/r/dataisbeautiful/comments/718wt7/heatmap_of_my_location_during_last_2_years_living/

## How to use:
1. Go to https://takeout.google.com/ and download only the **Location History** in JSON format. Extract the archive.
2. `cd goloheat`
3. `python3 -m venv ./venv`
4. `source ./venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python3 main.py --locationsfile path-to-json-file-from-extracted-archive`
7. Open the created `goloheat.html` from current directory using an internet browser (tested on Chrome and Firefox)
