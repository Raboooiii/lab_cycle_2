class ThreeDshapes:
    def Printvolume(self):
        pass
    def Printarea(self):
        pass

class Sphere(ThreeDshapes):
    def __init__(self,radius):
        self.Radius=radius
    def Printarea(self):
        area=4*3.14*self.Radius**2
        return area
    def Printvolume(self):
        vol=round(((4/3)*3.14*self.Radius**3),2)
        return vol
    
class Cylinder(ThreeDshapes):
    def __init__(self,radius,hight):
        self.Radius=radius
        self.Hight=hight
    def Printarea(self):
        area=2*3.14*self.Radius*(self.Radius+self.Hight)
        return area
    def Printvolume(self):
        vol=3.14*self.Hight*(self.Radius**2)
        return vol
SP=Sphere(6)
print("===============SPHERE=================")
print("Area :", SP.Printarea())
print("Volume :",SP.Printvolume())

CY=Cylinder(6,10)
print("===============CYLINDER================")
print("Area :", CY.Printarea())
print("Volume :",CY.Printvolume())