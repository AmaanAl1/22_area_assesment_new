#Menu that displays all the options
def menu():
    print("[1] rectangle",
          "[2] square",
          "[3] circle",
          "[4] triangle",
          "[5] calculation history")

#asks the user to input what option they want
menu()
option = int(input("enter your option: "))

#history of all the calculations are outputted in this line of code
history = []

while option != 0:
    #code to calculate the area and perimeter of a rectangle
    if option == 1:
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        answer = length * width
        answer = 2 * (length * width)
        print("Area of rectangle = ", answer)
        print("Perimeter of rectangle = ", answer)
    # code to calculate the area and perimeter of a square
    elif option == 2:
        square_side = float(input("Side of square : "))
        answer = square_side * square_side
        answer = 4 * square_side
        print("Area of square : ",answer)
        print("Perimeter of square : ",answer)
    # code to calculate the area and perimeter of a circle
    elif option == 3:
        radius = float(input("Input Radius : "))
        answer = 3.14 * radius * radius
        answer = 2 * 3.14 * radius
        print("Area of Circle: ",answer)
        print("Perimeter of Circle: ",answer)
    # code to calculate the area and perimeter of a triangle
    elif option == 4:
        base = float(input("Length of triangle : "))
        height = float(input("Height of triangle : "))
        answer = 0.5 * base * height
        a = float(input("Side 1 : "))
        b = float(input("Side 2 : "))
        c = float(input("Side 3 : "))
        answer = a + b + c
        print("Area of Triangle : ", answer)
        print("Perimeter of Triangle : ",answer)
    #will display the history of calculations and exits the program.
    elif option == 5:
        print(history)
        break
    else:
        print("invalid option")

    history.append(answer)
    #runs the code again
    menu()
    option = int(input("enter your option: "))
