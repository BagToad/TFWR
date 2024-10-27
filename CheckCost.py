# Return true if we can afford it, false if we can't
def CheckCost(item, num):
    cost = get_cost(item)
    for i in cost:
        if num_items(i) < cost[i] * num:
            return False
    return True