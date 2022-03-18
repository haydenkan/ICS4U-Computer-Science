

def SELECTION_SORT(NUM_LIST):
    LIMIT = len(NUM_LIST)
    for i in range(LIMIT):
        ITEM_TO_MOVE = i
        for j in range(i + 1, LIMIT):
            if NUM_LIST[j] < NUM_LIST[ITEM_TO_MOVE]:
                ITEM_TO_MOVE = j

        NUM_LIST[ITEM_TO_MOVE], NUM_LIST[i] = NUM_LIST[i], NUM_LIST[ITEM_TO_MOVE]
    return NUM_LIST

NUM_LIST = [9, 3, 15, 2, 21, 6, 7]
print(SELECTION_SORT(NUM_LIST))


