# study-quest-shuffler
A simple python program that serves as a memorization study tool for students at any level with any program specialization. 

There are four main functions of this program. 
1) Program prompts user to enter the number of questions for the session.
The input() function is used to allow the user to enter the number of questions they want to practice memorizing for the session.

2) Program prompts user to enter each question and corresponding answer.
The while loop in the program is controlled by the number the user enters. In other words, it determines the amount of times the program will ask for the question and the corresponding answer to the question. The responses are stores in a list called 'question_bank'.

3) Program randomly shuffles the order of the questions, allows user to input and match it to the answer.
The random module is imported to the program and thhe shuffle() function is used to randomize the questions stored in the question bank and displays it to the user. The input()     function is used to allowed the user to enter their answer to the question. The input is validated by checking if it matched the answer entered previously.

4) Program displays the tally of scores to user.
Throughout the program, the count variable 'score' is increased by 1 if the answer is correct. This is then used to calculate the percentage of accuracy at the end of the           program. The tally of the score against the number of question is displayed. The out put statement differs based on the percentage. If the percentage is greater than 60%, the       output statement says "Great job!" and if not, the output statement says "Good try!".

Overall, the program runs smoothly and it is completely case-insensitive. 

Room for improvement for the Study Quest Shuffler includes allowing the user to start another study session with the same question submitted and to start another session completely. I want to also look into a GUI interface.

