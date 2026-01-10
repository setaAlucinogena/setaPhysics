from ursina import *

from enum import Enum

class PhysicsType(Enum):
    IGNORE = 0
    INAMOBIBLE = 1
    MOBILE = 2

class PhysicalObject(Entity):
    gravity = True
    gravity_vector = Vec3(0,-9.81,0)
    #should I include a parameter for the terminal velocity to avoid clipping??


    def __init__(self, position, model, phyisics_type, scale, mass = -1):
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

        self.mass = mass
        if self.physics_type == PhysicsType.INAMOBIBLE:
            self.mass = -1 #gotta look up how to get the biggest number in python, while I dont do it, -1 will do as a rather symbolic value

    def getFallDirection(self):
        return (
            int(abs(PhysicalObject.gravity_vector.normalized()[0])*0)+
                    int(abs(PhysicalObject.gravity_vector.normalized()[1]))+
                    int(abs(PhysicalObject.gravity_vector.normalized()[2])*2)
            )


    #puts grounded to True, meaning that the object is apoyado in something stable. 
    #also, if there's still movement applied by the gravity in the movement vector, then it = 0.
    def land(self):
        print("land")
        self.grounded = True

        #self.y+=.1
        #self.movement_vector[1] = 0
        #self.grounded = True
        if self.movement_vector[self.getFallDirection()]:
            tmp1 = self.gravity_vector[self.getFallDirection()]
            tmp2 = self.movement_vector[self.getFallDirection()]
            if abs(tmp1) != tmp1: #if gravity drags you to the negative direction of the axis: (eg: "regular" gravity always drags you to -y)
                if tmp2 < 0:
                    self.movement_vector[self.getFallDirection()] = 0
            elif abs(tmp1) == tmp1: #if gravity drags you to the positive direction of the axis:
                if tmp2 > 0:
                    self.movement_vector[self.getFallDirection()] = 0

        self.position[self.getFallDirection()] = self.ground_ray.world_point[self.getFallDirection()]+.1
        

    def fall(self):
        self.grounded = False
        self.movement_vector += PhysicalObject.gravity_vector

    def update(self):
        if self.physics_type == PhysicsType.MOBILE:
            self.position += self.movement_vector*time.dt
            if PhysicalObject.gravity:
                self.ground_ray = raycast(self.position, PhysicalObject.gravity_vector.normalized(), ignore=(self,), 
                                          distance=((self.scale[self.getFallDirection()]/2)+1), debug=True)

                if self.ground_ray.hit:
                    
                    if not self.grounded:
                        self.land()
                else:
                    
                    self.fall()

                #if self.ground_ray.hit:
                #    for entity in self.ground_ray.entities:
                #        if (entity.physics_type == PhysicsType.INAMOBIBLE or
                #            entity.physics_type == PhysicsType.MOBILE
                #            ):
                #            if entity.grounded:#si lo q toca esta recolzant-se en algo:
                #                self.land()

                #if not self.grounded:
                #    self.fall()





        elif self.physics_type == PhysicsType.INAMOBIBLE:
            pass
