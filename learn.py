from ursina import *

app = Ursina()

# Basic floor
ground = Entity(model='plane', scale=100, texture='white_cube', texture_scale=(100,100), collider='box')

player = Entity(
    model='Female_rabbit.obj',  # Ensure the model is in the directory
    texture='female_color.jpg',  # Use your texture file here
    scale=0.1,
    rotation_y=310,
    position=(0,0.5,0),
    collider='box'
)

male = Entity(
    model='Male_rabbit.obj',  # Ensure the model is in the directory
    texture='male_color.jpg',  # Use your texture file here
    scale=0.05,
    position=(0,1,1),
    collider='box'
)

preditor = Entity(
    model='Preditor.obj',  # Ensure the model is in the directory
    texture='male_color.jpg',  # Use your texture file here
    scale=0.05,
    rotation_z=90,
    position=(0,1,0),
    collider='box'
)


# A sky
Sky()

# Simple camera control
camera.position = (0, 10, -20)
camera.rotation_x = 30

# Movement logic
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
