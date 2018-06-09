# Anne Harris
# CS325-400
# Homework 4
# 4/29/2018

# Introduce Program
print("Activity Selection: Last-to-Start Implementation by Anne Harris", '\n', "CS325-400", '\n')

# implement Last-to-Start Selection
# based on pseudo code of Greedy-Activity Selector algorithm in Cormen, Leiserson, Rivest, Stein,
#   Introduction to Algorithms, 3rd edition, page 421
def lastToStart(actSet):
    # create empty list of selected activities to return
    retAct = []
    # sort the list of lists based on start time
    # technique from: https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
    actSet.sort(key=lambda x: x[1])
    # reverse the list of lists
    actSet.reverse()

    # always take the first element
    retAct.append(actSet[0])
    prev = 0

    # search rest of activity list
    for act in range(1, (len(actSet)-1)):
        # if the activity's finish time is less than or equal to the prev activity's start time select it
        if actSet[act][2] <= (actSet[prev][1]):
            # add activity to list
            retAct.append(actSet[act])
            # assign previous activity to the current activity
            prev = act

    # put activities in reverse order to return
    retAct.reverse()
    return retAct


# open file
# read in as:
# [number of activities]
# [[activity id] [start time] [finish time]]
nums = []   # list to hold activity information
sets = []   # list to hold set lengths
with open("act.txt", "r") as f:
    for x in f:
        var = x.split(" ")
        # if there is only one number it's the beginning of a new set
        if len(var) == 1:
            sets.append(int(var[0]))
        else:
            for y in range(len(var)):
                var[y] = int(var[y])    # string into integer
            nums.append(var)

f.close()

# organize sets
# create variable to keep track of previous set
prevSet = 0
# go through each set
for s in range(len(sets)):
    print("Set ", s+1)
    # set length is the number in the sets list
    setLen = sets[s]
    # create subset from nums of activities within sets
    tempSet = nums[prevSet:(prevSet+setLen)]
    # call the activity selector algorithm
    activitiesSel = lastToStart(tempSet)
    # print results
    print("Number of Activities Selected: ", len(activitiesSel))
    # create temp list to hold the activity number
    finalAct = []
    for i in range(len(activitiesSel)):
        finalAct.append(activitiesSel[i][0])
    print("Activities: ", finalAct)
    # increase previous set to the end of the last set looked at
    prevSet += setLen