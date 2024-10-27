def CheckWater():
    while get_water() <= 0.75:
        if num_items(Items.Water_Tank) <= 0:
            break
        use_item(Items.Water_Tank)