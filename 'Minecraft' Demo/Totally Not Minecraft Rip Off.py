from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
import time

app = Ursina()

grass_texture = load_texture('Assets/Grass_Block.PNG')
dirt_texture = load_texture('Assets/Dirt_Block.PNG')
stone_texture = load_texture('Assets/Stone_Block.PNG')
hand_texture = load_texture('Assets/Hand.PNG')

blockpick = 1
def update():
    global blockpick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: blockpick = 1
    if held_keys['2']: blockpick = 2
    if held_keys['3']: blockpick = 3
    if held_keys['4']: blockpick = 4


class Voxel(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture,parent=scene):
        super().__init__(
            parent=parent,
            position=position,
            model='Blended_Grass',
            origin_y= 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)), # color.color(hue,saturation,value)
            highlight_color = color.lime,
            scale = 0.5
            )
        print(self.model)
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if blockpick == 1:
                    voxel=Voxel(position = self.position + mouse.normal,texture=grass_texture) #Assign Blocks
                if blockpick == 2:
                    voxel=Voxel(position = self.position + mouse.normal,texture=dirt_texture)
                if blockpick == 3:
                    voxel=Voxel(position = self.position + mouse.normal,texture=stone_texture)
            if key == 'left mouse down':
                destroy(self) #Destroy Blocks

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture = 'sky_sunset',
            scale = 100,
            double_sided = True
            )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='Hand',
            texture=hand_texture,
            scale=Vec3(0.2,0.4,0.2),
            rotation=Vec3(63,-20,0),
            position=Vec2(0.5,-0.42)
        )
    
    def active(self):
        self.rotation=Vec3(83,-20,0)
        self.position = Vec2(0.4,-0.42)

    def passive(self):
        self.rotation=Vec3(63,-20,0)
        self.position = Vec2(0.5,-0.42)

    def update(self):
        if held_keys['q']:
            for z in range(3):
                for x in range(3):
                    for y in range(3):
                        y *= -1
                        if y == 0:
                            voxel = Voxel(position=(x,y,z),texture=grass_texture)
                        else:
                            voxel = Voxel(position=(x,y,z),texture=dirt_texture) 
        else:
            pass

class Human(Button):
    def __init__(self):
        super.__init__(

        )

class invisfloor(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture = 'Assets/Grass_Block.PNG',
            scale = Vec3(10,3,10),
            position = Vec2(0,-10),
            origin_y= 0.5,
        )

class FirstPerson(FirstPersonController):
    def __init__(self):
        super().__init__(

        )

class Healthbar(Entity):
    def __init__(self):
        super().__init__(

        )
            
for z in range(20):
    for x in range(20):
        for y in range(3):
            y *= -1
            if y == 0:
                voxel = Voxel(position=(x,y,z),texture=grass_texture)
            else:
                voxel = Voxel(position=(x,y,z),texture=dirt_texture)



sky = Sky()
hand = Hand()
player = FirstPerson()
Healthbar = Healthbar()
time.sleep(1)
invisiblefloor = invisfloor()

app.run()
