# -*- coding:Utf-8 -*-
from PySFML import sf
from random import randrange
from math import floor

def menu():
	"Affiche le menu avant de quitter"
	global etatDuJeu
	global carte
	
	texteContinuer, texteQuitter = sf.String("Continuer", police2, 30), sf.String("Quitter", police2, 30)
	texteContinuer.Move(fenetre.GetWidth() / 2 - texteContinuer.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteContinuer.GetRect().GetHeight() / 2 + 140)
	texteContinuer.SetColor(sf.Color(255, 0, 0))
	texteQuitter.Move(fenetre.GetWidth() / 2 - texteQuitter.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteQuitter.GetRect().GetHeight() / 2 + 180)
	choix = 1
	while etatDuJeu == 'COMMENCE':
		while fenetre.GetEvent(evenement):
			if Input.IsKeyDown(sf.Key.Up) or Input.IsKeyDown(sf.Key.Down):
				sonChoix.Play()
				if choix == 1:
					texteContinuer.SetColor(sf.Color(255, 255, 255))
					texteQuitter.SetColor(sf.Color(255, 0, 0))
					choix = 2
				elif choix == 2:
					texteContinuer.SetColor(sf.Color(255, 0, 0))
					texteQuitter.SetColor(sf.Color(255, 255, 255))
					choix = 1
				sf.Sleep(0.1)
			if Input.IsKeyDown(sf.Key.Return):
				sonChoix.Play()
				if choix == 1:
					return False
				elif choix == 2:
					carte = []
					for i in range(NBR_BLOCS_LARGEUR):
						carte.append(range(NBR_BLOCS_HAUTEUR))
					return True
		fenetre.Clear(sf.Color(0, 0, 0))
		fenetre.Draw(texteContinuer)
		fenetre.Draw(texteQuitter)
		fenetre.Display()

def chargerCarte(carte):
	for i in range(len(carte)):
		for j in range(len(carte[i])):
			if i == 0 or i == NBR_BLOCS_LARGEUR - 1:
				carte[i][j] = caseCarte['GRIS']
			else:
				carte[i][j] = caseCarte['VIDE']
			if j == 0 or j == NBR_BLOCS_HAUTEUR - 1:
				carte[i][j] = caseCarte['GRIS']

def peutDescendre(posDesCarres, carte, formeTetromino, rotationTetromino):
	if formeTetromino == caseCarte['BLEU']: #j
		if rotationTetromino == 1:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 2:
			if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
	elif formeTetromino == caseCarte['ORANGE']: #l
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 2:
			if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
		elif rotationTetromino == 3:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
	elif formeTetromino == caseCarte['TURQUOISE']: #i
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
							return True
		elif rotationTetromino == 2:
			if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
				return True
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
							return True
		elif rotationTetromino == 4:
			if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
				return True
	elif formeTetromino == caseCarte['JAUNE']: #o
		if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
			if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
				return True
	elif formeTetromino == caseCarte['VERT']: #s
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 2:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 4:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
	elif formeTetromino == caseCarte['VIOLET']: #t
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 2:
			if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
	elif formeTetromino == caseCarte['ROUGE']: #z
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 2:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						return True
		elif rotationTetromino == 4:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					return True
	return False

