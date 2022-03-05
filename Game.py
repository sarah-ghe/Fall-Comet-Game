import pygame
from Player import Player
from Monster import Monster
from comet_event import CometFallEvent


#creer une 2eme classe qui represente le jeu
class Game:

	def __init__(self):
		#definir si le jeu a commencé ou non
		self.is_playing = False
		# generer le joueur
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		#generer l'event
		self.comet_event = CometFallEvent(self)
		#groupe de monstre
		self.all_monster = pygame.sprite.Group()
		self.pressed = {}


	def start(self):
		self.is_playing = True
		self.spawn_monster()
		self.spawn_monster()

	def game_over(self):
		#remettre le jeu a neuf, retirer les monstres, remettre le joueur à 100 de vie, jeu en attente
		self.all_monster = pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.reset_percent()
		self.is_playing = False

	def update(self, screen):
		# appliquer l'image du joueur
		screen.blit(self.player.image, self.player.rect)

		# actualiser la barre de vie du joueur
		self.player.update_health_bar(screen)

		#actualiser la barre d'event
		self.comet_event.update_bar(screen)

		# actualiser l'animation du joueur
		self.player.update_animation()

		# recuperer les projectiles du joueur
		for projectile in self.player.all_projectiles:
			projectile.move()

		# recuperer les monstres
		for monster in self.all_monster:
			monster.forward()
			monster.update_health_bar(screen)
			monster.update_animation()

		#recuperer les cometes du jeu
		for comet in self.comet_event.all_comets:
			comet.fall()

		# appliquer l'ensemble des images du groupe de projectiles, draw prend tous les projectiles du groupe et les dessine sur l'ecran
		self.player.all_projectiles.draw(screen)

		# appliquer l'ensemble des images du groupe de monstres
		self.all_monster.draw(screen)

		# appliquer l'ensemble des images du groupe de cometes
		self.comet_event.all_comets.draw(screen)

		# vérifier si le joueur souhaite aller à gauche ou à droite
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()

	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	def spawn_monster(self):
		monster = Monster(self)
		self.all_monster.add(monster)