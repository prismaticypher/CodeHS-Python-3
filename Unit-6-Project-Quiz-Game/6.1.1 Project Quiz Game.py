correct_answers = 0

def get_answer(answer):
    if answer == "a":
        print("Correct!")
        global correct_answers
        correct_answers += 1
    else:
        print("Incorrect.")

print("Multiple-Choice Quiz Game")
print("")

# Question 1
print("1. What is the capital of France?")
print("(a) Paris")
print("(b) London")
print("(c) Rome")
print("")

user_input_1 = get_answer(input("> ").lower())

# Question 2
print("")
print("2. Which planet is known as the Red Planet?")
print("(a) Mars")
print("(b) Venus")
print("(c) Jupiter")
print("")

user_input_2 = get_answer(input("> ").lower())

# Question 3
print("")
print("3. Who painted the Mona Lisa?")
print("(a) Leonardo da Vinci")
print("(b) Pablo Picasso")
print("(c) Vincent van Gogh")
print("")

user_input_3 = get_answer(input("> ").lower())

print("")
print("Quiz complete!")
print(f"You answered {correct_answers} out of 3 questions correctly.")