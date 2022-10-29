from email.errors import StartBoundaryNotFoundDefect


def sunsetViews(buildings, direction):
    
    if len(buildings) == 0:
        return []
    
    if len(buildings) == 1:
        return [0]
    
    buildingsWithSunsetViews = []
    startOfDirection = 0
    if direction == "EAST":
        startOfDirection = len(buildings) - 1
        buildingsWithSunsetViews.append(startOfDirection)
        helperFacingEast(buildings, buildingsWithSunsetViews, startOfDirection - 1)
    else:
        buildingsWithSunsetViews.append(startOfDirection)
        helperFacingWest(buildings, buildingsWithSunsetViews, startOfDirection + 1)
    return buildingsWithSunsetViews

def helperFacingEast(buildings, buildingsWithSunsetViews, index):
    while index >= 0:
        if buildings[index] > buildings[buildingsWithSunsetViews[0]]:
            buildingsWithSunsetViews.insert(0,index)
        index -= 1

def helperFacingWest(buildings, buildingsWithSunsetViews, index):
    while index < len(buildings):
        if buildings[index] > buildings[buildingsWithSunsetViews[-1]]:
            buildingsWithSunsetViews.append(index)
        index += 1
    

buildings = [3,5,4,4,3,1,3,2]
direction = "EAST"
print(sunsetViews(buildings, direction))

buildings = [3,5,4,4,3,1,3,2]
direction = "WEST"
print(sunsetViews(buildings, direction))