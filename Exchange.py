import json
import time
import pdb
import re
import os
from urllib2 import urlopen

# pulls the exchange rate info to be used. The info come in a list, so it needs to be changed to a dictionary
data = urlopen("http://www.getexchangerates.com/api/latest.json")
data = json.load(data)
data = data.pop(0)

print "Data retrieved at: %s" % data["DateTime"]

def Input_Curr():
    global Input
    Input = str(raw_input("What currency are you coverting FROM?"))
    while Input.upper() not in data:
        print "Invalid Currency"
        Input = str(raw_input("What currency are you coverting FROM?"))
    print "Accepted: ", Input.upper()
    return float(data[Input.upper()])


def Input_Value():
    global Value
    Value = raw_input("How much are you converting?")
    while True:
        try:
            float(Value)
            print "Accepted: ", Value
            return float(Value)
        except ValueError:
            print "Invalid Input"
            Value = raw_input("How much are you converting?")
            
   
def Output_Curr():
    global Output
    Output = str(raw_input("What currency are you coverting TO?"))
    while Output.upper() not in data:
        print "Invalid Currency"
        Output = str(raw_input("What currency are you coverting TO?"))
    print "Accepted: ", Output.upper()
    return float(data[Output.upper()])

def Output_Value():
    return round((float(1) / InputCurr) * InputVal * OutputCurr,2)

InputCurr = Input_Curr()
OutputCurr = Output_Curr()
InputVal = Input_Value()
print Value, Input, " = ", Output_Value(), Output

