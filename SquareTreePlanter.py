def SquareTreePlanter():
    isOddColumn = get_pos_x() % 2 == 1
    # We just started this column and need to
    # skip the first row.
    if get_pos_y() == 0 and isOddColumn:
        move(North)
    if can_harvest():
        harvest()
        if get_ground_type() == Grounds.Turf:
            till()
        plant(Entities.Tree)
    else:
        while get_water() <= 0.75:
            if num_items(Items.Water_Tank) <= 0:
                break
            use_item(Items.Water_Tank)
           
    move(North)
    # If we haven't moved off the edge of
    # the map, then we need to move once more
    # to stagger the trees
    if get_pos_y() != 0:
        move(North)
    # If we have move off the edge of the map
    # at this point, that means we need to move
    # to the next column
    if get_pos_y() == 0:
        move(East)