def rotationForme(posDesCarres, carte, formeTetromino):
	global rotationTetromino
	if formeTetromino == caseCarte['BLEU']: #j
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
				if carte[posDesCarres[0][0] + 2][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] = caseCarte['BLEU']
						posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1]]
						carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] = caseCarte['BLEU']
						posDesCarres[1] = [posDesCarres[1][0] + 1, posDesCarres[1][1]]
						carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] = caseCarte['BLEU']
						posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] + 1]
						carte[posDesCarres[3][0]][posDesCarres[3][1] - 1] = caseCarte['BLEU']
						posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] - 1]
						rotationTetromino = 2
		elif rotationTetromino == 2:
			if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] = caseCarte['BLEU']
						posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1] + 1]
						carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] = caseCarte['BLEU']
						posDesCarres[2] = [posDesCarres[2][0] + 1, posDesCarres[2][1] - 1]
						carte[posDesCarres[3][0]][posDesCarres[3][1] + 2] = caseCarte['BLEU']
						posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] + 2]
						rotationTetromino = 3
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0]][posDesCarres[1][1] - 1] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] = caseCarte['BLEU']
						posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] + 1]
						carte[posDesCarres[1][0]][posDesCarres[1][1] - 1] = caseCarte['BLEU']
						posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] - 1]
						carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] = caseCarte['BLEU']
						posDesCarres[2] = [posDesCarres[2][0] - 1, posDesCarres[2][1]]
						carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] = caseCarte['BLEU']
						posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1]]
						rotationTetromino = 4
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] - 2] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0]][posDesCarres[0][1] - 2] = caseCarte['BLEU']
						posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] - 2]
						carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] = caseCarte['BLEU']
						posDesCarres[1] = [posDesCarres[1][0] - 1, posDesCarres[1][1] + 1]
						carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] = caseCarte['BLEU']
						posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1] - 1]
						rotationTetromino = 1
	elif formeTetromino == caseCarte['ORANGE']: #l
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0] + 1][posDesCarres[0][1] - 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0] - 1][posDesCarres[2][1] + 2] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] + 1][posDesCarres[0][1] - 1] = caseCarte['ORANGE']
						posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1] - 1]
						carte[posDesCarres[2][0] - 1][posDesCarres[2][1] + 2] = caseCarte['ORANGE']
						posDesCarres[2] = [posDesCarres[2][0] - 1, posDesCarres[2][1] + 2]
						carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] = caseCarte['ORANGE']
						posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] + 1]
						rotationTetromino = 2
		elif rotationTetromino == 2:
			if carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0]][posDesCarres[3][1] - 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] = caseCarte['ORANGE']
						posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1] + 1]
						carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] = caseCarte['ORANGE']
						posDesCarres[1] = [posDesCarres[1][0] - 1, posDesCarres[1][1] + 1]
						carte[posDesCarres[2][0]][posDesCarres[2][1] - 1] = caseCarte['ORANGE']
						posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] - 1]
						carte[posDesCarres[3][0]][posDesCarres[3][1] - 1] = caseCarte['ORANGE']
						posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] - 1]
						rotationTetromino = 3
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] - 1] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1] - 2] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] - 1][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0]][posDesCarres[0][1] - 1] = caseCarte['ORANGE']
						posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] - 1]
						carte[posDesCarres[1][0] + 1][posDesCarres[1][1] - 2] = caseCarte['ORANGE']
						posDesCarres[1] = [posDesCarres[1][0] + 1, posDesCarres[1][1] - 2]
						carte[posDesCarres[3][0] - 1][posDesCarres[3][1] + 1] = caseCarte['ORANGE']
						posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1] + 1]
						rotationTetromino = 4
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] = caseCarte['ORANGE']
						posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] + 1]
						carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] = caseCarte['ORANGE']
						posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] + 1]
						carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] = caseCarte['ORANGE']
						posDesCarres[2] = [posDesCarres[2][0] + 1, posDesCarres[2][1] - 1]
						carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] = caseCarte['ORANGE']
						posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1] - 1]
						rotationTetromino = 1
	elif formeTetromino == caseCarte['TURQUOISE']: #i
		if rotationTetromino == 1:
			if carte[posDesCarres[0][0] + 2][posDesCarres[0][1] - 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] - 1][posDesCarres[3][1] + 2] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] + 2][posDesCarres[0][1] - 1] = caseCarte['TURQUOISE']
						posDesCarres[0] = [posDesCarres[0][0] + 2, posDesCarres[0][1] - 1]
						carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] = caseCarte['TURQUOISE']
						posDesCarres[1] = [posDesCarres[1][0] + 1, posDesCarres[1][1]]
						carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] = caseCarte['TURQUOISE']
						posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] + 1]
						carte[posDesCarres[3][0] - 1][posDesCarres[3][1] + 2] = caseCarte['TURQUOISE']
						posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1] + 2]
						rotationTetromino = 2
		elif rotationTetromino == 2:
			if carte[posDesCarres[0][0] - 2][posDesCarres[0][1] + 2] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] - 2][posDesCarres[0][1] + 2] = caseCarte['TURQUOISE']
						posDesCarres[0] = [posDesCarres[0][0] - 2, posDesCarres[0][1] + 2]
						carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] = caseCarte['TURQUOISE']
						posDesCarres[1] = [posDesCarres[1][0] - 1, posDesCarres[1][1] + 1]
						carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] = caseCarte['TURQUOISE']
						posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1] - 1]
						rotationTetromino = 3
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0] + 1][posDesCarres[0][1] - 2] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0]][posDesCarres[1][1] - 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] - 2][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] + 1][posDesCarres[0][1] - 2] = caseCarte['TURQUOISE']
						posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1] - 2]
						carte[posDesCarres[1][0]][posDesCarres[1][1] - 1] = caseCarte['TURQUOISE']
						posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] - 1]
						carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] = caseCarte['TURQUOISE']
						posDesCarres[2] = [posDesCarres[2][0] - 1, posDesCarres[2][1]]
						carte[posDesCarres[3][0] - 2][posDesCarres[3][1] + 1] = caseCarte['TURQUOISE']
						posDesCarres[3] = [posDesCarres[3][0] - 2, posDesCarres[3][1] + 1]
						rotationTetromino = 4
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 2][posDesCarres[3][1] - 2] == caseCarte['VIDE']:
						carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
						carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
						carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
						carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] = caseCarte['TURQUOISE']
						posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1] + 1]
						carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] = caseCarte['TURQUOISE']
						posDesCarres[2] = [posDesCarres[2][0] + 1, posDesCarres[2][1] - 1]
						carte[posDesCarres[3][0] + 2][posDesCarres[3][1] - 2] = caseCarte['TURQUOISE']
						posDesCarres[3] = [posDesCarres[3][0] + 2, posDesCarres[3][1] - 2]
						rotationTetromino = 1
	elif formeTetromino == caseCarte['VERT']: #s
		if rotationTetromino == 1:
			if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 2] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
						
					carte[posDesCarres[0][0] + 1][posDesCarres[0][1] - 1] = caseCarte['VERT']
					posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1] - 1]
					carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] = caseCarte['VERT']
					posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] + 1]
					carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] = caseCarte['VERT']
					posDesCarres[2] = [posDesCarres[2][0] + 1, posDesCarres[2][1]]
					carte[posDesCarres[3][0]][posDesCarres[3][1] + 2] = caseCarte['VERT']
					posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] + 2]
					rotationTetromino = 2
		elif rotationTetromino == 2:
			if carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 2] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0] - 1][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
					
					carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 2] = caseCarte['VERT']
					posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1] + 2]
					carte[posDesCarres[2][0] - 1][posDesCarres[2][1] + 1] = caseCarte['VERT']
					posDesCarres[2] = [posDesCarres[2][0] - 1, posDesCarres[2][1] + 1]
					carte[posDesCarres[3][0]][posDesCarres[3][1] - 1] = caseCarte['VERT']
					posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] - 1]
					rotationTetromino = 3
		elif rotationTetromino == 3:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] - 2] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
					
					carte[posDesCarres[0][0]][posDesCarres[0][1] - 2] = caseCarte['VERT']
					posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] - 2]
					carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] = caseCarte['VERT']
					posDesCarres[1] = [posDesCarres[1][0] - 1, posDesCarres[1][1]]
					carte[posDesCarres[2][0]][posDesCarres[2][1] - 1] = caseCarte['VERT']
					posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] - 1]
					carte[posDesCarres[3][0] - 1][posDesCarres[3][1] + 1] = caseCarte['VERT']
					posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1] + 1]
					rotationTetromino = 4
		elif rotationTetromino == 4:
			if carte[posDesCarres[1][0] + 1][posDesCarres[1][1] - 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 2] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
					
					carte[posDesCarres[0][0]][posDesCarres[0][1] + 1] = caseCarte['VERT']
					posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] + 1]
					carte[posDesCarres[1][0] + 1][posDesCarres[1][1] - 1] = caseCarte['VERT']
					posDesCarres[1] = [posDesCarres[1][0] + 1, posDesCarres[1][1] - 1]
					carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 2] = caseCarte['VERT']
					posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1] - 2]
					rotationTetromino = 1
	elif formeTetromino == caseCarte['VIOLET']: #t
		if rotationTetromino == 1:
			if carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] == caseCarte['VIDE']:
				carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
				carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
				carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					
				carte[posDesCarres[0][0] + 1][posDesCarres[0][1] - 1] = caseCarte['VIOLET']
				posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1] - 1]
				carte[posDesCarres[1][0]][posDesCarres[1][1] + 1] = caseCarte['VIOLET']
				posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] + 1]
				carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] = caseCarte['VIOLET']
				posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] + 1]
				rotationTetromino = 2
		elif rotationTetromino == 2:
			if carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] == caseCarte['VIDE']:
				carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
				carte[posDesCarres[0][0] - 1][posDesCarres[0][1] + 1] = caseCarte['VIOLET']
				posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1] + 1]
				rotationTetromino = 3
		elif rotationTetromino == 3:
			carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
			carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
			carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
			
			carte[posDesCarres[1][0]][posDesCarres[1][1] - 1] = caseCarte['VIOLET']
			posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] - 1]
			carte[posDesCarres[2][0]][posDesCarres[2][1] - 1] = caseCarte['VIOLET']
			posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] - 1]
			carte[posDesCarres[3][0] - 1][posDesCarres[3][1] + 1] = caseCarte['VIOLET']
			posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1] + 1]
			rotationTetromino = 4
		elif rotationTetromino == 4:
			if carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] == caseCarte['VIDE']:
				carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
				
				carte[posDesCarres[3][0] + 1][posDesCarres[3][1] - 1] = caseCarte['VIOLET']
				posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1] - 1]
				rotationTetromino = 1
	elif formeTetromino == caseCarte['ROUGE']: #z
		if rotationTetromino == 1:
			if carte[posDesCarres[1][0]][posDesCarres[1][1] + 2] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
				
					carte[posDesCarres[0][0] + 1][posDesCarres[0][1] + 1] = caseCarte['ROUGE']
					posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1] + 1]
					carte[posDesCarres[1][0]][posDesCarres[1][1] + 2] = caseCarte['ROUGE']
					posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] + 2]
					carte[posDesCarres[2][0] + 1][posDesCarres[2][1] - 1] = caseCarte['ROUGE']
					posDesCarres[2] = [posDesCarres[2][0] + 1, posDesCarres[2][1] - 1]
					rotationTetromino = 2
		elif rotationTetromino == 2:
			if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
				
					carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] = caseCarte['ROUGE']
					posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1]]
					carte[posDesCarres[1][0]][posDesCarres[1][1] - 1] = caseCarte['ROUGE']
					posDesCarres[1] = [posDesCarres[1][0], posDesCarres[1][1] - 1]
					carte[posDesCarres[2][0] - 1][posDesCarres[2][1] + 2] = caseCarte['ROUGE']
					posDesCarres[2] = [posDesCarres[2][0] - 1, posDesCarres[2][1] + 2]
					carte[posDesCarres[3][0]][posDesCarres[3][1] + 1] = caseCarte['ROUGE']
					posDesCarres[3] = [posDesCarres[3][0], posDesCarres[3][1] + 1]
					rotationTetromino = 3
		elif rotationTetromino == 3:
			if carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] == caseCarte['VIDE']:
				if carte[posDesCarres[2][0]][posDesCarres[2][1] - 2] == caseCarte['VIDE']:
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
				
					carte[posDesCarres[1][0] - 1][posDesCarres[1][1] + 1] = caseCarte['ROUGE']
					posDesCarres[1] = [posDesCarres[1][0] - 1, posDesCarres[1][1] + 1]
					carte[posDesCarres[2][0]][posDesCarres[2][1] - 2] = caseCarte['ROUGE']
					posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] - 2]
					carte[posDesCarres[3][0] - 1][posDesCarres[3][1] - 1] = caseCarte['ROUGE']
					posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1] - 1]
			rotationTetromino = 4
		elif rotationTetromino == 4:
			if carte[posDesCarres[0][0]][posDesCarres[0][1] - 1] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
					carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
					carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
					carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
					carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
				
					carte[posDesCarres[0][0]][posDesCarres[0][1] - 1] = caseCarte['ROUGE']
					posDesCarres[0] = [posDesCarres[0][0], posDesCarres[0][1] - 1]
					carte[posDesCarres[1][0] + 1][posDesCarres[1][1] - 2] = caseCarte['ROUGE']
					posDesCarres[1] = [posDesCarres[1][0] + 1, posDesCarres[1][1] - 2]
					carte[posDesCarres[2][0]][posDesCarres[2][1] + 1] = caseCarte['ROUGE']
					posDesCarres[2] = [posDesCarres[2][0], posDesCarres[2][1] + 1]
					carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] = caseCarte['ROUGE']
					posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1]]
				rotationTetromino = 1

