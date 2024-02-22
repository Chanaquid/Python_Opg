import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            print(f"The area is {(0.5*base * height):.6f}")
            
        elif shape == "rectangle":
            length = float(input("Give length of the rectangle: "))
            width = float(input("Give width of the rectangle: "))
            print(f"The area is {(length * width):.6f}")
        
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            print(f"The area is {(math.pi*radius**2):.6f}")
        
        elif shape == "":
            break
        
        else:
            print("Unknown shape!")

# def triangle(base, height):
#     return 0.5*base * height
# def rectangle(length, width):
#     return length * width
# def circle(radius):
#     return math.pi*radius**2

if __name__ == "__main__":
    main()
