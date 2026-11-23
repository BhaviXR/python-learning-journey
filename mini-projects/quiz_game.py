
# PYTHON QUIZ MASTER

questions = [
    ("Which language are we learning?", ["A. Java", "B. Python", "C. C++", "D. HTML"], "B"),
    ("What does len() do?", ["A. Add", "B. Delete", "C. Count", "D. Sort"], "C"),
    ("Which loop repeats over a sequence?", ["A. for", "B. if", "C. else", "D. break"], "A"),
    ("Which symbol is used for comments?", ["A. //", "B. <!--", "C. #", "D. **"], "C"),
    ("What is 2 ** 3?", ["A. 6", "B. 8", "C. 9", "D. 5"], "B")
]

score = 0

print("\n===== PYTHON QUIZ MASTER =====")

for i, (question, options, answer) in enumerate(questions, 1):
    print(f"\nQ{i}. {question}")
    for option in options:
        print(option)

    user = input("Your answer: ").upper()

    if user == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {answer}")

print("\n===== FINAL RESULT =====")
print("Score:", score, "/", len(questions))
print("Percentage:", score / len(questions) * 100, "%")

if score == len(questions):
    print("Excellent work!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practising!")
