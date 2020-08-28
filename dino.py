class Body():
	
	def __init__(self, x_pos, y_pos, width, height, *args):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height

		for costume in args:
			self.costumes.append(costume)

		self.x_velocity = 0
		self.y_velocity = 0

	def get_x_pos(self):
		return self.x_pos

	def get_y_pos(self):
		return self.y_pos

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def set_x_pos(self, x_pos):
		self.x_pos = x_pos

	def set_y_pos(self, y_pos):
		self.y_pos = y_pos			

	def costumes(self, current_time):
		if current_time - self.prev_costume_time > self.costume_tick:
			if self.current_costume != len(self.current_costume) - 1
				self.current_costume += 1
			else:
				self.current_costume = 0

		self.prev_costume_time = current_time

	def update(self, screen):
		self.y_pos += self.y_velocity

		screen.blit(self.costumes[self.current_costume], (self.x_pos, self.y_pos))



class Dino():
	
	def __init__(self, x_pos, y_pos, width, height, gravity, jump_force, *args):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.gravity = gravity
		self.jump_force = jump_force

		for costume in args:
			self.costumes.append(costume)

		self.y_velocity = 0
		self.collision = False

	def get_x_pos(self):
		return self.x_pos

	def get_y_pos(self):
		return self.y_pos

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def set_y_pos(self, y_pos):
		self.y_pos = y_pos

	def jump(self):
		self.y_velocity = self.jump_force

	def gravity(self):
		self.y_velocity += self.gravity

	def detect_collision(self, *args):
		self.collision = False
		for body in args:
			if type(body).__name__ == Ground:
				if self.y_pos >= body.get_y_pos():
					self.y_velocity = 0
				else:
					self.y_velocity += self.gravity
			else:
				if self.x_pos + self.width > body.get_x_pos() > self.x_pos:
					if self.y_pos + self.height > body.get_y_pos() > self.y_pos:
						collision == True
						break
					elif body.get_y_pos() + body.get_height() > self.y_pos > body.get_y_pos():
						collision == True
						break
				elif body.get_x_pos() < self.x_pos < body.get_x_pos() + body.get_width():
					if self.y_pos + self.height > body.get_y_pos() > self.y_pos:
						collision == True
						break
					elif body.get_y_pos() + body.get_height() > self.y_pos > body.get_y_pos():
						collision == True
						break

		return collision

	def costumes(self, screen, current_time):
		if current_time - self.prev_costume_time > self.costume_tick:
			if self.current_costume != len(self.current_costume) - 1
				self.current_costume += 1
			else:
				self.current_costume = 0

		self.prev_costume_time = current_time
		screen.blit(self.costumes[self.current_costume], (self.x_pos, self.y_pos))

	def update(self, screen, current_time, *args):
		self.y_pos += self.y_velocity
		
		if self.detect_collision(args) == True:
			self.die()

		self.costumes(screen, current_time)
