# Example One - A Data visualization of Trees in Austin using Folium
Tree data for Austin, Texas can be accessed via API at: https://data.austintexas.gov/resource/wrik-xasw.json
## Instructions
- Create a Folium map of Austin, Texas that has tree data from the API above.
- The map should show the roads, parks, and trees in Austin, Texas.
- Trees should be represented by a green circle.
- Parks should be represented by a blue circle.
- Roads should be represented by a black line.

```python
import folium
import requests

# Get tree data from API
url = "https://data.austintexas.gov/resource/wrik-xasw.json"
trees = requests.get(url).json()

# Create Folium map centered on Austin, Texas
m = folium.Map(location=[30.2672, -97.7431], zoom_start=12)

# Add tree data to map
for tree in trees:
    folium.CircleMarker(location=[tree['latitude'], tree['longitude']],
                        radius=3, color='green', fill=True, fill_color='green').add_to(m)

# Add parks data to map
# (Assuming you have the parks data in a similar format as the tree data)
# for park in parks:
#    folium.CircleMarker(location=[park['latitude'], park['longitude']],
#                        radius=10, color='blue', fill=True, fill_color='blue').add_to(m)

# Add roads data to map
# (Assuming you have the roads data in a format that can be added to the map as a line)
# folium.PolyLine(road_coordinates, color='black', weight=2.5, opacity=1).add_to(m)

# Save map to HTML file
m.save('austin_tree_map.html')
```