def peutBouger(posDesCarres, carte, direction, formeTetromino, rotationTetromino):
	if direction == 'droite':
		if formeTetromino == caseCarte['BLEU']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['ORANGE']:
			if rotationTetromino == 1:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['TURQUOISE']:
			if rotationTetromino == 1:
				if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
					return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
								return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
					return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
								return True
		elif formeTetromino == caseCarte['JAUNE']:
			if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
				if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
					return True
		elif formeTetromino == caseCarte['VERT']:
			if rotationTetromino == 1:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['VIOLET']:
			if rotationTetromino == 1:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] + 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['ROUGE']:
			if rotationTetromino == 1:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[1][0] + 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] + 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] + 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
	elif direction == 'gauche':
		if formeTetromino == caseCarte['BLEU']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['ORANGE']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['TURQUOISE']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
								return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
								return True
		elif formeTetromino == caseCarte['JAUNE']:
			if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
				if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
					return True
		elif formeTetromino == caseCarte['VERT']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['VIOLET']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[3][0] - 1][posDesCarres[3][1]] == caseCarte['VIDE']:
							return True
		elif formeTetromino == caseCarte['ROUGE']:
			if rotationTetromino == 1:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 2:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							return True
			elif rotationTetromino == 3:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
						return True
			elif rotationTetromino == 4:
				if carte[posDesCarres[0][0] - 1][posDesCarres[0][1]] == caseCarte['VIDE']:
					if carte[posDesCarres[1][0] - 1][posDesCarres[1][1]] == caseCarte['VIDE']:
						if carte[posDesCarres[2][0] - 1][posDesCarres[2][1]] == caseCarte['VIDE']:
							return True
	return False

def bougerBlocs(posDesCarres, carte, direction, formeTetromino):
	carte[posDesCarres[0][0]][posDesCarres[0][1]] = caseCarte['VIDE']
	carte[posDesCarres[1][0]][posDesCarres[1][1]] = caseCarte['VIDE']
	carte[posDesCarres[2][0]][posDesCarres[2][1]] = caseCarte['VIDE']
	carte[posDesCarres[3][0]][posDesCarres[3][1]] = caseCarte['VIDE']
	
	if direction == 'gauche':
		posDesCarres[0] = [posDesCarres[0][0] - 1, posDesCarres[0][1]]
		posDesCarres[1] = [posDesCarres[1][0] - 1, posDesCarres[1][1]]
		posDesCarres[2] = [posDesCarres[2][0] - 1, posDesCarres[2][1]]
		posDesCarres[3] = [posDesCarres[3][0] - 1, posDesCarres[3][1]]
	elif direction == 'droite':
		posDesCarres[0] = [posDesCarres[0][0] + 1, posDesCarres[0][1]]
		posDesCarres[1] = [posDesCarres[1][0] + 1, posDesCarres[1][1]]
		posDesCarres[2] = [posDesCarres[2][0] + 1, posDesCarres[2][1]]
		posDesCarres[3] = [posDesCarres[3][0] + 1, posDesCarres[3][1]]
	
	carte[posDesCarres[0][0]][posDesCarres[0][1]] = formeTetromino
	carte[posDesCarres[1][0]][posDesCarres[1][1]] = formeTetromino
	carte[posDesCarres[2][0]][posDesCarres[2][1]] = formeTetromino
	carte[posDesCarres[3][0]][posDesCarres[3][1]] = formeTetromino

def ligneComplete(ligne):
	compteurCaseRemplie = 0
	for case in ligne:
		if case == caseCarte['BLEU'] or case == caseCarte['ORANGE'] or case == caseCarte['TURQUOISE'] or case == caseCarte['JAUNE']  or case == caseCarte['VERT'] or case == caseCarte['VIOLET'] or case == caseCarte['ROUGE']:
			compteurCaseRemplie = compteurCaseRemplie + 1
	if compteurCaseRemplie == 10:
		return True
	else:
		return False

def enleveLigne(carte, numLigne):
	i = 0
	j = 0
	i, j = len(carte) - 1, len(carte[i]) - 1
	while i > 0:
	 	j = len(carte[i]) - 1
		while j > 0:
			if j < numLigne and j > 0 and numLigne != -1:
				if carte[i][j] != caseCarte['GRIS']:
					carte[i][j + 1] = carte[i][j]
			j = j - 1
		i = i - 1

