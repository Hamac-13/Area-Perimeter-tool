from functions import validator, area_main, circle_area, perimeter_4_sided, circle_perimeter, perimeter_3_sided

true = True
fourSided = ["square", "rectangle", "parallelogram"]
threeSided = ["triangle"]
circle = ["circle"]
history = []
area_perimeter = ["area", "perimeter"]
while true:
    ap = input("Do you want to find area or perimeter, or access history ")
    if ap in area_perimeter:
        if ap == "area":
            shape = input("What shape ")

            if shape == "circle":
                r = validator("What is the radius of the circle ")
                area = circle_area(r)
                print(area)

            else:
                x = validator("What is the width of the shape ")
                y = validator("What is the height of the shape ")
                area = area_main(shape, x, y)
                print(area)

            history_item = ap + " of " + shape + " = " + str(area)    
            history.append(history_item)
        elif ap == "perimeter":
            shape = input("What shape ")
            if shape in fourSided:
                if shape == "square":
                    x = validator("x ")
                    y = None
                    perimeter = perimeter_4_sided("square", x, y)
                    print(perimeter)
                perimeter = perimeter_4_sided(shape, x, y)
                print(perimeter)
            elif shape in threeSided:
                side1 = validator("side length 1 ")
                side2 = validator("side length 2 ")
                side3 = validator("side length 3 ")
                perimeter = perimeter_3_sided(side1, side2, side3)
                print(perimeter)
            elif shape in circle:
                r = validator("Radius ")
                perimeter = circle_perimeter(r)
                print(perimeter)
            history_item = ap + " of " + shape + " = " + str(perimeter)
            history.append(history_item)
    elif ap == "history":
        for i in history:
          print(i)

    else:
        print("no. goodbye!")
        true = False
