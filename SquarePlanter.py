def SquarePlanter(entity, seed, t = False):
    if seed:
        if not BuyEnoughSeeds(seed):
            return
    if can_harvest():
        harvest()
    else:
        CheckWater()
    if t:
        if get_ground_type() != Grounds.Soil:
            till()
    if entity != Entities.Grass:
        plant(entity)
    else:
        if get_ground_type() != Grounds.Turf:
            plant(Entities.Grass)
    move(North)       
    if get_pos_y() == 0:
        move(East)
    