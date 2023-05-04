inputPence = int(input("Enter the number of pence to be converted: "))

fifties = 0
twenties = 0
tens = 0
fives = 0
twos = 0
ones = 0

if inputPence >= 50:
	fifties = inputPence // 50
	inputPence = inputPence % 50

if inputPence >= 20:
	twenties = inputPence // 20
	penceLeft = inputPence % 20

if inputPence >= 10:
	tens = inputPence // 10
	inputPence = inputPence % 10

if inputPence >= 5:
	fives = inputPence // 5
	inputPence = inputPence % 5

if inputPence >= 2:
	twos = inputPence // 2
	inputPence = inputPence % 2

if inputPence >= 1:
	ones = inputPence // 1
	inputPence = inputPence % 1

print(f"{fifties} x 50p, {twenties} x 20p, {tens} x 10p, {fives} x 5p, {twos}x 2p, {ones} x 1p")
