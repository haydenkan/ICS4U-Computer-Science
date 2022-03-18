
def BUBBLE_SORT(NUM_LIST):
    LIMIT = len(NUM_LIST)
    for i in range(LIMIT):
        SORTED = True
        for j in range(LIMIT - i - 1):
            if NUM_LIST[j] > NUM_LIST[j + 1]:
                NUM_LIST[j], NUM_LIST[j + 1] = NUM_LIST[j + 1], NUM_LIST[j]
                SORTED = False
        if SORTED:
            break
    return NUM_LIST

NUM_LIST = [9, 3, 15, 2, 21, 6, 7]
print(BUBBLE_SORT(NUM_LIST))
