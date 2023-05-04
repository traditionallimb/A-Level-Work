with open('day02input.txt', 'r') as f:
    raw = f.readlines()
    stratGuide = []
    totalScore1 = 0
    mePick = ['X', 'Y', 'Z']  # r, p, s

    for i in raw:
        stratGuide.append(i.rstrip().replace(" ", ""))

for i in stratGuide:
    if i in ['AY', 'BZ', 'CX']:
        totalScore1 += (6 + (mePick.index(i[1]) + 1))
    elif i in ['AX', 'BY', 'CZ']:
        totalScore1 += (3 + (mePick.index(i[1]) + 1))
    elif i in ['AZ', 'BX', 'CY']:
        totalScore1 += (mePick.index(i[1]) + 1)

# PART ONE
print(totalScore1)


# PART TWO

rock = {'X': 3, 'Y': 1, 'Z': 2}
paper = {'X': 1, 'Y': 2, 'Z': 3}
scissors = {'X': 2, 'Y': 3, 'Z': 1}

totalScore2 = 0

for i in stratGuide:
    if i[0] == 'A':
        totalScore2 += rock[i[1]]
    elif i[0] == 'B':
        print(paper[i[1]])
    elif i[0] == 'C':
        print(scissors[i[1]])