def afficheProchainTetromino(fenetre, prochaineForme, prochaineRotation):
	global spriteCBleu
	global spriteCOrange
	global spriteCTurquoise
	global spriteCJaune
	global spriteCVert
	global spriteCViolet
	global spriteCRouge
	
	prochaineFormeTableau = []
	for i in range(4):
		prochaineFormeTableau.append(range(4))
	for i in range(len(prochaineFormeTableau)):
		for j in range(len(prochaineFormeTableau[i])):
			prochaineFormeTableau[i][j] = 0
	c1 = [0, 0]
	c2 = [0, 0]
	c3 = [0, 0]
	c4 = [0, 0]
	if prochaineForme == caseCarte['BLEU']:
		if prochaineRotation == 1:
			c1 = [0, 0]
			c2 = [0, 1]
			c3 = [1, 1]
			c4 = [2, 1]
			positionXAAjouter = 305
			positionYAAjouter = 220
		elif prochaineRotation == 2:
			c1 = [1, 0]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [2, 0]
			positionXAAjouter = 295
			positionYAAjouter = 210
		elif prochaineRotation == 3:
			c1 = [0, 1]
			c2 = [1, 1]
			c3 = [2, 1]
			c4 = [2, 2]
			positionXAAjouter = 305
			positionYAAjouter = 200
		elif prochaineRotation == 4:
			c1 = [0, 2]
			c2 = [1, 0]
			c3 = [1, 1]
			c4 = [1, 2]
			positionXAAjouter = 317
			positionYAAjouter = 210
	elif prochaineForme == caseCarte['ORANGE']:
		if prochaineRotation == 1:
			c1 = [0, 1]
			c2 = [1, 1]
			c3 = [2, 0]
			c4 = [2, 1]
			positionXAAjouter = 305
			positionYAAjouter = 220
		elif prochaineRotation == 2:
			c1 = [1, 0]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [2, 2]
			positionXAAjouter = 295
			positionYAAjouter = 210
		elif prochaineRotation == 3:
			c1 = [0, 1]
			c2 = [0, 2]
			c3 = [1, 1]
			c4 = [2, 1]
			positionXAAjouter = 307
			positionYAAjouter = 200
		elif prochaineRotation == 4:
			c1 = [0, 0]
			c2 = [1, 0]
			c3 = [1, 1]
			c4 = [1, 2]
			positionXAAjouter = 317
			positionYAAjouter = 210
	elif prochaineForme == caseCarte['TURQUOISE']:
		if prochaineRotation == 1:
			c1 = [0, 1]
			c2 = [1, 1]
			c3 = [2, 1]
			c4 = [3, 1]
			positionXAAjouter = 295
			positionYAAjouter = 210
		elif prochaineRotation == 2:
			c1 = [2, 0]
			c2 = [2, 1]
			c3 = [2, 2]
			c4 = [2, 3]
			positionXAAjouter = 285
			positionYAAjouter = 198
		elif prochaineRotation == 3:
			c1 = [0, 2]
			c2 = [1, 2]
			c3 = [2, 2]
			c4 = [3, 2]
			positionXAAjouter = 295
			positionYAAjouter = 190
		elif prochaineRotation == 4:
			c1 = [1, 0]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [1, 3]
			positionXAAjouter = 306
			positionYAAjouter = 198
	elif prochaineForme == caseCarte['JAUNE']:
		c1 = [1, 1]
		c2 = [1, 2]
		c3 = [2, 1]
		c4 = [2, 2]
		positionXAAjouter = 295
		positionYAAjouter = 200
	elif prochaineForme == caseCarte['VERT']:
		if prochaineRotation == 1:
			c1 = [0, 1]
			c2 = [1, 0]
			c3 = [1, 1]
			c4 = [2, 0]
			positionXAAjouter = 306
			positionYAAjouter = 220
		elif prochaineRotation == 2:
			c1 = [1, 0]
			c2 = [1, 1]
			c3 = [2, 1]
			c4 = [2, 2]
			positionXAAjouter = 295
			positionYAAjouter = 210
		elif prochaineRotation == 3:
			c1 = [0, 2]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [2, 1]
			positionXAAjouter = 306
			positionYAAjouter = 198
		elif prochaineRotation == 4:
			c1 = [0, 0]
			c2 = [0, 1]
			c3 = [1, 1]
			c4 = [1, 2]
			positionXAAjouter = 318
			positionYAAjouter = 210
	elif prochaineForme == caseCarte['VIOLET']:
		if prochaineRotation == 1:
			c1 = [0, 1]
			c2 = [1, 0]
			c3 = [1, 1]
			c4 = [2, 1]
			positionXAAjouter = 307
			positionYAAjouter = 220
		elif prochaineRotation == 2:
			c1 = [1, 0]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [2, 1]
			positionXAAjouter = 297
			positionYAAjouter = 210
		elif prochaineRotation == 3:
			c1 = [0, 1]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [2, 1]
			positionXAAjouter = 307
			positionYAAjouter = 200
		elif prochaineRotation == 4:
			c1 = [0, 1]
			c2 = [1, 0]
			c3 = [1, 1]
			c4 = [1, 2]
			positionXAAjouter = 315
			positionYAAjouter = 210
	elif prochaineForme == caseCarte['ROUGE']:
		if prochaineRotation == 1:
			c1 = [0, 0]
			c2 = [1, 0]
			c3 = [1, 1]
			c4 = [2, 1]
			positionXAAjouter = 305
			positionYAAjouter = 220
		elif prochaineRotation == 2:
			c1 = [1, 1]
			c2 = [1, 2]
			c3 = [2, 0]
			c4 = [2, 1]
			positionXAAjouter = 295
			positionYAAjouter = 210
		elif prochaineRotation == 3:
			c1 = [0, 1]
			c2 = [1, 1]
			c3 = [1, 2]
			c4 = [2, 2]
			positionXAAjouter = 306
			positionYAAjouter = 200
		elif prochaineRotation == 4:
			c1 = [0, 1]
			c2 = [0, 2]
			c3 = [1, 0]
			c4 = [1, 1]
			positionXAAjouter = 317
			positionYAAjouter = 210
	prochaineFormeTableau[c1[0]][c1[1]] = prochaineForme
	prochaineFormeTableau[c2[0]][c2[1]] = prochaineForme
	prochaineFormeTableau[c3[0]][c3[1]] = prochaineForme
	prochaineFormeTableau[c4[0]][c4[1]] = prochaineForme
	
	positionX = 0
	positionY = 0
	for i in range(len(prochaineFormeTableau)):
		for j in range(len(prochaineFormeTableau[i])):
			positionX = i * TAILLE_BLOC
			positionY = j * TAILLE_BLOC
			
			if prochaineFormeTableau[i][j] == caseCarte['BLEU']:
				spriteCBleu.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCBleu)
			if prochaineFormeTableau[i][j] == caseCarte['ORANGE']:
				spriteCOrange.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCOrange)
			if prochaineFormeTableau[i][j] == caseCarte['TURQUOISE']:
				spriteCTurquoise.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCTurquoise)
			if prochaineFormeTableau[i][j] == caseCarte['JAUNE']:
				spriteCJaune.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCJaune)
			if prochaineFormeTableau[i][j] == caseCarte['VERT']:
				spriteCVert.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCVert)
			if prochaineFormeTableau[i][j] == caseCarte['VIOLET']:
				spriteCViolet.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCViolet)
			if prochaineFormeTableau[i][j] == caseCarte['ROUGE']:
				spriteCRouge.SetPosition(positionX + positionXAAjouter, positionY + positionYAAjouter)
				fenetre.Draw(spriteCRouge)

def partieTerminee():
	"Affiche les points et niveau avant de quitter"
	police = sf.Font()
	police.LoadFromFile("Données/Polices/HandSean.ttf", 20)
	
	musiqueGameOver = sf.Music()
	musiqueGameOver.OpenFromFile("Données/Sons/musiqueGameOver.wav")
	musiqueGameOver.SetLoop(True)
	musiqueGameOver.Play()
	if pointsJoueur > 1:
		chainePoints = 'Vous avez terminé avec ' + str(pointsJoueur) + ' points'
	else:
		chainePoints = 'Vous avez terminé avec ' + str(pointsJoueur) + ' point'
	chaineNiveau = 'Vous avez terminé au niveau ' + str(niveauJoueur)
	textePoints, texteNiveau, texteQuitter, texteTouche = sf.String(chainePoints, police, 20), sf.String(chaineNiveau, police, 20), sf.String("La partie est terminée.", police, 20), sf.String("Appuyez sur entrée pour quitter.", police, 20)
	textePoints.Move(fenetre.GetWidth() / 2 - textePoints.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - textePoints.GetRect().GetHeight() / 2 - 80)
	texteNiveau.Move(fenetre.GetWidth() / 2 - texteNiveau.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteNiveau.GetRect().GetHeight() / 2 - 40)
	texteQuitter.Move(fenetre.GetWidth() / 2 - texteQuitter.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteQuitter.GetRect().GetHeight() / 2)
	texteTouche.Move(fenetre.GetWidth() / 2 - texteQuitter.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteQuitter.GetRect().GetHeight() / 2 + 40)
	while etatDuJeu == 'GAME_OVER':
		while fenetre.GetEvent(evenement):
			if Input.IsKeyDown(sf.Key.Return):
				sf.Sleep(0.1)
				musiqueMenu.Play()
				return True
		fenetre.Clear(sf.Color(0, 0, 0))
		fenetre.Draw(textePoints)
		fenetre.Draw(texteNiveau)
		fenetre.Draw(texteQuitter)
		fenetre.Draw(texteTouche)
		fenetre.Display()

