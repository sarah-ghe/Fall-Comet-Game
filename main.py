import pygame
import math
from Game import Game
from Player import Player

pygame.init()

# generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# l'arriere plan en 3 steps: charger l'image, injecter l'image sur l'ecran, mettre a jour set ecran
background = pygame.image.load('assets/bg.jpg')

#importer notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#importer le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

# charger le jeu
game = Game()

# charger notre joueur
player = Player(game)

running = True

# boucle tq cette cond est vraie
while running:

	# appliquer le bg
	screen.blit((background), (0, -200))

	#verifier si le jeu a commencé ou non
	if game.is_playing:
		#declencher les instructions de la partie
		game.update(screen)

	#verifier si le jeu n'a pas commencé
	else:
		#ajouter l'ecran de bienvenue
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, banner_rect)



	# mettre à jour l'ecran
	pygame.display.flip()

	# si le joueur ferme cette fenetre
	for event in pygame.event.get():
		# que l'event est fermeture de fenetre
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			print("Fermeture du jeu")
		# detecter si un joueur lache une touche du clavier
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			#detecter si la touche espace est enclenchée pour lancer la projectile
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()

		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			#verifier si la souris est en collision avec le bouton play
			if play_button_rect.collidepoint(event.pos):
				#mettre le jeu en mode lancé
				game.start()
