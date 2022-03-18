

def INSERTION_SORT(NUM_LIST):
    LIMIT = len(NUM_LIST)
    for i in range(1, LIMIT):
        for j in range(i, 0, -1):
            if NUM_LIST[j] < NUM_LIST[j - 1]:
                NUM_LIST[j], NUM_LIST[j - 1] = NUM_LIST[j - 1], NUM_LIST[j]
    return NUM_LIST

NUM_LIST = [9, 3, 15, 2, 21, 6, 7]
print(INSERTION_SORT(NUM_LIST))


