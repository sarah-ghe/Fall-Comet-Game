import pygame
import random


#creer une classe pour generer la comete
class Comet(pygame.sprite.Sprite):

	def __init__(self, comet_event):
		super().__init__()
		#definir l'image associée a cette comette
		self.image = pygame.image.load('assets/comet.png')
		self.rect = self.image.get_rect()
		self.velocity = random.randint(2, 4)
		self.rect.x = random.randint(20, 800)
		self.rect.y = - random.randint(0, 800)
		self.comet_event = comet_event

	def remove(self):
		self.comet_event.all_comets.remove(self)

		# verifier si l nb de moetes est 0
		if len(self.comet_event.all_comets) == 0:
			#remettre la barre a 0
			self.comet_event.reset_percent()
			#apparaitre les 3 premiers monstres
			self.comet_event.game.spawn_monster()
			self.comet_event.game.spawn_monster()
			self.comet_event.game.spawn_monster()

	def fall(self):
		self.rect.y += self.velocity

		# ne tombe pas sur le sol
		if self.rect.y >= 500:
			print("sol")
			self.remove()

		# s'il n ya plus de comet
		if len(self.comet_event.all_comets) == 0:
			print("la pluie est finie")
			self.comet_event.reset_percent()
			self.comet_event.fall_mode = False

		# verifier si la boule de feu touche le joueur
		if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
			print("joueur touché")
			self.remove()
			# subir 20 pts de degats
			self.comet_event.game.player.damage(20)