def eclaireLigne(carte, numeroLigneAEnlever, fenetre):#, enleve):
	#if enleve == False:
	i = 0
	j = 0
	i, j = len(carte) - 1, len(carte[i]) - 1
	while i > 0:
	 	j = len(carte[i]) - 1
		while j > 0:
			if j == numeroLigneAEnlever and numeroLigneAEnlever != -1:
				if carte[i][j] == caseCarte['BLEU']:
					carte[i][j] = caseCarte['BLEUE']
				if carte[i][j] == caseCarte['ORANGE']:
					carte[i][j] = caseCarte['ORANGEE']
				if carte[i][j] == caseCarte['TURQUOISE']:
					carte[i][j] = caseCarte['TURQUOISEE']
				if carte[i][j] == caseCarte['JAUNE']:
					carte[i][j] = caseCarte['JAUNEE']
				if carte[i][j] == caseCarte['VERT']:
					carte[i][j] = caseCarte['VERTE']
				if carte[i][j] == caseCarte['VIOLET']:
					carte[i][j] = caseCarte['VIOLETE']
				if carte[i][j] == caseCarte['ROUGE']:
					carte[i][j] = caseCarte['ROUGEE']
			j = j - 1
		i = i - 1
	
	positionX, positionY = 0, 0
	for i in range(len(carte)):
		for j in range(len(carte[i])):
			positionX = i * TAILLE_BLOC
			positionY = j * TAILLE_BLOC
			if carte[i][j] == caseCarte['BLEU']:
				spriteCBleu.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCBleu)
			if carte[i][j] == caseCarte['ORANGE']:
				spriteCOrange.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCOrange)
			if carte[i][j] == caseCarte['TURQUOISE']:
				spriteCTurquoise.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCTurquoise)
			if carte[i][j] == caseCarte['JAUNE']:
				spriteCJaune.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCJaune)
			if carte[i][j] == caseCarte['VERT']:
				spriteCVert.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCVert)
			if carte[i][j] == caseCarte['VIOLET']:
				spriteCViolet.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCViolet)
			if carte[i][j] == caseCarte['ROUGE']:
				spriteCRouge.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCRouge)
			if carte[i][j] == caseCarte['GRIS']:
				spriteCGris.SetPosition(positionX, positionY)
				fenetre.Draw(spriteCGris)
			if carte[i][j] == caseCarte['BLEUE']:
				spriteEBleu.SetPosition(positionX, positionY)
				fenetre.Draw(spriteEBleu)
			if carte[i][j] == caseCarte['ORANGEE']:
				spriteEOrange.SetPosition(positionX, positionY)
				fenetre.Draw(spriteEOrange)
			if carte[i][j] == caseCarte['TURQUOISEE']:
				spriteETurquoise.SetPosition(positionX, positionY)
				fenetre.Draw(spriteETurquoise)
			if carte[i][j] == caseCarte['JAUNEE']:
				spriteEJaune.SetPosition(positionX, positionY)
				fenetre.Draw(spriteEJaune)
			if carte[i][j] == caseCarte['VERTE']:
				spriteEVert.SetPosition(positionX, positionY)
				fenetre.Draw(spriteEVert)
			if carte[i][j] == caseCarte['VIOLETE']:
				spriteEViolet.SetPosition(positionX, positionY)
				fenetre.Draw(spriteEViolet)
			if carte[i][j] == caseCarte['ROUGEE']:
				spriteERouge.SetPosition(positionX, positionY)
				fenetre.Draw(spriteERouge)
	fenetre.Display()
	sf.Sleep(1)

