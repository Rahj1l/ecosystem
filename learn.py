from ursina import *

app = Ursina()

# Basic floor
ground = Entity(model='plane', scale=100, texture='white_cube', texture_scale=(100,100), collider='box')

# ----------- Classes -----------

class Rabbit(Entity):
    def __init__(self, model_file, texture_file, position=(0,0.5,0), scale=0.1, **kwargs):
        super().__init__(
            model=model_file,
            texture=texture_file,
            scale=scale,
            position=position,
            collider='box',
            **kwargs
        )


class FemaleRabbit(Rabbit):
    def __init__(self, position=(0,0.5,0)):
        super().__init__(
            model_file='Female_rabbit.obj',
            texture_file='female_color.jpg',
            position=position,
            scale=0.1,
            rotation_y=310
        )


class MaleRabbit(Rabbit):
    def __init__(self, position=(0,1,1)):
        super().__init__(
            model_file='Male_rabbit.obj',
            texture_file='male_color.jpg',
            position=position,
            scale=0.05
        )


class Predator(Entity):
    def __init__(self, position=(0,1,0)):
        super().__init__(
            model='Preditor.obj',
            texture='male_color.jpg',
            scale=0.05,
            position=position,
            rotation_z=90,
            collider='box'
        )

# ----------- Instances -----------

female = FemaleRabbit(position=(0, 0.5, 0))
male = MaleRabbit(position=(0, 1, 1))
player = Predator(position=(0, 1, 0))

# ----------- Environment -----------

Sky()

camera.position = (0, 10, -20)
camera.rotation_x = 30

# ----------- Movement Logic -----------

def update():
    speed = 5 * time.dt
    if held_keys['w']:
        player.z += speed
    if held_keys['s']:
        player.z -= speed
    if held_keys['a']:
        player.x -= speed
    if held_keys['d']:
        player.x += speed

app.run()
