import pygame
from comet import Comet


# creer une classe pour generer cet event
class CometFallEvent:
	# lors du chargement -> creer un compteur
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 10
		self.game = game
		self.fall_mode = False

		# def un groupe de sprite pour stocker les comettes
		self.all_comets = pygame.sprite.Group()

	def add_percent(self):
		self.percent += self.percent_speed / 100

	def is_full_loaded(self):
		return self.percent >= 100

	def reset_percent(self):
		self.percent = 0

	def meteor_fall(self):
		#boucle pour la vals entre 0 et 10
		for i in range(1, 15):
			# apparaitre les boules de feu
			self.all_comets.add(Comet(self))

	def attempt_fall(self):
		if self.is_full_loaded() and len(self.game.all_monster) == 0:
			print("Pluie de cometes !")
			self.meteor_fall()
			self.fall_mode = True

	def update_bar(self, surface):
		# ajouter du poucentage a la barre
		self.add_percent()

		# barre noire sur l'arriere plan
		pygame.draw.rect(surface, (0, 0, 0), [
			0,
			surface.get_height() - 25,
			surface.get_width(),
			10
		])

		# barre rouge (jauge d'evenement)
		pygame.draw.rect(surface, (187, 11, 11), [
			0,
			surface.get_height() - 25,
			(surface.get_width() / 100) * self.percent,
			10
		])