def jeu():
	"Déroulement du jeu"
	global spriteCBleu
	global spriteCOrange
	global spriteCTurquoise
	global spriteCJaune
	global spriteCVert
	global spriteCViolet
	global spriteCRouge
	global etatDuJeu
	global carte
	global niveauJoueur
	global pointsJoueur
	global rotationTetromino
	global vitesseDescente
	
	uneLigne, deuxLignes, troisLignes, quatreLignes, prochainNiveau = sf.SoundBuffer(), sf.SoundBuffer(), sf.SoundBuffer(), sf.SoundBuffer(), sf.SoundBuffer()
	uneLigne.LoadFromFile("Données/Sons/1ligne.wav")
	deuxLignes.LoadFromFile("Données/Sons/2ligne.wav")
	troisLignes.LoadFromFile("Données/Sons/3ligne.wav")
	quatreLignes.LoadFromFile("Données/Sons/4ligne.wav")
	prochainNiveau.LoadFromFile("Données/Sons/prochainNiveau.wav")
	sonUneLigne = sf.Sound(uneLigne, False)
	sonDeuxLigne = sf.Sound(deuxLignes, False)
	sonTroisLigne = sf.Sound(troisLignes, False)
	sonQuatreLigne = sf.Sound(quatreLignes, False)
	sonProchainNiveau = sf.Sound(prochainNiveau, False)
	
	musiqueJeu = sf.Music()
	musiqueJeu.OpenFromFile("Données/Musiques/MusiqueClassique.ogg")
	musiqueJeu.SetLoop(True)
	musiqueJeu.Play()
	
	nombreTotalLignes = 0
	
	police = sf.Font()
	police.LoadFromFile("Données/Polices/HandSean.ttf", 20)
	
	horloge = sf.Clock()
	temps = horloge.GetElapsedTime()
	tempsAvant = horloge.GetElapsedTime()
	
	if pointsJoueur > 1:
		chainePoints = str(pointsJoueur) + ' points'
	else:
		chainePoints = str(pointsJoueur) + ' point'
	chaineNiveau = 'niveau ' + str(niveauJoueur)
	if nombreTotalLignes > 1:
		chaineNbrLignes = str(nombreTotalLignes) + ' lignes'
	else:
		chaineNbrLignes = str(nombreTotalLignes) + ' ligne'
	textePoints, texteNiveau, texteLignes = sf.String(chainePoints, police, 20), sf.String(chaineNiveau, police, 20), sf.String(chaineNbrLignes, police, 20)
	textePoints.SetPosition(270, 60)
	texteNiveau.SetPosition(270, 100)
	texteLignes.SetPosition(270, 140)

	chargerCarte(carte)
	
	formeTetromino = randrange(1, 8)
	rotationTetromino = randrange(1, 5)
	prochaineForme = randrange(1, 8)
	prochaineRotation = randrange(1, 5)
	tetrominoDescend = False
	tetrominoCouleurDescend = ''
	c1 = [0, 0]
	c2 = [0, 0]
	c3 = [0, 0]
	c4 = [0, 0]
	posTetromino = [c1, c2, c3, c4]
	nombreLignesASupp = 0
	lignesAEnlver = [-1, -1, -1, -1]
	
	varTemp = None
	
	while etatDuJeu == 'COMMENCE':
		temps = horloge.GetElapsedTime()
		ligne = []
		numeroLigneAEnlever = 0
		while fenetre.GetEvent(evenement):
			if evenement.Type == sf.Event.Closed:
				if menu() == True:
					etatDuJeu = 'PAS_COMMENCE'
					musiqueJeu.Stop()
					musiqueMenu.Play()
			if Input.IsKeyDown(sf.Key.Escape):
				if menu() == True:
					etatDuJeu = 'PAS_COMMENCE'
					musiqueJeu.Stop()
					musiqueMenu.Play()
					sf.Sleep(0.1)
			if evenement.Type == sf.Event.KeyPressed:
				if evenement.Key.Code == sf.Key.Down:
					vitesseDescente = 0.05
			if evenement.Type == sf.Event.KeyReleased:
				if evenement.Key.Code == sf.Key.Down:
					if niveauJoueur == 1:
						vitesseDescente = 1.5
					elif niveauJoueur == 2:
						vitesseDescente = 1.25
					elif niveauJoueur == 3:
						vitesseDescente = .55
					elif niveauJoueur == 4:
						vitesseDescente = .4
					elif niveauJoueur == 5:
						vitesseDescente = .3
					elif niveauJoueur == 6:
						vitesseDescente = .25
					elif niveauJoueur == 7:
						vitesseDescente = .2
					elif niveauJoueur == 8:
						vitesseDescente = .15
					elif niveauJoueur == 9:
						vitesseDescente = .15
					elif niveauJoueur == 10:
						vitesseDescente = .1
			if Input.IsKeyDown(sf.Key.Right):
				if peutBouger(posTetromino, carte, 'droite', formeTetromino, rotationTetromino):
					bougerBlocs(posTetromino, carte, 'droite', formeTetromino)
			if Input.IsKeyDown(sf.Key.Left):
				if peutBouger(posTetromino, carte, 'gauche', formeTetromino, rotationTetromino):
					bougerBlocs(posTetromino, carte, 'gauche', formeTetromino)
		if tetrominoDescend == False:
			compteur = 0
			for i in range(NBR_BLOCS_HAUTEUR):
				ligne = []
				for j in range(NBR_BLOCS_LARGEUR):
					ligne.append(carte[j][i])
					numeroLigneAEnlever = i
				if ligneComplete(ligne):
					lignesAEnlver[compteur] = numeroLigneAEnlever
					nombreLignesASupp = nombreLignesASupp + 1
					nombreTotalLignes = nombreTotalLignes + 1
					if niveauJoueur < 10:
						varTemp = int(floor(nombreTotalLignes / 10) + 1)
						if varTemp > niveauJoueur:
							sonProchainNiveau.Play()
							niveauJoueur = int(floor(nombreTotalLignes / 10) + 1)
							varTemp = None
					else:
						etatDuJeu = 'GAME_OVER'
						musiqueJeu.Stop()
					if niveauJoueur == 1:
						vitesseDescente = 1.5
					elif niveauJoueur == 2:
						vitesseDescente = 1.25
					elif niveauJoueur == 3:
						vitesseDescente = .55
					elif niveauJoueur == 4:
						vitesseDescente = .4
					elif niveauJoueur == 5:
						vitesseDescente = .3
					elif niveauJoueur == 6:
						vitesseDescente = .25
					elif niveauJoueur == 7:
						vitesseDescente = .2
					elif niveauJoueur == 8:
						vitesseDescente = .15
					elif niveauJoueur == 9:
						vitesseDescente = .15
					elif niveauJoueur == 10:
						vitesseDescente = .1
					compteur = compteur + 1
			if nombreLignesASupp == 1:
				lignesAEnlver[1] = -1
				lignesAEnlver[2] = -1
				lignesAEnlver[3] = -1
				numeroLigneAEnlever = lignesAEnlver[0]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				enleveLigne(carte, numeroLigneAEnlever)
				sonUneLigne.Play()
				pointsJoueur = pointsJoueur + 40 * niveauJoueur
			elif nombreLignesASupp == 2:
				lignesAEnlver[2] = -1
				lignesAEnlver[3] = -1
				numeroLigneAEnlever = lignesAEnlver[0]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[1]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[0]
				enleveLigne(carte, numeroLigneAEnlever)
				numeroLigneAEnlever = lignesAEnlver[1]
				enleveLigne(carte, numeroLigneAEnlever)
				sonDeuxLigne.Play()
				pointsJoueur = pointsJoueur + 100 * niveauJoueur
			elif nombreLignesASupp == 3:
				lignesAEnlver[3] = -1
				numeroLigneAEnlever = lignesAEnlver[0]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[1]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[2]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[0]
				enleveLigne(carte, numeroLigneAEnlever)
				numeroLigneAEnlever = lignesAEnlver[1]
				enleveLigne(carte, numeroLigneAEnlever)
				numeroLigneAEnlever = lignesAEnlver[2]
				enleveLigne(carte, numeroLigneAEnlever)
				sonTroisLigne.Play()
				pointsJoueur = pointsJoueur + 300 * niveauJoueur
			elif nombreLignesASupp == 4:
				numeroLigneAEnlever = lignesAEnlver[0]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[1]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[2]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[3]
				eclaireLigne(carte, numeroLigneAEnlever, fenetre)
				numeroLigneAEnlever = lignesAEnlver[0]
				enleveLigne(carte, numeroLigneAEnlever)
				numeroLigneAEnlever = lignesAEnlver[1]
				enleveLigne(carte, numeroLigneAEnlever)
				numeroLigneAEnlever = lignesAEnlver[2]
				enleveLigne(carte, numeroLigneAEnlever)
				numeroLigneAEnlever = lignesAEnlver[3]
				enleveLigne(carte, numeroLigneAEnlever)
				sonQuatreLigne.Play()
				pointsJoueur = pointsJoueur + 1200 * niveauJoueur
			nombreLignesASupp = 0
			if pointsJoueur > 1:
				chainePoints = str(pointsJoueur) + ' points'
			else:
				chainePoints = str(pointsJoueur) + ' point'
			chaineNiveau = 'niveau ' + str(niveauJoueur)
			if nombreTotalLignes > 1:
				chaineNbrLignes = str(nombreTotalLignes) + ' lignes'
			else:
				chaineNbrLignes = str(nombreTotalLignes) + ' ligne'
			textePoints.SetText(chainePoints)
			texteNiveau.SetText(chaineNiveau)
			texteLignes.SetText(chaineNbrLignes)
			formeTetromino = prochaineForme
			rotationTetromino = prochaineRotation
			prochaineForme = randrange(1, 8)
			prochaineRotation = randrange(1, 5)
			if formeTetromino == caseCarte['BLEU']: #j
				if rotationTetromino == 1:
					c1 = [4, 1]
					c2 = [4, 2]
					c3 = [5, 2]
					c4 = [6, 2]
				elif rotationTetromino == 2:
					c1 = [5, 1]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [6, 1]
				elif rotationTetromino == 3:
					c1 = [4, 2]
					c2 = [5, 2]
					c3 = [6, 2]
					c4 = [6, 3]
				elif rotationTetromino == 4:
					c1 = [4, 3]
					c2 = [5, 1]
					c3 = [5, 2]
					c4 = [5, 3]
				tetrominoCouleurDescend = 'BLEU'
			if formeTetromino == caseCarte['ORANGE']: #l
				if rotationTetromino == 1:
					c1 = [4, 2]
					c2 = [5, 2]
					c3 = [6, 1]
					c4 = [6, 2]
				elif rotationTetromino == 2:
					c1 = [5, 1]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [6, 3]
				elif rotationTetromino == 3:
					c1 = [4, 2]
					c2 = [4, 3]
					c3 = [5, 2]
					c4 = [6, 2]
				elif rotationTetromino == 4:
					c1 = [4, 1]
					c2 = [5, 1]
					c3 = [5, 2]
					c4 = [5, 3]
				tetrominoCouleurDescend = 'ORANGE'
			if formeTetromino == caseCarte['TURQUOISE']: #i
				if rotationTetromino == 1:
					c1 = [4, 2]
					c2 = [5, 2]
					c3 = [6, 2]
					c4 = [7, 2]
				elif rotationTetromino == 2:
					c1 = [6, 1]
					c2 = [6, 2]
					c3 = [6, 3]
					c4 = [6, 4]
				elif rotationTetromino == 3:
					c1 = [4, 3]
					c2 = [5, 3]
					c3 = [6, 3]
					c4 = [7, 3]
				elif rotationTetromino == 4:
					c1 = [5, 1]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [5, 4]
				tetrominoCouleurDescend = 'TURQUOISE'
			if formeTetromino == caseCarte['JAUNE']: #o
				c1 = [5, 2]
				c2 = [5, 3]
				c3 = [6, 2]
				c4 = [6, 3]
				tetrominoCouleurDescend = 'JAUNE'
			if formeTetromino == caseCarte['VERT']: #s
				if rotationTetromino == 1:
					c1 = [4, 2]
					c2 = [5, 1]
					c3 = [5, 2]
					c4 = [6, 1]
				elif rotationTetromino == 2:
					c1 = [5, 1]
					c2 = [5, 2]
					c3 = [6, 2]
					c4 = [6, 3]
				elif rotationTetromino == 3:
					c1 = [4, 3]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [6, 2]
				elif rotationTetromino == 4:
					c1 = [4, 1]
					c2 = [4, 2]
					c3 = [5, 2]
					c4 = [5, 3]
				tetrominoCouleurDescend = 'VERT'
			if formeTetromino == caseCarte['VIOLET']: #t
				if rotationTetromino == 1:
					c1 = [4, 2]
					c2 = [5, 1]
					c3 = [5, 2]
					c4 = [6, 2]
				elif rotationTetromino == 2:
					c1 = [5, 1]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [6, 2]
				elif rotationTetromino == 3:
					c1 = [4, 2]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [6, 2]
				elif rotationTetromino == 4:
					c1 = [4, 2]
					c2 = [5, 1]
					c3 = [5, 2]
					c4 = [5, 3]
				tetrominoCouleurDescend = 'VIOLET'
			if formeTetromino == caseCarte['ROUGE']: #z
				if rotationTetromino == 1:
					c1 = [4, 1]
					c2 = [5, 1]
					c3 = [5, 2]
					c4 = [6, 2]
				elif rotationTetromino == 2:
					c1 = [5, 2]
					c2 = [5, 3]
					c3 = [6, 1]
					c4 = [6, 2]
				elif rotationTetromino == 3:
					c1 = [4, 2]
					c2 = [5, 2]
					c3 = [5, 3]
					c4 = [6, 3]
				elif rotationTetromino == 4:
					c1 = [4, 2]
					c2 = [4, 3]
					c3 = [5, 1]
					c4 = [5, 2]
				tetrominoCouleurDescend = 'ROUGE'
			if carte[c1[0]][c1[1]] == caseCarte['VIDE']:
				if carte[c2[0]][c2[1]] == caseCarte['VIDE']:
					if carte[c3[0]][c3[1]] == caseCarte['VIDE']:
						if carte[c4[0]][c4[1]] == caseCarte['VIDE']:
							carte[c1[0]][c1[1]] = caseCarte[tetrominoCouleurDescend]
							carte[c2[0]][c2[1]] = caseCarte[tetrominoCouleurDescend]
							carte[c3[0]][c3[1]] = caseCarte[tetrominoCouleurDescend]
							carte[c4[0]][c4[1]] = caseCarte[tetrominoCouleurDescend]
							posTetromino = [c1, c2, c3, c4]
							tetrominoDescend = True
			if tetrominoDescend == False:
				etatDuJeu = 'GAME_OVER'
				musiqueJeu.Stop()
		else:
			if peutDescendre(posTetromino, carte, formeTetromino, rotationTetromino):
				if temps - tempsAvant > vitesseDescente:
					if formeTetromino == caseCarte['BLEU']: #j
						if rotationTetromino == 1:
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 2:
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 3:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
						elif rotationTetromino == 4:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['BLEU']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
					if formeTetromino == caseCarte['ORANGE']: #l
						if rotationTetromino == 1:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
						elif rotationTetromino == 2:
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 3:
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 4:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['ORANGE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
					if formeTetromino == caseCarte['TURQUOISE']: #i
						if rotationTetromino == 1 or rotationTetromino == 3:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['TURQUOISE']
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['TURQUOISE']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['TURQUOISE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['TURQUOISE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 2 or rotationTetromino == 4:
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['TURQUOISE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
					if formeTetromino == caseCarte['JAUNE']: #o
						carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['JAUNE']
						carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['JAUNE']
						carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
						carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
					if formeTetromino == caseCarte['VERT']: #s
						if rotationTetromino == 1 or rotationTetromino == 3:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['VERT']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['VERT']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['VERT']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 2 or rotationTetromino == 4:
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['VERT']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['VERT']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
					if formeTetromino == caseCarte['VIOLET']: #t
						if rotationTetromino == 1:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 2:
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 3:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 4:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['VIOLET']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
					if formeTetromino == caseCarte['ROUGE']: #z
						if rotationTetromino == 1 or rotationTetromino == 3:
							carte[posTetromino[0][0]][posTetromino[0][1] + 1] = caseCarte['ROUGE']
							carte[posTetromino[2][0]][posTetromino[2][1] + 1] = caseCarte['ROUGE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['ROUGE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[1][0]][posTetromino[1][1]] = caseCarte['VIDE']
							carte[posTetromino[3][0]][posTetromino[3][1]] = caseCarte['VIDE']
						elif rotationTetromino == 2 or rotationTetromino == 4:
							carte[posTetromino[1][0]][posTetromino[1][1] + 1] = caseCarte['ROUGE']
							carte[posTetromino[3][0]][posTetromino[3][1] + 1] = caseCarte['ROUGE']
							carte[posTetromino[0][0]][posTetromino[0][1]] = caseCarte['VIDE']
							carte[posTetromino[2][0]][posTetromino[2][1]] = caseCarte['VIDE']
					tempsAvant = horloge.GetElapsedTime()
					posTetromino = [(posTetromino[0][0], posTetromino[0][1] + 1), (posTetromino[1][0], posTetromino[1][1] + 1), (posTetromino[2][0], posTetromino[2][1] + 1), (posTetromino[3][0], posTetromino[3][1] + 1)]
			else:
				if temps - tempsAvant > 1:
					tetrominoDescend = False
					tempsAvant = horloge.GetElapsedTime()
		fenetre.Clear(sf.Color(0, 0, 0))
		for i in range(len(carte)):
			for j in range(len(carte[i])):
				positionX = i * TAILLE_BLOC
				positionY = j * TAILLE_BLOC
				if carte[i][j] == caseCarte['BLEU']:
					spriteCBleu.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCBleu)
				if carte[i][j] == caseCarte['ORANGE']:
					spriteCOrange.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCOrange)
				if carte[i][j] == caseCarte['TURQUOISE']:
					spriteCTurquoise.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCTurquoise)
				if carte[i][j] == caseCarte['JAUNE']:
					spriteCJaune.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCJaune)
				if carte[i][j] == caseCarte['VERT']:
					spriteCVert.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCVert)
				if carte[i][j] == caseCarte['VIOLET']:
					spriteCViolet.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCViolet)
				if carte[i][j] == caseCarte['ROUGE']:
					spriteCRouge.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCRouge)
				if carte[i][j] == caseCarte['GRIS']:
					spriteCGris.SetPosition(positionX, positionY)
					fenetre.Draw(spriteCGris)
		spritePieceSuiv.SetPosition(LARGEUR_FENETRE - 150 + 150 / 2 - spritePieceSuiv.GetSubRect().GetWidth() / 2, HAUTEUR_FENETRE / 2 - spritePieceSuiv.GetSubRect().GetHeight() / 2)
		fenetre.Draw(spritePieceSuiv)
		afficheProchainTetromino(fenetre, prochaineForme, prochaineRotation)
		fenetre.Draw(textePoints)
		fenetre.Draw(texteNiveau)
		fenetre.Draw(texteLignes)
		fenetre.Display()
		if Input.IsKeyDown(sf.Key.Up):
			rotationForme(posTetromino, carte, formeTetromino)	
			sf.Sleep(0.2)

