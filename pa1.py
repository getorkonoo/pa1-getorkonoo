# Programmer: Genevieve Torkornoo
# Course: CS151, Prof. Franceschi
# Date: 09/21/21
# Programming Assignment: 1
# Program Inputs: length, width, height
length = input("enter the length of your wall in ft >")
width = input("enter the width of your wall in ft >")
height = input("enter the height of your wall in ft >")
# convert
length = int(length)
width = int(width)
height = int(height)
# length*height*2 and width*height*2 add them together
side = length*height*2
side2 = width*height*2
totalAmount = side+side2
primer = totalAmount/200
paint = totalAmount/350
# Program Outputs: the total area to be painted
print("the total area painted is",totalAmount)
print("total amount of primer need is",primer)
print("total amount of paint gallons needed is %.0f"% paint)