# Project #4
# Name: Destinee Monroe
# Class Section: CSC 105-01
# Purpose: The purpose of this project is to use information
# on a text file to respond to formulas created in our python program.
# This project builds upon what we accomplished in previous projects.
# Date: 4/12/14


# The numbers in the text file being read backwards
# so I switched the height and weight.

#'height**2' is height squared. 'height*height' does
# not equal height squared in the formula.

def getBMI (height, weight):
    BMI=(weight*703)/(height**2)
    return BMI

def getStatus(z):

    if z > 30:
        return('Obese')

    elif z >=25.0:
        return('Overweight')

    elif z>=18.5:
        return('Normal')

    elif z >= 18.5 and z<=18.5:
        return('Underweight')

def main():
    print('Height(inches)   Weight(Pounds)  BMI      Weight Status')
    print('-------------------------------------------------------')

# Saved bodyWeight.dat as bodyWeight.txt in same file as python project.
# .txt is a text file.

    infile=open('bodyWeight.txt')
    for line in infile:
        data = line.split()

# I made shortcuts to defined formulas.

        BMI = getBMI(int(data[0]),int(data[1]))
        status = getStatus(BMI)
        print(data[0],'\t\t',data[1],'\t\t',"%.2f" % BMI,'\t ',status)    
    print('-------------------------------------------------------')

main()
