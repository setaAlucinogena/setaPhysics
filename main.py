from ursina import *
from  physic_object import *

app = Ursina()

po = PhysicalObject(position = (0,0,0),model = "cube", phyisics_type=PhysicsType.MOBILE,scale = 1)


EditorCamera()
app.run()