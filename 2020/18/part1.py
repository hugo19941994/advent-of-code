DIGITS = '0123456789'
def parse(lexems):
    result = 0
    current_op = None
    current_num = None
    try:
        while (lexem := next(lexems)):
            if isinstance(lexem, int):
                if current_num is None:
                    current_num = lexem
                else:
                    if current_op == '+':
                        result = current_num + lexem
                    elif current_op == '*':
                        result = current_num * lexem
                    current_num = result
                    current_op = None
            elif lexem == '+':
                current_op = '+'
            elif lexem == '*':
                current_op = '*'
            elif lexem == '(':
                res = parse(lexems)
                if current_num is None:
                    current_num = res
                else:
                    if current_op == '+':
                        result = current_num + res
                    elif current_op == '*':
                        result = current_num * res
                    current_num = result
                    current_op = None
            elif lexem == ')':
                return result
    except StopIteration:
        return result


def lex(l):
    lexems = []
    current_char = ''
    for char in l:
        if char == '+':
            lexems.append('+')
        elif char == '*':
            lexems.append('*')
        elif char == ' ':
            if current_char != '':
                lexems.append(int(current_char))
                current_char = ''
        elif char in DIGITS:
            current_char += char
        elif char == '(':
            lexems.append('(')
        elif char == ')':
            if current_char != '':
                lexems.append(int(current_char))
                current_char = ''
            lexems.append(')')

    if current_char != '':
        lexems.append(int(current_char))

    print(lexems)
    res = parse(iter(lexems))
    print(res)
    return res



def eval(l):
    current_token = ''
    try:
        while (c := next(l)):
            if c == '+':
                return int(current_token) + eval(l)
            if c == '*':
                return int(current_token) * eval(l)
            if c == ' ':
                pass
            if c == '(':
                return eval(l)
            if c == ')':
                return int(current_token)
            elif c in DIGITS:
                current_token += c
        return int(current_token)
    except:
        return int(current_token)


total = 0
with open('input.txt') as f:
    for line in f:
        l = iter(line.strip())
        total += lex(l)

print(total)
# 7059707 too low
# 557863721 too low
# 1386799940801 too low
# 1451467526514