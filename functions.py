import math


def validator(prompt):
    true = True
    while true:
        try:
            value = float(input(prompt))
            true = False
        except:
            print("That is not a valid float please input a float")
    return value

def historyAdding(ap, shape, num, history):
    history_item = ap + " of " + shape + " = " + str(num)    
    history.append(history_item)
    return history
# area functions

def circle_area(r, y):
    return math.pi * r * r

def square_area(x, y):
  return x * x

def rectangle_area(x,y):
  return x * y

def triangle_area(b,h):
  return (0.5 * b) * h

# perimeter functions

def square_perimeter(x, y, z):
  return 4 * x

def rectangle_perimeter(x,y, z):
  return (2 * x) + (2 * y)

def circle_perimeter(r, x, y):
    return 2 * math.pi * r

def triangle_perimeter(s1,s2,s3):
  return s1 + s2 + s3

def area_tool(oneInput, twoInput):
  functions = {
    "square" :square_area,
    "rectangle" : rectangle_area,
    "triangle" : triangle_area,
    "circle" : circle_area
  }
  val = True
  while val: 
    shape = input("What shape do you want to find ")
    if shape in oneInput:
      x = validator("What is the radius or side-length ")
      y = None
      function = functions.get(shape)
      area = function(x, y)
      area = [shape, area]
    elif shape in twoInput:
      x = validator("What is a side-length ")
      y = validator("What is the other side-length ")
      function = functions.get(shape)
      area = function(x, y)
      area = [shape, area]
    elif shape == "end":
      break
    else:
      print("This is a shape that this tool is not designed to deal with")

    #print(history)
    return area

def perimeter_tool(oneInput, twoInputP, threeInput):
  functions = {
    "square" :square_perimeter,
    "rectangle" : rectangle_perimeter,
    "triangle" : triangle_perimeter,
    "circle" : circle_perimeter
  }
  val = True
  while val:
    shape = input("What shape do you want to find ")
    if shape in oneInput:
      x = validator("what is the side length or radius ")
      y = None
      z = None
      z = None
      function = functions.get(shape) 
      perimeter = function(x, y, z)
      perimeter = [shape, perimeter]
    elif shape in twoInputP:
      x = validator("What is the first side length")
      y = validator("What is the second side length")
      z = None
      function = functions.get(shape) 
      perimeter = function(x, y, z)
      perimeter = [shape, perimeter]
    elif shape in threeInput:
      x = validator("What is the first side length ")
      y = validator("What is the second side length ")
      z = validator("What is the third side lenght ")
      function = functions.get(shape)
      perimeter = function(x, y, z)
      perimeter = [shape, perimeter]
    else:
      print("This is a shape that this tool is not designed to deal with")
      
    #print(history)
    return perimeter


def main(history):
  
  oneInput = ["square", "circle"]
  twoInput = ["triangle", "rectangle"]
  twoInputP = ["rectangle"]
  threeInput = ["triangle"]
  area_perimeter = ["area", "perimeter","history","end"]
  ap = input("Do you want to find area or perimeter ")
  true = True
  while true:

    if ap in area_perimeter:
      if ap == "perimeter":
        num = perimeter_tool(oneInput, twoInputP, threeInput)
        shape = num[0]
        num1 = num[1]
        history = historyAdding(ap, shape, num1, history)
        print(history[-1])
      elif ap == "area":
        num = area_tool(oneInput, twoInput)
        shape = num[0]
        num1 = num[1]
        history = historyAdding(ap, shape, num1, history)
        print(history[-1])
      elif ap == "history":
        for i in history:
          print(i)
      elif ap == "end":
        history = "end"
    else:
      break
    
    return history