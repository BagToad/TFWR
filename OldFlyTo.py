def OldFlyTo(x, y):
    # Check if out of bounds.
    # If out of bounds, just exit.
    if x > get_world_size() -1  or y > get_world_size() - 1:
        return

    while get_pos_x() != x:
        if get_pos_x() < x:
            move(East)
            continue
        move(West)
    while get_pos_y() != y:
        if get_pos_y() < y:
            move(North)
            continue
        move(South)