def check_double_digits(num):
    if ((num[0] == num[1]) and (num[1] != num[2])):
        return True

    for i in range(1, len(num) - 2):
        if ((num[i] == num[i+1]) and (num[i+2] != num[i+1]) and (num[i] != num[i-1])):
            return True

    if ((num[-1] == num[-2]) and (num[-2] != num[-3])):
        return True

    return False


def check_ascending(num):
    num = [d for d in num]
    num_sorted = [d for d in num]
    num_sorted.sort()
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
