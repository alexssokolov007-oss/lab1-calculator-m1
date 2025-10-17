class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        if text:
            self.current_char = text[0]
        else:
            self.current_char = None
    
    def next_char(self):
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
        else:
            self.current_char = None
    
    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.next_char()
    
    def read_number(self):
        number_str = ""
        dot_count = 0
        
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    raise ValueError("В числе не может быть две точки!")
            number_str += self.current_char
            self.next_char()
        
        if dot_count == 0:
            return int(number_str)
        else:
            return float(number_str)

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit() or self.current_char == '.':
                number_value = self.read_number()
                return {'type': 'NUMBER', 'value': number_value}

            if self.current_char == '+':
                self.next_char()
                return {'type': 'PLUS'}
            
            if self.current_char == '-':
                self.next_char()
                return {'type': 'MINUS'}
            
            if self.current_char == '*':
                self.next_char()
                if self.current_char == '*':
                    self.next_char()
                    return {'type': 'POWER'}
                return {'type': 'MULTIPLY'}
            
            if self.current_char == '/':
                self.next_char()
                if self.current_char == '/':
                    self.next_char()
                    return {'type': 'INT_DIVIDE'}
                return {'type': 'DIVIDE'}
            
            if self.current_char == '%':
                self.next_char()
                return {'type': 'MODULO'}
            
            if self.current_char == '(':
                self.next_char()
                return {'type': 'LEFT_BRACKET'}
            
            if self.current_char == ')':
                self.next_char()
                return {'type': 'RIGHT_BRACKET'}
            
            raise ValueError(f"Непонятный символ: '{self.current_char}'")
        
        return {'type': 'END'}

class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.current_token = self.tokenizer.get_next_token()

    def check_and_move(self, expected_type):
        if self.current_token['type'] == expected_type:
            self.current_token = self.tokenizer.get_next_token()
        else:
            raise SyntaxError(f"Ожидался {expected_type}, а получили {self.current_token['type']}")

    def process_factor(self):
        token = self.current_token

        if token['type'] in ['PLUS', 'MINUS']:
            self.check_and_move(token['type'])
            result = self.process_factor()
            if token['type'] == 'MINUS':
                return -result
            return result

        if token['type'] == 'NUMBER':
            value = token['value']
            self.check_and_move('NUMBER')
            return value

        if token['type'] == 'LEFT_BRACKET':
            self.check_and_move('LEFT_BRACKET')
            result = self.process_expression()
            self.check_and_move('RIGHT_BRACKET')
            return result
        
        raise SyntaxError("Некорректное выражение")

    def process_power(self):
        result = self.process_factor()
        
        while self.current_token['type'] == 'POWER':
            self.check_and_move('POWER')
            result **= self.process_power()
        
        return result

    def process_term(self):
        result = self.process_power()
        
        while self.current_token['type'] in ['MULTIPLY', 'DIVIDE', 'INT_DIVIDE', 'MODULO']:
            operation = self.current_token['type']
            self.check_and_move(operation)
            
            right_value = self.process_power()
            
            if operation == 'MULTIPLY':
                result *= right_value
            elif operation == 'DIVIDE':
                if right_value == 0:
                    raise ZeroDivisionError("Нельзя делить на ноль!")
                result /= right_value
            elif operation == 'INT_DIVIDE':
                if right_value == 0:
                    raise ZeroDivisionError("Нельзя делить на ноль!")
                result //= right_value
            elif operation == 'MODULO':
                if right_value == 0:
                    raise ZeroDivisionError("Нельзя делить на ноль!")
                result %= right_value
        
        return result

    def process_expression(self):
        result = self.process_term()
        
        while self.current_token['type'] in ['PLUS', 'MINUS']:
            operation = self.current_token['type']
            self.check_and_move(operation)
            
            right_value = self.process_term()
            
            if operation == 'PLUS':
                result += right_value
            elif operation == 'MINUS':
                result -= right_value
        
        return result

    def parse(self):
        result = self.process_expression()
        
        if self.current_token['type'] != 'END':
            raise SyntaxError("В выражении есть лишние символы")
        
        return result

def calculate_expression(expression: str) -> float:
     """
    Вычисляет математическое выражение expression - 
    строка с выражением возвращает результат вычисления
    :return: результат вычисления как float
    :raises IndexError: если недостаточно операндов для операции
    :raises ZeroDivisionError: если деление на ноль
    :raises ValueError: при недопустимом токене или оставшихся лишних операндах
    """
    expression = expression.strip()
    if not expression:
        raise ValueError("Выражение не может быть пустым")
    
    token_maker = Tokenizer(expression)
    expression_parser = Parser(token_maker)
    
    result = expression_parser.parse()
    
    return result
