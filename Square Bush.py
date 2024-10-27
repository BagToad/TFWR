while True:
    if can_harvest():
        harvest()  
    plant(Entities.Bush)
    move(North)
    if get_pos_y() == 0:
        move(East)