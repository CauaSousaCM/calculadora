from models.calculate import Calculate

def main() -> None: 
    points: int = 0
    play(points)
    
def play(points: int) -> None:
    difficulty: int = int(input(
        'Informe o nível de dificuldade desejado [1, 2, 3, 4]:'
    ))
    calc: Calculate = Calculate(difficulty) 
    calc.print_operation()

    result: int = int(input())
    
    if calc.check_result(result):
        points += 1
        print(f'Você tem: {points} ponto(s).')
    
    continue_in_game: int = int(input(
        'Deseja continuar no jogo? [1 - sim, 0 - não]'
    )) 
    
    if continue_in_game:
        play(points)
    else:
        print(f'Você finalizou com {points} ponto(s).')
        print('Até a proxima!')
    
if __name__ == '__main__':
    main()
