def area_of_circle(r):
    return pi*r*r
def circum_of_circle(r):
    return 2*pi*r

r=int(input("enter the radius"))
pi=3.14
area=area_of_circle(r)
circum=circum_of_circle(r)
print(f"area of circle is {area}")
print(f"circumference of circle is {circum}")
