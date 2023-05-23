class Sphere():
    def __init__(self, radius=1, coordx=0, coordy=0, coordz=0):
        self.radius = radius
        self.coordx = coordx
        self.coordy = coordy
        self.coordz = coordz
    def get_volume(self):
        volume = 4/3 * 3.14 * self.radius*self.radius*self.radius
        return volume
    def get_square(self):
        square = 4 * 3.14 * self.radius()*self.radius()
        return square
    def get_radius(self):
        return self.radius
    def get_center(self):
        return tuple([self.coordx, self.coordy, self.coordz])
    def set_radius(self, radius = 1):
        self.radius = radius
        return 0
    def set_center(self, coordx=0, coordy=0, coordz=0):
        self.coordx = coordx
        self.coordy = coordy
        self.coordz = coordz
        return 0
    def is_point_inside(self, coordx, coordy, coordz):
        if(-self.coordx-self.radius<coordx<self.coordx+self.radius)\
                and(-self.coordy-self.radius<coordy<self.coordy+self.radius)\
                and(-self.coordz-self.radius <= coordz <= self.coordz+self.radius):
            return True
        return False

s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print(s0.get_volume()) # 0.523598775598
print(s0.is_point_inside(0 , -1.5, 0)) # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6