TAILLE_BLOC = 22
NBR_BLOCS_LARGEUR = 12
NBR_BLOCS_HAUTEUR = 22
LARGEUR_FENETRE = TAILLE_BLOC * NBR_BLOCS_LARGEUR + 150
HAUTEUR_FENETRE = TAILLE_BLOC * NBR_BLOCS_HAUTEUR

niveauJoueur = 1
pointsJoueur = 0
vitesseDescente = 1.5
rotationTetromino = 0

tamponChoix = sf.SoundBuffer()
tamponChoix.LoadFromFile("Données/Sons/choix.wav")
sonChoix = sf.Sound(tamponChoix, False)

carte = []
for i in range(NBR_BLOCS_LARGEUR):
	carte.append(range(NBR_BLOCS_HAUTEUR))

caseCarte = {'VIDE': 0, 'BLEU': 1, 'ORANGE': 2, 'TURQUOISE': 3, 'JAUNE': 4, 'VERT': 5, 'VIOLET': 6, 'ROUGE': 7, 'GRIS': 8, 'BLEUE': 9, 'ORANGEE': 10, 'TURQUOISEE': 11, 'JAUNEE': 12, 'VERTE': 13, 'VIOLETE': 14, 'ROUGEE': 15}
etatJeu = {'PAS_COMMENCE': 'PAS_COMMENCE', 'COMMENCE': 'COMMENCE', 'GAME_OVER': 'GAME_OVER'}
etatDuJeu = 'PAS_COMMENCE'

