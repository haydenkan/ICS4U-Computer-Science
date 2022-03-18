FILE = open('testit.txt')

LINE = FILE.readline().strip('\n').split(',')
FILE.seek(0)
COLUMN_COUNT = len(LINE)
LIST = []

for i in range(COLUMN_COUNT):
    COLUMN = []
    for LINE in FILE:
        LINE = LINE.strip('\n').split(',')
        COLUMN.append(LINE[i])
    LIST.append(COLUMN)
    FILE.seek(0)

for i in range(1, len(LIST[0])):
    for j in range(COLUMN_COUNT):
        print(LIST[j][0] + ': ' + LIST[j][i])
    print('\n')

FILE.close()
