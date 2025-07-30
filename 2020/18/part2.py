# with help from https://www.youtube.com/watch?v=TwKWUj033vY

DIGITS = '0123456789'


class Parser:
    def __init__(self, lexems):
        self.lexems = lexems
        self.current_token = None
        self.advance()

    def advance(self):
        try:
            res = next(self.lexems)
            self.current_token = res
        except StopIteration:
            self.current_token = None

    def term(self):
        result = self.expresion()

        while self.current_token is not None and self.current_token == '*':
            if self.current_token == '*':
                self.advance()
                result = result * self.expresion()
        return result

    def expresion(self):
        result = self.factor()

        while self.current_token is not None and self.current_token == '+':
            if self.current_token == '+':
                self.advance()
                result = result + self.factor()
        return result

    def factor(self):
        result = self.current_token
        if isinstance(self.current_token, int):
            self.advance()
            return result
        elif self.current_token == '(':
            self.advance()
            result = self.term()
            if self.current_token != ')':
                raise('parens error')
            self.advance()
            return result

        return None


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
    res = Parser(iter(lexems)).term()
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
