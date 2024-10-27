def FlyTo(x, y):
    # Check if out of bounds.
    # If out of bounds, just exit.
    if x > get_world_size() -1 or y > get_world_size() - 1:
        return

    while get_pos_x() != x:
        if get_pos_x() < x: # Left of the Dest
            # Compare the distance to the destination vs
            # the distance to the west wall
            distanceToDestRight = x - get_pos_x()
                                                # (10 - 1) - 8 = 1
            distanceToDestLeft = get_pos_x() + ((get_world_size() - 1) - x)
            if distanceToDestRight < distanceToDestLeft:
                move(East)
                continue
            move(West)
        if get_pos_x() > x: # Right of the Dest
                    # Compare the distance to the destination vs
                    # the distance to the east wall
                    distanceToDestLeft = get_pos_x() - x
                    distanceToDestRight = (get_world_size() - 1) - distanceToDestLeft
                    if distanceToDestLeft < distanceToDestRight:
                        move(West)
                        continue
                    move(East)
    while get_pos_y() != y:
        if get_pos_y() < y:
            move(North)
            continue
        move(South)

    set_execution_speed(0)
