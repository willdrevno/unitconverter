'''
The distance converter takes in amount, source unit and destination unit.
Its output is the amount the source unit was in the destination unit.
'''
def distanceconverter(amount,sourceunit,destinationunit):
    #converting to base unit of meters
    if sourceunit == 'm':
        masterunit = amount
    elif sourceunit == 'cm':
        masterunit = amount*.01
    elif sourceunit == 'mm':
        masterunit = amount*.001
    elif sourceunit == 'km':
        masterunit = amount*1000
    elif sourceunit == 'in':
        masterunit = amount*.0254
    elif sourceunit == 'ft':
        masterunit = amount*.3048
    elif sourceunit == 'yd':
        masterunit = amount*.9144
    elif sourceunit == 'mi':
        masterunit = amount*1609.34
    #taking the amount of meters and converting to the destination unit
    if destinationunit == 'm':
        answer = masterunit*1
    elif destinationunit == 'cm':
        answer = masterunit*1/.01
    elif destinationunit == 'mm':
        answer = masterunit*1/.001
    elif destinationunit == 'km':
        answer = masterunit*1/1000
    elif destinationunit == 'in':
        answer = masterunit*1/.0254
    elif destinationunit == 'ft':
        answer = masterunit*1/.3048
    elif destinationunit == 'yd':
        answer = masterunit*1/.9144
    elif destinationunit == 'mi':
        answer = masterunit*1/1609.34
        
    return answer