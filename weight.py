

'''
The weight converter takes in amount, source unit and destination unit.
Its output is the amount the source unit was in the destination unit.
'''

def weightconverter(amount,sourceunit,destinationunit):
    #converting to base unit g
    if sourceunit == 'g':
        masterunit = amount
    elif sourceunit == 'kg':
        masterunit = amount*1000
    elif sourceunit == 'mg':
        masterunit = amount*.001
    elif sourceunit == 'oz':
        masterunit = amount*28.3495
    elif sourceunit == 'lb':
        masterunit = amount*453.592

    #converting from g to destination unit
    if destinationunit == 'g':
        answer = masterunit*1
    elif destinationunit == 'kg':
        answer = masterunit*1/1000
    elif destinationunit == 'mg':
        answer = masterunit*1/.001
    elif destinationunit == 'oz':
        answer = masterunit*1/28.3465
    elif destinationunit == 'lb':
        answer = masterunit*1/453.592

        
    return answer