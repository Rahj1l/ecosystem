# ecosystem

Hey guys,  
I'm currently working on this project where I'm trying to simulate an ecosystem. Right now it's super basic — I just have a big flat ground, a male and a female rabbit loaded in 3D, and a predator that you can control using WASD keys. Nothing is alive yet, no AI, no reproduction, no hunting — but that’s all coming soon (hopefully).

This is more of a sandbox setup right now, mostly just to get used to using **Ursina Engine**, and figure out how to make simple 3D stuff work without going into full-blown game dev.

## How to Run

First, install Ursina:

```bash
pip install ursina
```

Then make sure these files are in the same directory as the script:

Female_rabbit.obj

female_color.jpg

Male_rabbit.obj

male_color.jpg

Preditor.obj (I know, spelling — I'll fix that later)

Now just run:
```
python your_script_name.py

Controls
W — Move predator forward

A — Move left

S — Move back

D — Move right

What's Working
Ground

Male and female rabbit entities with separate models and textures

Player-controlled predator that moves with WASD

Skybox and camera positioning

What's Next (in my head)
Basic AI for animals to wander

Reproduction if a male and female are close for long enough

Hunger, energy, death

Maybe random terrain with trees or grass

Food sources

That's all for now. It's fun and relaxing to build, and Ursina makes it way easier than I expected.