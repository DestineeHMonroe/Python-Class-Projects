# Name: Destinee Monroe
# Class Session: CSC 105-01
# Purpose: The purpose of this project is to advance futher from our last project.
# We are learning how to answer prompts  with numbers and non-numbers multiple
# times.
# Date: 4/30/2014

def convertFahToCel(F):
    C=(F-32)*5/9
    return C

def convertCelToFah(C):
    F=9/5*C+32
    return F

def getColorCode (X):

    if X>110:
        return('Red')

    elif X>=90:
        return('Orange')

    elif X>=32:
        return('Yellow')

    elif X<32:
        return('Blue')

def main():
        numTemp=eval(input('Please tell the number of temperatures to convert?: '))
        if numTemp == 0:
            print('(Execution ends)')
        else:
            # 'eval(input(''))' is for answers that are numbers.
            # 'input('')' is for answers that are non-numbers.
            for i in range(numTemp):
                # 'degTemp' and 'typeTemp' are shortcuts.
                degTemp=eval(input('[#]'+' Enter the temperature in degrees: '))
                typeTemp=input('Is it Fahrenheit or Celsius? [F/C]: ')
                if typeTemp == 'F' or typeTemp == 'f':
                    # 'conversion' and 'code' are shortcuts.
                    conversion = convertFahToCel(degTemp)
                    code = getColorCode(degTemp)
                    print('    ',degTemp, 'F =', '%.2f' % conversion, 'C'+'\t'+'  Code:', code)
                if typeTemp == 'C' or typeTemp == 'c':
                    conversion = convertCelToFah(degTemp)
                    code = getColorCode(conversion)
                    print('    ',degTemp, 'C =',format(conversion,'.2f'), 'F'+'\t'+'  Code:', code)
                    # ['%.2f' % conversion] = [ format(converion,'.2f')]
main()
