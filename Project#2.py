# Project#2
# Name: Destinee Monroe
# Class Section: CSC105-01
# Purpose: The purpose of this lab is to learn how to execute more elaborate
# programs in Python. The purpose is also to learn how to use more functions
# in Python.
# Date: 3/1/2014

def convertFahToCel(x):
    y = x.split(',')                    
    print ('Fahrenheit'+'\t'+'Celsius') 
    for item in y:
        celsius = (eval(item) - 32)*5/9
        print (str(item)+'\t\t'+("%.1f" % celsius))

# 'item' can also be called 'i'. It is a built in function in Python.
# 'x.split' is splits a string and turns it into a list.
# 'x.split(,) splits s string with commas.
# '/t' is tab in Python. '\t\t' is tabbing twice in Python.
        
def convertCelToFah(x):
    y = x.split(',')
    print ('Celsius'+'\t\t'+'Fahrenheit')
    for item in y:
        fahrenheit = 9/5*eval(item)+ 32
        print (str(item)+'\t\t'+("%.1f" % fahrenheit))

# 'Main' is the bulk of this project.

def main():
    choice = eval(input("Convert to degrees or celsius(Enter 0 or 1): "))
    if choice == 0:
        x = input("Enter 4 temperatures in degrees Fahrenheit seperated by a comma: ")
        convertFahToCel(x)
    elif choice == 1:
        x = input("Enter 4 temperatures in degrees Celsius seperated by a comma: ")
        convertCelToFah(x)

# 'elif' means 'else if' or 'the second condition.'
        
main()
