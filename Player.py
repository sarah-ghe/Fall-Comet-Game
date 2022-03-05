import pygame
from projectile import Projectile
import animation

#creer la 1ere classe qui represente le joueur
class Player(animation.AnimateSprite):

	def __init__(self, game):
		super().__init__('player')
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 10
		self.velocity = 6
		self.all_projectiles = pygame.sprite.Group()
		self.rect = self.image.get_rect()
		self.rect.x = 450
		self.rect.y = 500

	def damage(self, amount):
		#infliger les degats
		if self.health - amount > amount:
			self.health -= amount
		else:
			#si le joueur n'a plus de points de vie
			self.game.game_over()

	def update_animation(self):
		self.animate()

	def update_health_bar(self, surface):

		#dessiner notre bar de vie
		pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

	def launch_projectile(self):
		#creer une nouvelle instance de la classe Projectile
		self.all_projectiles.add(Projectile(self))
		# demarrer l'anim
		self.start_animation()

	def move_right(self):
		#si le joueur n'est pas en collision avec un monstre present dans le groupe all monsters
		if not self.game.check_collision(self, self.game.all_monster):
			self.rect.x +=self.velocity

	def move_left(self):
		self.rect.x -=self.velocity