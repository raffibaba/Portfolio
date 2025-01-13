#Raffi Barber
#1/9
#Multiplication Quiz

#Init

import random
correctAnswer = 0

#Functions
def finalQuiz():
    def Quiz1():
        global correctAnswer
        howMany = input("How many questions would you like?")
        howManyint = int(howMany)
        for i in range(howManyint):
            list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            num1 = int(random.choice(list1))
            num2 = int(random.choice(list1))
            num3 = int(num1*num2)
            print("What is " + str(num1) + " times " + str(num2) + "?")
            answer = input("Type your answer here:")
            answerint = int(answer)
            if answerint == num3:
                print("Correct!")
                correctAnswer = correctAnswer + 1
            else:
                print("Incorrect.")
        quizPercent = correctAnswer/howManyint*100
        print("You got a " + str(quizPercent) + " percent on this quiz, or a " + str(correctAnswer) + "/" + str(howManyint))
    def Quiz2():
        global correctAnswer
        howMany = input("How many questions would you like?")
        howManyint = int(howMany)
        for i in range(howManyint):
            num1 = random.randint(0, 20)
            num2 = random.randint(0, 10)
            num3 = int(num1*num2)
            print("What is " + str(num1) + " times " + str(num2) + "?")
            answer = input("Type your answer here:")
            answerint = int(answer)
            if answerint == num3:
                print("Correct!")
                correctAnswer = correctAnswer + 1
            else:
                print("Incorrect.")
        quizPercent = correctAnswer/howManyint*100
        print("You got a " + str(quizPercent) + " percent on this quiz, or a " + str(correctAnswer) + "/" + str(howManyint))
    def Quiz3():
        global correctAnswer
        howMany = input("How many questions would you like?")
        howManyint = int(howMany)
        for i in range(howManyint):
            num1 = random.randint(0, 20)
            num2 = random.randint(0, 20)
            num3 = int(num1*num2)
            print("What is " + str(num1) + " times " + str(num2) + "?")
            answer = input("Type your answer here:")
            answerint = int(answer)
            if answerint == num3:
                print("Correct!")
                correctAnswer = correctAnswer + 1
            else:
                print("Incorrect.")
        quizPercent = correctAnswer/howManyint*100
        print("You got a " + str(quizPercent) + " percent on this quiz, or a " + str(correctAnswer) + "/" + str(howManyint))
    def quizPicker():
        print("Which quiz difficulty would you like: 0, 1, or 2?")
        quiz = input("Which quiz?")
        quiz = int(quiz)
        if quiz == 0:
            Quiz1()
        elif quiz == 1:
            Quiz2()
        elif quiz == 2:
            Quiz3()
    quizPicker()
#Main
finalQuiz()

