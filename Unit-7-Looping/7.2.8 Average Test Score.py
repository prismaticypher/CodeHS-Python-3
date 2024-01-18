total_score = 0

for i in range(1, 4):
    test_score = int(input(f"Enter your score {1}: "))
    total_score += test_score

print(f"Your average score is {total_score / 3}")