elfCalorieTotal = []
holdingTotal = 0

with open('day01input.txt', 'r') as f:
    for i in f:
        if i == '\n':
            elfCalorieTotal.append(holdingTotal)
            holdingTotal = 0
        else:
            holdingTotal += int(i)

elfCalorieTotal.sort()
# PART ONE
print(elfCalorieTotal[-1])
# PART TWO
print(elfCalorieTotal[-1] + elfCalorieTotal[-2] + elfCalorieTotal[-3])