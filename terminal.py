scores = []
clear()
for ii in range(10):
    SquareSunflowerPlanter()
    if ii == 0:
        scores.append(get_op_count())
    else:
        scores.append(get_op_count() - prevCount)
    displayAverageScore(scores)
    prevCount = get_op_count()
# 1000, 2000, 3000
# 1000, (2000 - 1000 = 1000), (3000 - 2000 = 1000)

    
def displayAverageScore(s):
    sum = 0
    for score in s:
        sum += score
    print("Current iteration: ", len(s), "Average: ", sum / len(s), "List: ", s)
    #print("Average: ", sum / len(s))


#     #MazeRunner()
#     SquarePumpkinPlanter()
#MoveUntilWall(East)
#set_execution_speed(4)
#FlyTo(1,0)
#FlyTo(8,0)