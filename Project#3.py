# Name: Destinee Monroe
# Class Session: CSC 105-01
# Purpose: The purpose of this project is to learn how to create a chart
# that uses multiple functions. Learning how to list the colors on the
# right side of the chart is a challenge.
# Date: 4/4/2014

def convertFahToCel(F):
    C=(F-32)*5/9
    return C

def getColorCode(C):
    
    if C >110:
        return('red')

    elif C >=90:
        return('orange')

    elif C >=32:
        return('yellow')

    elif C >=0:
        return('blue')

def main():
    a,b,c,d=eval(input('Enter 4 temperatures in degree Fahrenheit separated by a comma:'))

    print('Fahrenheit'+'\t'+'Celsius'+'\t\t'+'Color Code')

    print('------------------------------------------')

    print(format(a)+'\t\t'+format(convertFahToCel(a),'.1f')+'\t\t'+format(getColorCode(a)))
    print(format(b)+'\t\t'+format(convertFahToCel(b),'.1f')+'\t\t'+format(getColorCode(b)))
    print(format(c)+'\t\t'+format(convertFahToCel(c),'.1f')+'\t\t'+format(getColorCode(c)))
    print(format(d)+'\t\t'+format(convertFahToCel(d),'.1f')+'\t\t'+format(getColorCode(d)))

    print('------------------------------------------')

main()
