from ursina import *

from enum import Enum

class PhysicsType(Enum):
    IGNORE = 0
    INAMOBIBLE = 1
    MOBILE = 2

class PhysicalObject(Entity):
    gravity = True
    gravity_vector = Vec3(0,-9.8,0)

    def __init__(self, position, model, phyisics_type, scale):
        super().__init__(
            position = position,
            scale = scale,
            model = model,
            collider = 'box'#rn the collider will be a box regardless of the shape of the model
            )

        #
        self.alpha = .5
        #

        self.physics_type = phyisics_type
        self.grounded = True
        self.movement_vector = Vec3(0,0,0)

    def update(self):
        if self.physics_type == PhysicsType.MOBILE:
            self.position = self.movement_vector*time.dt
            if PhysicalObject.gravity:
                raycast(self.position, PhysicalObject.gravity_vector.normalized(), ignore=(self,), distance=(self.scale[
                    int(abs(PhysicalObject.gravity_vector.normalized()[0])*0)+
                    int(abs(PhysicalObject.gravity_vector.normalized()[1]))+
                    int(abs(PhysicalObject.gravity_vector.normalized()[2])*2)
                    ]/2), debug=True)




        elif self.phyisics_type == PhysicsType.INAMOBIBLE:
            pass
