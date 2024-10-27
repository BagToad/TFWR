def MazeRunner():
    # Start the maze
    plant(Entities.Bush)
    while get_entity_type() == Entities.Bush:
        # Check if we have enough fertilizer
        if num_items(Items.Fertilizer) < 1:
            trade(Items.Fertilizer, 10)
        use_item(Items.Fertilizer)
    
    # RUN THE MAZE

    directions = [North, East, South, West]
    d = 0
    
    foundTreasure = False
    while not foundTreasure:
        # Check if we are at the treasure before we move anywhere
        if get_entity_type() == Entities.Treasure:
            foundTreasure = True
            harvest()
            break
        # Main pathfinding logic

        # Check if the wall we are following has an opening
        moved = move(directions[rotate(d, "left")])
        # If there was an opening in the wall we are following,
        # we rotate to the left and follow this new wall
        if moved:
            d = rotate(d, "left")
        # If there wasn't an opening in the wall we are following,
        # we carry on following the wall until we hit a wall
        if not moved:
            moved = move(directions[d])
        # If we hit a wall, we need to rotate to the right and follow this 
        # wall we just hit
        if not moved:
            d = rotate(d, "right")
        

def rotate(currentDirection, rotateDirection):
    if rotateDirection == "right":
        return (currentDirection + 1) % 4
    if rotateDirection == "left":
        return (currentDirection - 1) % 4