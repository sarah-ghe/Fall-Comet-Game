import pygame
import random
import animation


# creer une classe qui genere la notion du monstre qui extends animationSprite qui herite sprite
class Monster(animation.AnimateSprite):

	def __init__(self, game):
		super().__init__("mummy")
		self.game = game
		self.health = 50
		self.max_health = 100
		self.attack = 0.3
		self.rect = self.image.get_rect()
		self.rect.x = 1000 + random.randint(0, 300)
		self.rect.y = 540
		self.velocity = random.randint(2, 3)

	def damage(self, amount):
		# infliger les degats
		self.health -= amount

		# verifier si son nouveau nombre de points de vie est <= 0
		if self.health <= 0:
			# reapparaitre comme un nouveau monstre
			self.rect.x = 1000 + random.randint(0, 300)
			self.velocity = random.randint(1, 3)
			self.health = self.max_health

		# si la barre d'evenement est chargée a son max
		if self.game.comet_event.is_full_loaded():
			# retirer
			self.game.all_monster.remove(self)

			# appel a la methoe pour declencher la pluie
			self.game.comet_event.attempt_fall()

	def update_animation(self):
		self.animate()

	def update_health_bar(self, surface):

		# dessiner notre bar de vie
		pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health, 5])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 20, self.health, 5])

	def forward(self):
		# le deplaczement ne ce fait que s'il n y a pas une collision avec un joueur
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity

		else:
			# infliger des degats (au joueur)
			self.game.player.damage(self.attack)
