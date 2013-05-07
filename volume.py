
'''
The volume converter takes in amount, source unit and destination unit.
Its output is the amount the source unit was in the destination unit.
'''
def volumeconverter(amount,sourceunit,destinationunit):
    #converting to base unit L
    if sourceunit == 'L':
        masterunit = amount
    elif sourceunit == 'mL':
        masterunit = amount*.001
    elif sourceunit == 'floz':
        masterunit = amount*.02957
    elif sourceunit == 'cup':
        masterunit = amount*.2365
    elif sourceunit == 'pint':
        masterunit = amount*.4731
    elif sourceunit == 'qt':
        masterunit = amount*.9464
    elif sourceunit == 'gal':
        masterunit = amount*3.785
    #converting L to destination unit
    if destinationunit == 'L':
        answer = masterunit*1
    elif destinationunit == 'mL':
        answer = masterunit*1/.001
    elif destinationunit == 'floz':
        answer = masterunit*1/.02957
    elif destinationunit == 'cup':
        answer = masterunit*1/.2365
    elif destinationunit == 'pint':
        answer = masterunit*1/.4731
    elif destinationunit == 'qt':
        answer = masterunit*1/.9464
    elif destinationunit == 'gal':
        answer = masterunit*1/3.785
        
    return answer