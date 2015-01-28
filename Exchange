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

def Input_Curr(Input):
    str(Input)
    if Input in data:
        print "Accepted"
        return float(data[Input])
    else:
        print "Error: Not Found"
        Input_Curr(str(raw_input("What Currency?")))

def Input_Value(Value):
    try:
        float(Value)
    except ValueError:
        print "Error"
        Input_Value(raw_input("ValueError: How Much?"))
    if Value <= 0:
        Input_Value(raw_input("Error: How Much?"))
    if Value == type(int) or type(float):
        print "Accepted"
        return float(Value)
    else:
        print "No Good"
        Input_Value(raw_input("Error: How Much?"))
        
def Output_Curr(Output):
    str(Output)
    if Output in data:
        print "Accepted"
        return float(data[Output])
    else:
        print "Error: Not Found"
        Output_Curr(raw_input("Into What?"))

def Output_Value():
    print InputCurr
    print InputVal
    print OutputCurr
    return round((float(1) / InputCurr) * InputVal * OutputCurr,2)


InputCurr = Input_Curr(raw_input("What Currency?"))
OutputCurr = Output_Curr(raw_input("Into What?"))
InputVal = Input_Value(raw_input("How Much?"))
print Output_Value()
