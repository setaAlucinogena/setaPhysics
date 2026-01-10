from ursina import *
from  physic_object import *

app = Ursina()

po = PhysicalObject(position = (0,0,0), mass = 5,model = "cube", phyisics_type=PhysicsType.MOBILE,scale = 1)
ground = PhysicalObject(position = (0,-2,0), model = "cube", phyisics_type=PhysicsType.INAMOBIBLE,scale = (10,.5,10))


def input(key):
    if key == "j":

        po.movement_vector[1] += 10

#def update():
#    po.position+=po.left*time.dt*3*held_keys["a"]

EditorCamera()
app.run()