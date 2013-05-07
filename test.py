#Take in string
#start while loop to keep stuff running
#parse relavent information (raw input)
#try, except stuff for errors in input
#find what units you are converting from
#export relavent information to converter
#have converter convert to base unit and then requested unit

from parser import parser
from distance import distanceconverter
from volume import volumeconverter
from weight import weightconverter

'''The unitconverter function takes in a string formatted as follows
AMOUNT SOURCE_UNIT in DESTINATION_UNIT and outputs AMOUNT SOURCE UNIT = ANSWER DESTINATION_UNIT




'''
def unitconverter():
    #program gives directions
    print '''This is a unit converter written by Will Drevno. Conversions accepted are distance, weight and volume.
    
   Distances: ft cm mm mi m yd km in
   Weights: lb mg kg oz g
   Volumes: floz qt cup mL L gal pint
    
    '''
    #condition being set to when program should quit
    q = 0
    while q == 0:
        inputstring = raw_input('Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ')
        if not inputstring == 'q':
            
            stringdata = parser(inputstring) #parses the string
            amount = float(stringdata[0]) #assigns each part of the separated string to a variable
            sourceunit = stringdata[1]
            destinationunit = stringdata[3]
            #following series of if and elif statements directs the string data to its respective function
            if not ' m cm mm km in ft yd mi'.find(sourceunit) == -1:
                output = distanceconverter(amount, sourceunit, destinationunit)
            elif not 'L mL floz cup pint qt gal'.find(sourceunit) == -1:
                output = volumeconverter(amount, sourceunit, destinationunit)
            elif not 'g kg mg oz lb'.find(sourceunit) == -1:
                output = weightconverter(amount, sourceunit, destinationunit)
            #formats and prints answer
            outputformatted = str(amount) + ' ' + sourceunit + ' = ' + str(output) + ' ' + destinationunit
            print outputformatted
            break
                
        else:
            #code for what to when the user hits q
            print 'Bye!'
            q = q+1
    
unitconverter()

