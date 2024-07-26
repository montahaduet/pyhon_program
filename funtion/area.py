
def area_fun(shape):
   

    if shape=='circle':
        print("enter the radius")
        r=float(input("radius="))
        cirle_area=3.1416*r*r
        print("circle area is : "+str(cirle_area))
    elif shape=='rectangle':
        print("enter the height and width :")
        height=float(input("height="))
        width=float(input("width="))
        rectangle_area=height*width
        print("rectangle area is: "+str(rectangle_area))
    else:
        print("nothing")

shape=input() 
area_fun(shape)         

        
