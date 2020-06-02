import math
def validator(prompt):
    true = True
    while true:
        try:
            value = float(input(prompt))
            true = False
        except:
            print("That is not a valid int please input an integer")
    return value

def area_main(shape, x, y):
  
  if shape == "square":
    return x * y
  
  elif shape == "triangle":
    area = 0.5 * x
    return area * y
  elif shape == "rectangle":
    return x * y
  elif shape == "parallelogram":
    return x * y

def circle_area(r):
  return math.pi * r * r
def circle_perimeter(r):
  return 2 * math.pi * r
def perimeter_3_sided(x,y,z):
  return x + y + z

def perimeter_4_sided(shape,x,y):
  if shape == "square":
    return 4 * x
  elif shape == "rectangle":
    return (2 * x) + (2 * y)
  elif shape == "parallelogram":
    return (2 * x) + (2 * y)