def check_double_digits(num):
    for i in range(len(num) - 1):
        if num[i] == num[i+1]:
            return True
    return False


def check_ascending(num):
    num = [d for d in num]
    num_sorted = [d for d in num]
    num_sorted.sort()
    print(f'num: {num}')
    print(f'num_sorted: {num_sorted}')
    return num_sorted == num


# max is 643603
count = 0
for i in range(171309, 643604):
    num = str(i)
    if not check_double_digits(num):
        continue
    if not check_ascending(num):
        continue
    count += 1

print(count)
