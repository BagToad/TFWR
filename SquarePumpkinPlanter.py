def SquarePumpkinPlanter():
    # We want to keep planting until the entire farm is full
    fullyPlanted = False
    plantedOrGrowing = False
    while not fullyPlanted:
        if not BuyEnoughSeeds(Items.Pumpkin_Seed):
            return
        for xPos in range(get_world_size()):
            for yPos in range(get_world_size()):
                if get_ground_type() != Grounds.Soil:
                    till()
                if get_entity_type() != Entities.Pumpkin:
                    CheckWater()
                    plant(Entities.Pumpkin)
                    plantedOrGrowing = True
                if not can_harvest():
                    plantedOrGrowing = True
                move(North)
            move(East)
        if not plantedOrGrowing:
            fullyPlanted = True
        plantedOrGrowing = False

    harvest()

# def buyEnoughPumpkinSeeds():
#     seed = Items.Pumpkin_Seed
#     numPlots = get_world_size() * get_world_size()
#     if num_items(seed) <= numPlots:
#         if not CheckCost(seed, numPlots):
#             return
#         trade(seed, numPlots)