import time
import pandas
import numpy

def menu():
	loopCtrl = 1
	print("========== RISC & CISC QUIZ ==========")
	print("\t1. Start Quiz\n\t2. Display High Score\n\t3. Quit")
	while loopCtrl == 1:
		loopCtrl = 2
		userOpt = input("Enter a number > ")
		try:
			int(userOpt)
		except:
			print("That isn't a number, please try again.")
			loopCtrl = 1
		userOpt = int(userOpt)
		if userOpt > 3 or userOpt < 1:
			print("That number is not an option, please try again.")
			loopCtrl = 1
	return userOpt

def start_quiz():
	# generates a list with the contents of a csv file and then converts it into a dictionary, and then an array
	bigQuestionListDataFrame = pandas.read_csv("qanda.csv")
	bigQuestionListDictionary = bigQuestionListDataFrame.to_dict()
	questionList = list(bigQuestionListDictionary.values())
	questions = questionList[0]
	timer = 180

	print("Welcome to the RISC or CISC Quiz!\nYou will be given various statements that will apply to either CISC or RISC processors, and you need to answer with which one it is!\nYou have 3 minutes to do as many as you can.")
	while timer > 0:



loopCtrl = 1
while loopCtrl == 1:
	loopCtrl = 2
	menuChoice = menu()
	if menuChoice == 1:
		start_quiz()
		loopCtrl = 1
	elif menuChoice == 2:
		display_high_score()
		loopCtrl = 1
	elif menuChoice == 3:
		finish()
		loopCtrl = 1
