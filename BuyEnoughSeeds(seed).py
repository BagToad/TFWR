def BuyEnoughSeeds(seed):
    numPlots = get_world_size() * get_world_size()
    if num_items(seed) <= numPlots:
        if not CheckCost(seed, numPlots):
            return False
        return trade(seed, numPlots)
    return True