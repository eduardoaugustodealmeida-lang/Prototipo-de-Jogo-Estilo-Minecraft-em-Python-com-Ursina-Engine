from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

player = FirstPersonController()
sky = Sky()

box = []
for i in range(20):
    for j in range(20):
        box = Button(parent=scene, model='cube', color=color.green, scale=(2,2,2), position=(i,0,j))
    boxes = []
    boxes.append(box)

def input(key):
    if box in boxes:
        if key == 'left mouse down':
            new_box = Button(parent=scene, model='cube', color=color.gray, scale=(2,2,2), position=(player.position + player.forward))
            boxes.append(new_box)
        if key == 'right mouse down':
            hit_info = raycast(player.position, player.forward, distance=5)
            if hit_info.hit:
                boxes.remove(hit_info.entity)
                destroy(hit_info.entity)
        

app.run()