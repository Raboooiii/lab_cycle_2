class Box:
    def __init__(self,length,breadth=None,height=None):
        self.Length=length
        self.Breadth=breadth
        self.Height=height
        if breadth is None and height is None:
            self.Breadth=length
            self.Height=length
        elif height is None:
            self.Height=length
    
    def Area(self):
        area=2*(self.Length*self.Breadth+self.Breadth*self.Height+self.Length*self.Height)
        return area
    
    def volume(self):
        vol=self.Length*self.Breadth*self.Height
        return vol
    
cube=Box(5)
sq_prism=Box(5,4)
rect_prism=Box(5,4,3)
print("===========CUBE===========")
print("Area :", cube.Area())
print("Volume :",cube.volume())
print("===========SQUARE PRISM============")
print("Area :", sq_prism.Area())
print("Volume :",sq_prism.volume())
print("=========RECTANGULAR PRISM============")
print("Area:",rect_prism.Area())
print("Volume:",rect_prism.volume())