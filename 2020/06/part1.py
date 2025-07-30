answers = []
with open('input.txt') as f:
    answer = set()
    for line in f:
        if line.strip() == "":
            answers.append(answer)
            answer = set()
        for char in line.strip():
            answer.add(char)
answers.append(answer)
print(answers)

total = 0
for answer in answers:
    total += len(answer)
print(total)
