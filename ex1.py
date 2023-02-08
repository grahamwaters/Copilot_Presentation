def speak_for_the_trees():
    # the Austonian Lorax that speaks for the trees
    print("I speak for the trees!")
    """
    Create A Data visualization of Trees in Austin using Folium Tree data for Austin, Texas can be accessed via API at: https://data.austintexas.gov/resource/wrik-xasw.json ## Instructions - Create a Folium map of Austin, Texas that has tree data from the API above. - The map should show the roads, parks, and trees in Austin, Texas. - Trees should be represented by a green circle. - Parks should be represented by a blue circle. - Roads should be represented by a black line.
    """
    # Get tree data from API
    url = "https://data.austintexas.gov/resource/wrik-xasw.json"
    trees = requests.get(url).json()

    # Create Folium map centered on Austin, Texas
    m = folium.Map(location=[30.2672, -97.7431], zoom_start=12)

    # Add tree data to map
    for tree in trees:
        # the tree data is a dictionary
        # the latitude and longitude are stored as strings
        # we need to convert them to floats
        # {'geometry': {'type': 'Point',
        # 'coordinates': [-97.73398904092146, 30.25239671647407]},
        # 'species': 'Live Oak',
        # 'diameter': '20.0',
        # 'latitude': '30.2523967165',
        # 'longtitude': '-97.7339890409',
        # 'geocoded_column': {'type': 'Point',
        # 'coordinates': [-97.7339890409, 30.2523967165]}}
        tree_dict = tree  # a dictionary
        latitude = float(tree_dict["latitude"])
        longitude = float(tree_dict["longtitude"])
        folium.CircleMarker(
            location=[latitude, longitude],
            radius=3,
            color="green",
            fill=True,
            fill_color="green",
        ).add_to(m)
    # Save map to HTML file
    m.save("austin_tree_map.html")
    # show map
    return m


# run the function
speak_for_the_trees()
