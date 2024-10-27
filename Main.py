while True:
    MinMaxRunner(Items.Hay, 50000, 50000, SquarePlanterPicker(Items.Hay))
    MinMaxRunner(Items.Wood, 100000, 100000, SquarePlanterPicker(Items.Wood), True, True)
    MinMaxRunner(Items.Carrot, 100000, 100000, SquarePlanterPicker(Items.Carrot))
    MinMaxRunner(Items.Power, 50000, 50000, SquarePlanterPicker(Items.Power), True)
    
    MinMaxRunner(Items.Gold, 100000, 100000, SquarePlanterPicker(Entities.Treasure), True, True)
    
    MinMaxRunner(Items.Pumpkin, 10000, 10000, SquarePlanterPicker(Items.Pumpkin), False, True)