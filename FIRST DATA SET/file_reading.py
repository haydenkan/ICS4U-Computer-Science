import random
try:
    FILE = open("info.txt")
except:
    LOCATION = input("Please specify the full path of the file ")

try:
    FILE = open(LOCATION)
    FILE_FOUND = True
except:
    FILE_FOUND = False
    print("Could not find file")

if FILE_FOUND:
    GAME_LIST = []
    TEXT = FILE.readlines()
    print ("This is what text looks like", TEXT)

    for LINE in TEXT:
        print(LINE)
        LINE = LINE.strip()
        print("This is line now ", LINE)
        LINE = LINE.split(",")
        print ("The string has been broken at the commas", LINE)
        GAME_LIST.append(LINE)

    print(GAME_LIST)