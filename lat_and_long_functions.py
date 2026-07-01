def c1Nc2(c1, c2, mainland=True):
    
    """
    This function will return the Boolean answer
    to the question of whether Country c1 is
    entirely north of Country c2. Adjust the
    "mainland" parameter to False to include
    island holdings etc.
    """
    
    with open("latitudes.json", "r") as json_file:
        lats = json.load(json_file)
    
    if mainland:
        pt1 = lats[c1]['ms']
        pt2 = lats[c2]['mn']

    else:
        pt1 = lats[c1]['s']
        pt2 = lats[c2]['n']
        
    return pt1 > pt2


def c1Cc2(c1, c2, north_or_east='north', mainland=True):
    """
    This function will return the Boolean answer
    to the question of whether Country c1 is
    either entirely north (north_or_east = 'north')
    or entirely east (north_or_east = 'east') of
    Country c2. Adjust the "mainland" parameter to
    False to include island holdings etc.
    """
    
    with open("extreme_points.json", "r") as json_file:
        points = json.load(json_file)
    
    if north_or_east == 'north':
    
        if mainland:
            pt1 = points[c1]['ms']
            pt2 = points[c2]['mn']

        else:
            pt1 = points[c1]['s']
            pt2 = points[c2]['n']
    
    else:
        
        if mainland:
            pt1 = points[c1]['mw']
            pt2 = points[c2]['me']
        
        else:
            pt1 = points[c1]['w']
            pt2 = points[c2]['e']
        
    return pt1 > pt2