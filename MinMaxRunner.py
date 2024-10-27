def MinMaxRunner(harvestEntity, requestedMin, requestedMax, fn, clr = False, zero = False):
    realMin = requestedMin
    realMax = requestedMax

    # Weird behavior, but hear me out.
    # -1 is a signal to execute this runner forever, but we want to
    # re-evaluate other resources every now and again, so we'll
    # just say it's 1000 above whatever we curreently have.
    if requestedMax == -1:
        realMax += num_items(harvestEntity) + 1000
    if num_items(harvestEntity) <= realMin or requestedMax == -1:
        if clr:
            clear()
        if zero:
            FlyTo(0, 0)
        while num_items(harvestEntity) <= realMax:
            fn()