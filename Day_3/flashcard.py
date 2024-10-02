import os
import random
import json

quizzes = {}

def load_quizzes():
    if os.path.exists("Test.json"):
        try:
            with open("Test.json", "r") as file:
                global quizzes
                quizzes = json.load(file)
                print("Quizzes loaded successfully!")
        except json.JSONDecodeError:
            print("❌ Error decoding the JSON file. Starting fresh.")
            quizzes.clear()

def adding_quiz():
    ask_quiz = input("😉Enter the question: \n")
    ask_answer = input("\n😎Enter the answer: \n")
    quizzes[ask_quiz] = ask_answer
    print(f"\n✅Quiz added: {ask_quiz} | Answer: {ask_answer}")
    saving_willing = int(input("Do you want to save the question in file?"
                               "\n1.Yes"
                               "\n2.No"))
    if saving_willing == 1:
        with open("Test.json", "w") as file:
            json.dump(quizzes, file)
        print("Test was saved!")
    elif saving_willing == 2:
        print("Test was not saved!")

    else:
        print("Please enter a valid choice!")



def viewing_questions():
    if not quizzes:
        print("\n❌No quizzes available!")
    else:
        total_questions = len(quizzes)
        print(f"\nThere are {total_questions} questions!🍋")
        for question, answer in quizzes.items():

            print(f"\n✅Question: {question} | Answer: {answer}")

def testing(quizzes):
    corrects =  []
    if not quizzes:
        print("\n❌No questions available right now!")
        return

    questions = list(quizzes.keys())
    random.shuffle(questions)
    corrects = 0

    while True:
        for question in questions:
            print(question)
            user_answer = input("\n😉Enter the answer: ")
            if user_answer.lower() == quizzes[question].lower():
                corrects +=1
                print("\n✅CORRECT!")


            else:
                print("\n❌INCORRECT!")
        percentage = corrects*100/len(questions)
        print(f"\n😉You got {corrects} answers correct of out {len(questions)} questions!\nPercentage: {percentage}%")
        user_willing = int(input("Do you want to resolve the test?"
                             "\n\n1. Yes"
                             "\n\n2. No"
                             "\n\nChoice: "))

        if user_willing == 1:
            continue

        elif user_willing == 2:
            break

        else:
            print("\nPlease, enter a valid choice!")
            continue






def main():
    load_quizzes()
    while True:
        print("\n😊Welcome to our flashcard maker!")
        options = int(input("\n🔔Choose an option you want:"
                            "\n\n1. Add question"
                            "\n2. View questions"
                            "\n3. Quiz test"
                            "\n4. Exit"
                            "\n\nYour choice: "))
        if options == 1:
            adding_quiz()
        elif options == 2:
            viewing_questions()
        elif options == 3:
            testing(quizzes)
        elif options == 4:
            print("\nThank you for being with us!")
            break
        else:
            print("\nPlease choose one of the choices!")
            continue




if __name__ == "__main__":
    main()