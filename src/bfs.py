from collections import deque
from player import Player
from arena import Arena, WALL

def bfs(player, golden_block, black_blcok):
    # Cria um objeto Arena e um objeto Player
    
   

    # Define a posição de destino
 
    # Cria uma fila para armazenar os próximos nós a serem explorados
    queue = deque([((player.x,player.y), 0)])

    # Cria um conjunto para armazenar as posições visitadas
    visited = set(([player.x,player.y]))

    while queue:
        # Pega o próximo nó da fila
        current_pos_X,current_pos_Y, distance = queue.popleft()

        # Verifica se chegou ao destino
        if current_pos_X == golden_block[0] and current_pos_Y==golden_block[1]:
            return distance

        # Expande os nós adjacentes
        
        if(player.state=="UP"):
         for r, c in [(current_pos_X-1,current_pos_Y), (current_pos_X, current_pos_Y+1), (current_pos_X+1, current_pos_Y), (current_pos_X, current_pos_Y-1)]:
            # Verifica se a posição é válida
            if arena.is_valid_pos(r, c) and (r, c) not in visited:
                # Verifica se a posição é uma parede
                if arena.get_pos_content(r, c) == WALL:
                    continue

                # Marca a posição como visitada
                visited.add((r, c))

                # Adiciona a posição à fila
                queue.append(((r, c), distance+1))

    # Se não foi possível chegar ao destino, retorna -1
    return -1

