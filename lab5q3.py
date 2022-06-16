class Circle:
    pi: float = 3.14
    
    def __init__(self, r) -> None:
        self.r = r
    
    def get_perimeter(self):
        return 2 * Circle.pi * self.r
    
    def get_area(self):
        return Circle.pi * self.r * self.r

