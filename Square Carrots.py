while True:
    if num_items(Items.Carrot_Seed) <= 1:
        for i in range(10):
            trade(Items.Carrot_Seed)
        
    if can_harvest():
        harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Carrots)
        move(North)       
    if get_pos_y() == 0:
        move(East)