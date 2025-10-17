class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[0] if text else None
    
    def next(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
    
    def skip_spaces(self):
        while self.current_char and self.current_char == ' ':
            self.next()
    
    def read_num(self):
        s = ""
        dots = 0
        while self.current_char and (self.current_char in '1234567890.'):
            if self.current_char == '.':
                dots += 1
                if dots > 1:
                    raise ValueError("Две точки в числе!")
            s += self.current_char
            self.next()
        
        if dots == 0:
            return int(s)
        else:
            return float(s)
    
    def get_token(self):
        while self.current_char:
            if self.current_char == ' ':
                self.skip_spaces()
                continue
            
            if self.current_char in '1234567890.':
                num = self.read_num()
                return {'type': 'NUM', 'val': num}
            
            # операции
            if self.current_char == '+':
                self.next()
                return {'type': '+'}
            
            if self.current_char == '-':
                self.next()
                return {'type': '-'}
            
            if self.current_char == '*':
                self.next()
                if self.current_char == '*':
                    self.next()
                    return {'type': '**'}
                return {'type': '*'}
            
            if self.current_char == '/':
                self.next()
                if self.current_char == '/':
                    self.next()
                    return {'type': '//'}
                return {'type': '/'}
            
            if self.current_char == '%':
                self.next()
                return {'type': '%'}
            
            if self.current_char == '(':
                self.next()
                return {'type': '('}
            
            if self.current_char == ')':
                self.next()
                return {'type': ')'}
            
            raise ValueError(f"Неизвестный символ: {self.current_char}")
        
        return {'type': 'END'}


class Parser:
    def __init__(self, tokenizer):
        self.t = tokenizer
        self.cur_tok = self.t.get_token()
    
    def eat(self, typ):
        if self.cur_tok['type'] == typ:
            self.cur_tok = self.t.get_token()
        else:
            raise SyntaxError(f"Ожидалось {typ}, но получили {self.cur_tok['type']}")
    
    def factor(self):
        tok = self.cur_tok
        
        if tok['type'] in ['+', '-']:
            self.eat(tok['type'])
            res = self.factor()
            return -res if tok['type'] == '-' else res
        
        if tok['type'] == 'NUM':
            val = tok['val']
            self.eat('NUM')
            return val
        
        if tok['type'] == '(':
            self.eat('(')
            res = self.expr()
            self.eat(')')
            return res
        
        raise SyntaxError("Ошибка в выражении")
    
    def power(self):
        res = self.factor()
        
        while self.cur_tok['type'] == '**':
            self.eat('**')
            res **= self.power()
        
        return res
    
    def term(self):
        res = self.power()
        
        while self.cur_tok['type'] in ['*', '/', '//', '%']:
            op = self.cur_tok['type']
            self.eat(op)
            right = self.power()
            
            if op == '*':
                res *= right
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError("Деление на 0!")
                res /= right
            elif op == '//':
                if right == 0:
                    raise ZeroDivisionError("Деление на 0!")
                res //= right
            elif op == '%':
                if right == 0:
                    raise ZeroDivisionError("Деление на 0!")
                res %= right
        
        return res
    
    def expr(self):
        res = self.term()
        
        while self.cur_tok['type'] in ['+', '-']:
            op = self.cur_tok['type']
            self.eat(op)
            right = self.term()
            
            if op == '+':
                res += right
            else:
                res -= right
        
        return res
    
    def parse(self):
        result = self.expr()
        if self.cur_tok['type'] != 'END':
            raise SyntaxError("Лишние символы в конце")
        return result


def calculate_expression(s: str) -> float:
    s = s.strip()
    if s == "":
        raise ValueError("Пустая строка")
    
    t = Tokenizer(s)
    p = Parser(t)
    
    return p.parse()
