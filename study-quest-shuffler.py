'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#Author: Shanice McKay
#Date: December 19, 2023
#Project: Study Quest Shuffler
#Description: Python program that allows users to enter number of questions, questions and answers that it will later shuffle and display to user to test their knowledge.

#random odule imported so that the questions can be shuffled
import random

#initializing variables
MAX_QUESTIONS = 0
question_bank = []
total_questions = 0 
score = 0

#output statements
print("*** WELCOME TO STUDY QUEST SHUFFLER ***")
print("\n-----\nHow it works: ")
print("Study Quest Shuffler is a great tool for students at any level.\nYou have complete control of the questions, answers and even the number of questions!\nThe program will display the questions at random to test your knowledge.\nYou'll get your score at the end of the quest. Happy studying!\n-----")

#prompts to start or exit the program
start = str(input("\nDo you want to start your study quest? "))

#if statements to display appropriate message based on input
if(start.lower() == "yes"):
    print("\n***\nStudy Shuffler loading...\n***")
elif(start.lower() == "no"):
    print("\nSee you next time!")
    exit()
else:
    print("\nInvalid entry.")
    exit()

#to prompt user to enter number of questions
question_number = int(input("\nHow many questions do you want to enter? "))

#the value of question_number is stored in MAX_QUESTIONS
MAX_QUESTIONS = question_number

#to prompt user to enter what subject they are preparing for
subject = str(input("\nWhat subject are you preparing for? "))

#pretest while loop to prompt user to enter question and answers
while total_questions < MAX_QUESTIONS:
    question = str(input("\nEnter question: "))
    answer = str(input("Enter answer: "))
    
    #adds question and answer to list called question bank
    question_bank.append([question, answer])
    
    #increases count by 1
    total_questions += 1

#Shuffles order of question in question_bank randomly
random.shuffle(question_bank)

#output statement
print(f"\n***\nShuffling {subject} Questions...\n***")

#Iterate through the shuffled questions
for q, a in question_bank:
    user_answer = input(f"\n{q}\nYour Answer: ")

    #Check if the user's answer is correct
    if user_answer.lower() == a.lower(): #.lower() makes the match case-insensitive
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is: {a}")

#Display the final score
print("\n-----\nStudy Quest Complete!\n-----")

#to calculate percentage
percent= ((score / MAX_QUESTIONS) * 100)

#if statement to display appropriate message based on percentage
if (percent > 60):
    print(f"\nYou got {score} out of {MAX_QUESTIONS} questions correct. Great job, {subject} scholar!")
else:
    print(f"\nYou got {score} out of {MAX_QUESTIONS} questions correct. Good try! Better luck with {subject} next time.")
