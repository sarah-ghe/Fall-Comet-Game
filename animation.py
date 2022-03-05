import pygame


# def une calsse qui se charge des animations
class AnimateSprite(pygame.sprite.Sprite):

	# def les choses a faire a la creation de l'entité
	def __init__(self, sprite_name):
		super().__init__()
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.current_image = 0  # commencer l'anoim a l'img 0
		self.images = animations.get(sprite_name)
		self.animation = False

	# def une methode ppur demarrer l'animation
	def start_animation(self):
		self.animation = True

	# definir une methode pour animer le sprite
	def animate(self):

		# verifier si l'anim est active
		if self.animation:

			# passer a l'image suivante
			self.current_image += 1

			# verifier si on a atteint la fin de l'animation
			if self.current_image >= len(self.images):
				# remettre l'anim au depart
				self.current_image = 0
				# desactivation de l'ani
				self.animation = False

			# modifier l'image precedente par la suivante
			self.image = self.images[self.current_image]


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
	# charger les 24 images de ce sprite dans le dossier correspondant
	images = []
	# recuperer le chemein du dossier des assets
	path = f'assets/{sprite_name}/{sprite_name}'

	# boucler sur chaque image dans ce dossier
	for num in range(1, 24):
		image_path = path + str(num) + '.png'
		images.append(pygame.image.load(image_path))  # charger les 24 images dans la liste images pour tout le jeu

	# renvoyer le contenu de liste
	return images


# definir un dictionnaire qui contient les images chargées de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
animations = {
	'mummy': load_animation_images('mummy'),
	'player': load_animation_images('player')
}
