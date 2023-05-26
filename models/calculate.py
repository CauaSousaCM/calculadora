from random import randint

class Calculate:
    def __init__(self, difficulty_level: int, /) -> None:
        self.__difficulty_level : int = difficulty_level
        self.__value1: float = self._generate_value
        self.__value2: float = self._generate_value
        self.__operation : int = randint(1, 3) # 1 = somar  \ 2 = subtrair \ 3 = multiplicar\ 
        self.__result : float = self._generate_result
    
    @property
    def difficult(self: object) -> int:
        return self.__difficulty_level
                
    @property
    def value1(self: object) -> int:
        return self.__value1
    
    @property
    def value2(self: object) -> int:
        return self.__value2
    
    @property 
    def operation(self: object) -> int:
        return self.__operation
    
    @property 
    def result(self: object) -> int:
        return self.__result
    
    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Somar'
        elif self.operation == 2:
            op = 'Subtrair'
        elif self.operation == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return (f'Valor 1: {self.value1}\nValor 2: {self.value2}'\
                f' \nDificuldade: {self.difficult}\n'\
                f'Operação: {op}')
        
    @property
    def _generate_value(self: object) -> int:
        if self.difficult == 1:
            return randint(0, 10)
        elif self.difficult == 2:
            return randint(0, 100)
        elif self.difficult == 3:
            return randint(0, 1000)
        elif self.difficult == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)
    
    @property
    def _generate_result(self:object) -> int:
        if self.operation == 1:
            return (self.value1 + self.value2)
        elif self.operation == 2:
            return (self.value1 - self.value2)
        else:
            return (self.value1 * self.value2)
        
    @property
    def _op_symbol(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'
        
    def check_result(self: object, response: int) -> bool:
        right: bool = False
        if self.result == response:
            print('Resposta correta!')
        else:
            print('Resposta Errada!')
        print(
            f'{self.value1} {self._op_symbol} '\
            f'{self.value2} = {self.result}'
        )
        return right
    
    def print_operation(self: object) -> None:
        print(
            f'{self.value1} {self._op_symbol} '\
            f'{self.value2} = ?'
        )
    