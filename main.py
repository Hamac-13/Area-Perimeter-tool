from functions import validator, area_main, circle_area, perimeter_4_sided, circle_perimeter


true = True
fourSided = ["square","rectangle","parallelogram"]
threeSided = ["triangle"]
circle = ["circle"]

area_perimeter = ["area","perimeter"]
while true:
    ap = input("Do you want to find area or perimeter? ")
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
          area = area_main(shape,x,y)
          print(area)
      elif ap == "perimeter":
        shape = input("What shape ")
        if shape in fourSided:
          if shape =="square":
            x= validator("x ")
            y = None
            perimeter = perimeter_4_sided("square",x, y)
            print(perimeter)
          perimeter = perimeter_4_sided(shape,x,y)
        elif shape in threeSided:
          print("3")
        elif shape in circle:
          r = validator("Radius ")
          perimeter = circle_perimeter(r)
          print(perimeter)
        
    else:
      print("no")
      true = False 
