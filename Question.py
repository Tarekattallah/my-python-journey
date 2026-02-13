"""
Simple quiz asking the user for the capital of Egypt.
User has 4 attempts to guess the correct answer.
"""

secret_answer = "Cairo"
answer = ""
limit = 4
count = 0
lose = False

while answer != secret_answer and not lose:
    if count < limit:
        answer = input("What is the capital of Egypt? ")
        count += 1
    else:
        lose = True

if lose:
    print(f"You lose! The correct answer is {secret_answer}.")
else:
    print("Congratulations, you win!")
