class Circle():

    def radius(self,radius):
        r = radius
    def center(self,center):
        o = center
    def area(self,r):
        area = 3.142*r*r
        print("Area of the circle is: ",area)
    def peri(self,r):
        peri = 2*3.14*r
        print("Perimeter of the circle is: ",peri)

c = Circle()
radius = int(input("Enter the radius of circle: "))
center = int(input("Enter the center of circle: "))
c.area(radius)
c.peri(radius)