musiqueMenu = sf.Music()
musiqueMenu.OpenFromFile("Données/Musiques/MusiqueMenu.ogg")
musiqueMenu.SetLoop(True)
musiqueMenu.Play()

largeur = sf.VideoMode(640, 480).GetDesktopMode().Width
hauteur = sf.VideoMode(640, 480).GetDesktopMode().Height
fenetre = sf.RenderWindow(sf.VideoMode(LARGEUR_FENETRE, HAUTEUR_FENETRE), "Tetris", sf.Style.Close)
fenetre.SetPosition(largeur / 2 - fenetre.GetWidth() / 2, hauteur / 2 -fenetre.GetHeight() / 2)

police, police2 = sf.Font(), sf.Font()
police.LoadFromFile("Données/Polices/HandSean.ttf", 50)
police2.LoadFromFile("Données/Polices/HandSean.ttf", 30)
texte = sf.String("Tetris", police, 50)
texte.Move(fenetre.GetWidth() / 2 - texte.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texte.GetRect().GetHeight() / 2)

texteNouveau = sf.String("Nouvelle partie", police2, 30)
texteNouveau.Move(fenetre.GetWidth() / 2 - texteNouveau.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteNouveau.GetRect().GetHeight() / 2 + 140)
texteNouveau.SetColor(sf.Color(255, 0, 0))
texteQuitter = sf.String("Quitter", police2, 30)
texteQuitter.Move(fenetre.GetWidth() / 2 - texteQuitter.GetRect().GetWidth() / 2, fenetre.GetHeight() / 2 - texteQuitter.GetRect().GetHeight() / 2 + 180)

imageLogo = sf.Image()
imageLogo.LoadFromFile("Données/Images/tetris.png")
spriteLogo = sf.Sprite(imageLogo)
spriteLogo.SetPosition(fenetre.GetWidth() / 2 - spriteLogo.GetSubRect().GetWidth() / 2, fenetre.GetHeight() / 2 - spriteLogo.GetSubRect().GetHeight() / 2 - 100)

Input = fenetre.GetInput()
choix = 1	

imageCBleu, imageCOrange, imageCTurquoise, imageCJaune, imageCVert, imageCViolet, imageCRouge, imageEBleu, imageEOrange, imageETurquoise, imageEJaune, imageEVert, imageEViolet, imageERouge, imageCGris, imagePieceSuiv = sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image(), sf.Image()
imageCBleu.LoadFromFile("Données/Images/j.png")
imageCOrange.LoadFromFile("Données/Images/l.png")
imageCTurquoise.LoadFromFile("Données/Images/i.png")
imageCJaune.LoadFromFile("Données/Images/o.png")
imageCVert.LoadFromFile("Données/Images/s.png")
imageCViolet.LoadFromFile("Données/Images/t.png")
imageCRouge.LoadFromFile("Données/Images/z.png")
imageEBleu.LoadFromFile("Données/Images/jE.png")
imageEOrange.LoadFromFile("Données/Images/lE.png")
imageETurquoise.LoadFromFile("Données/Images/iE.png")
imageEJaune.LoadFromFile("Données/Images/oE.png")
imageEVert.LoadFromFile("Données/Images/sE.png")
imageEViolet.LoadFromFile("Données/Images/tE.png")
imageERouge.LoadFromFile("Données/Images/zE.png")
imageCGris.LoadFromFile("Données/Images/tetrion.png")
imagePieceSuiv.LoadFromFile("Données/Images/carre.png")
spriteCBleu, spriteCOrange, spriteCTurquoise, spriteCJaune, spriteCVert, spriteCViolet, spriteCRouge, spriteCGris, spritePieceSuiv, spriteEBleu, spriteEOrange, spriteETurquoise, spriteEJaune, spriteEVert, spriteEViolet, spriteERouge = sf.Sprite(imageCBleu), sf.Sprite(imageCOrange), sf.Sprite(imageCTurquoise), sf.Sprite(imageCJaune), sf.Sprite(imageCVert), sf.Sprite(imageCViolet), sf.Sprite(imageCRouge), sf.Sprite(imageCGris), sf.Sprite(imagePieceSuiv), sf.Sprite(imageEBleu), sf.Sprite(imageEOrange), sf.Sprite(imageETurquoise), sf.Sprite(imageEJaune), sf.Sprite(imageEVert), sf.Sprite(imageEViolet), sf.Sprite(imageERouge)

while fenetre.IsOpened():
	evenement = sf.Event()
	while fenetre.GetEvent(evenement):
		if evenement.Type == sf.Event.Closed:
			fenetre.Close()
		if Input.IsKeyDown(sf.Key.Escape):
			fenetre.Close()
		if Input.IsKeyDown(sf.Key.Up) or Input.IsKeyDown(sf.Key.Down):
			if etatDuJeu == etatJeu['PAS_COMMENCE']:
				sonChoix.Play()
				if choix == 1:
					texteNouveau.SetColor(sf.Color(255, 255, 255))
					texteQuitter.SetColor(sf.Color(255, 0, 0))
					choix = 2
				else:
					texteNouveau.SetColor(sf.Color(255, 0, 0))
					texteQuitter.SetColor(sf.Color(255, 255, 255))
					choix = 1
				sf.Sleep(0.1)
		if Input.IsKeyDown(sf.Key.Return):
			if etatDuJeu == etatJeu['PAS_COMMENCE']:
				sonChoix.Play()
				if choix == 1:
					niveauJoueur = 1
					if niveauJoueur == 1:
						vitesseDescente = 1.5
					elif niveauJoueur == 2:
						vitesseDescente = 1.25
					elif niveauJoueur == 3:
						vitesseDescente = .55
					elif niveauJoueur == 4:
						vitesseDescente = .4
					elif niveauJoueur == 5:
						vitesseDescente = .3
					elif niveauJoueur == 6:
						vitesseDescente = .25
					elif niveauJoueur == 7:
						vitesseDescente = .2
					elif niveauJoueur == 8:
						vitesseDescente = .15
					elif niveauJoueur == 9:
						vitesseDescente = .15
					elif niveauJoueur == 10:
						vitesseDescente = .1
					pointsJoueur = 0
					etatDuJeu = etatJeu['COMMENCE']
					musiqueMenu.Stop()
					jeu()
				elif choix == 2:
					musiqueMenu.Stop()
					fenetre.Close()
			else:
				etatDuJeu = etatJeu['PAS_COMMENCE']
	fenetre.Clear(sf.Color(0, 0, 0))
	if etatDuJeu == etatJeu['PAS_COMMENCE']:
		fenetre.Draw(spriteLogo)
		fenetre.Draw(texte)
		fenetre.Draw(texteNouveau)
		fenetre.Draw(texteQuitter)
	elif etatDuJeu == etatJeu['GAME_OVER']:
		partieTerminee()
	fenetre.Display()
