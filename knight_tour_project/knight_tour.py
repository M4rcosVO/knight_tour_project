
def knight_tour(n):
    # Inicializa o tabuleiro com zeros
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Possíveis movimentos do cavalo
    h = [2, 1, -1, -2, -2, -1, 1, 2]
    v = [1, 2, 2, 1, -1, -2, -2, -1]

    # Função recursiva de backtracking
    def tenta(i, x, y):
        if i == n * n + 1:
            return True  # Todos os quadrados visitados

        for m in range(8):
            xn, yn = x + h[m], y + v[m]
            if 0 <= xn < n and 0 <= yn < n and board[xn][yn] == 0:
                board[xn][yn] = i
                if tenta(i + 1, xn, yn):
                    return True
                board[xn][yn] = 0  # backtrack

        return False

    # Começa pela posição (0, 0)
    board[0][0] = 1
    if tenta(2, 0, 0):
        for row in board:
            print(' '.join(f"{cell:2}" for cell in row))
    else:
        print("Não há solução.")

# Exemplo de execução
if __name__ == "__main__":
    knight_tour(5)
