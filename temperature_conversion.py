from dateutil import parser
import re
import math


def temp_conv(temp):
    target_char = 'C'

    '''
    Temperature conversion . 
    1.Checking if the temperature is in Celsius  2 Extracting the number (generator ->to list ) 
    3.Calculating the conversion  4.Back to String conversion
    '''

    if target_char in temp:
        temp = list((int(converted_temp) for converted_temp in re.findall(r'-?\d+\.?\d*', temp)))
        temp = (float(temp[0]) * 1.8) + 32
        temp = str(math.floor(temp)) + 'F'
    else:
        temp = [item.replace(" ", "") for item in temp]

    return temp

