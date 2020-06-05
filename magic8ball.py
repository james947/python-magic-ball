# Allow the user to input their question.
# Show an in progress message.
# Create 10/20 responses, and show a random response.
# Allow the user to ask another question/advice or quit the game.

import random
import time

answers = ["Yes that was the answer", "B is the answer", "Man sina idea"]

def ask_question():
    get_question = input("\nAsk question please\n")
    
    print("\n loading ...\n")
    time.sleep(3)

    random_ans = random.choice(answers)

    print("\n The answer is -> {}\n".format(random_ans))

    ask_another_question = int(input("Enter 1 to ask another question or 0 to exit\n"))

    if ask_another_question == 1:
        ask_question()
    else:
        print("Good bye ...")
        return


ask_question()

