from game_functions import draw_board, move, rules, settings

while(true):
		print("1. Play the Game")
		print("2. Game Rules")
		print("3. Settings(?)")
		op = int(input("Select a number from 1 to 3 : "))
		if (op == 0):
			break
		elif op == 1:
			draw_board() #desenha tabuleiro
			block = Block() #criar objeto block
			position = move(block) 
		elif op == 2:
			rules()
		elif op == 3:
			settings()