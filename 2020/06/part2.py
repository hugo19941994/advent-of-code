from collections import defaultdict
answers = []
with open('input.txt') as f:
    answer = defaultdict(int)
    for line in f:
        if line.strip() == "":
            answers.append(answer)
            answer = defaultdict(int)
            continue
        answer['total'] += 1
        for char in line.strip():
            answer[char] += 1
answers.append(answer)
print(answers)

total = 0
for answer in answers:
    local_total = answer['total']
    for key, value in answer.items():
        if key == 'total':
            continue
        if value == local_total:
            total += 1
print(total)
