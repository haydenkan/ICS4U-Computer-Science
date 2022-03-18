
def STRIP_FORMATTING(STRING):
    STRING = STRING.upper().replace(' ', '').strip('\n').split(',')
    return STRING

FILE = open('fruitlist.txt')
ELEMENTS = []
FRUITS = {}
LETTER_OCCURENCES = {}

for LINE in FILE:
    ELEMENTS.extend(STRIP_FORMATTING(LINE))

for ELEMENT in ELEMENTS:
    FRUITS[ELEMENT] = {}
    for LETTER in ELEMENT:
        if LETTER in FRUITS[ELEMENT]:
            FRUITS[ELEMENT][LETTER] += 1
        else:
            FRUITS[ELEMENT][LETTER] = 1


for KEY in FRUITS:
    for SUB_KEY in FRUITS[KEY]:
        if SUB_KEY in LETTER_OCCURENCES:
            LETTER_OCCURENCES[SUB_KEY] += FRUITS[KEY][SUB_KEY]
        else:
            LETTER_OCCURENCES[SUB_KEY] = FRUITS[KEY][SUB_KEY]

for LETTER in LETTER_OCCURENCES:
    print('There are', LETTER_OCCURENCES[LETTER], LETTER + 's')
