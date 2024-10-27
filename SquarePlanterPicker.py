def SquarePlanterPicker(harvestEntity):
    if harvestEntity == Items.Hay:
        def fn():
            return SquarePlanter(Entities.Grass, "", False)
    if harvestEntity == Items.Wood:
        def fn():
            return SquareTreePlanter()
    if harvestEntity == Items.Carrot:
        def fn():
            return SquarePlanter(Entities.Carrots, Items.Carrot_Seed, True)
    if harvestEntity == Items.Pumpkin:
        def fn():
            return SquarePumpkinPlanter()
    if harvestEntity == Items.Power:
        def fn():
            return SquareSunflowerPlanter()
    if harvestEntity == Entities.Treasure:
        def fn():
            return MazeRunner()
    return fn