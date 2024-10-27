def SquareSunflowerPlanter():
    numPlots = get_world_size() * get_world_size()
    largestPetalCount = []
    seed = Items.Sunflower_Seed
    sunflowers = []
    if not BuyEnoughSeeds(seed):
        return
    
    # Plant and water sunflowers
    for xPos in range(get_world_size()):
        for yPos in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            CheckWater()
            plant(Entities.Sunflower)
            sunflowers.append([measure(), xPos, yPos])
            move(North)
        move(East)
    
    # Harvest sunflowers in order of largest to smallest
    while len(sunflowers) > 0:
        largestPetalCount = 0
        largestSunflowers = []
        for i in range(len(sunflowers)):
            if sunflowers[i][0] == largestPetalCount:
                largestSunflowers.append(sunflowers[i])
            if sunflowers[i][0] > largestPetalCount:
                largestPetalCount = sunflowers[i][0]
                largestSunflowers = [sunflowers[i]]
        for sunflower in largestSunflowers:
            OldFlyTo(sunflower[1], sunflower[2])
            harvest()
            sunflowers.remove(sunflower)
    
    # All done, return to origin
    FlyTo(0, 0)