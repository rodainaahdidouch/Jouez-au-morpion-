def enter_move(board):
	ok = False	# hypothèse fictive – nous en avons besoin pour entrer dans la boucle
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # La saisie de l’utilisateur est-elle valide ?
		if not ok:
			print("Bad move - repeat your input!") # Non, ce n’est pas ça – recommence la saisie
			continue
		move = int(move) - 1 	# Numéro de cellule de 0 à 8
		row = move // 3 	# Ligne de la cellule
		col = move % 3		# Colonne de la cellule
		sign = board[row][col]	# cocher la case sélectionnée
		ok = sign not in ['O','X'] 
		if not ok:	# C’est occupé – retour à l’entrée
			print("Champ déjà utilisé - veuillez saisir à nouveau votre entrée !")
			continue
	board[row][col] = 'O' 	# Définir « 0 » dans la case sélectionnée


def make_list_of_free_fields(board):
	free = []	
	for row in range(3): # Parcourir les lignes
		for col in range(3): # Parcourir les colonnes
			if board[row][col] not in ['O','X']: # La cellule est-elle libre ?
				free.append((row,col)) # Oui, c’est ça : ajouter un nouveau tuple à la liste
	return free


def victory_for(board,sgn):
	if sgn == "X":	# Est-ce qu’on cherche X ?
		who = 'me'	# oui - c’est du côté de l’ordinateur
	elif sgn == "O": # ... ou pour O ?
		who = 'you'	# oui – c’est notre camp
	else:
		who = None	# On ne doit pas tomber ici !
	cross1 = cross2 = True  # pour les diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# vérifier la ligne rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # Vérifier la colonne rc
			return who
		if board[rc][rc] != sgn: # Vérifier la première diagonale
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # Vérifier la deuxième diagonale
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # dresser une liste des champs libres
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X' # Placer le premier « X » au milieu
free = make_list_of_free_fields(board)
human_turn = True # C’est à qui maintenant ?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("Vous avez gagné!")
elif victor == 'me':
	print("J’ai gagné")
else:
	print("Égalité!")
