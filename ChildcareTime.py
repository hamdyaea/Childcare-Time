#Developer : Hamdy Abou El Anein

from easygui import *
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom


totalDate1 = []
totalHours1 = []
totalAdded1 = []


def displayResultBobby():

    tree = ET.parse('work.xml')
    root = tree.getroot()

    for Bobby in root.findall("Bobby"):
        totalDate = Bobby.get("date")
        totalHours = Bobby.get("hours")
        totalAdded = Bobby.get("added")


        totalDate1.append(totalDate)
        totalHours1.append(totalHours)
        totalAdded1.append(totalAdded)

def displayResultSam():

    tree = ET.parse('work.xml')
    root = tree.getroot()

    for Sam in root.findall("Sam"):
        totalDate = Sam.get("date")
        totalHours = Sam.get("hours")
        totalAdded = Sam.get("added")


        totalDate1.append(totalDate)
        totalHours1.append(totalHours)
        totalAdded1.append(totalAdded)



def displayResultSarah():

    tree = ET.parse('work.xml')
    root = tree.getroot()

    for Sarah in root.findall("Sarah"):
        totalDate = Sarah.get("date")
        totalHours = Sarah.get("hours")
        totalAdded = Sarah.get("added")


        totalDate1.append(totalDate)
        totalHours1.append(totalHours)
        totalAdded1.append(totalAdded)


def addStuffBobby():

    msg = "Enter new informations"
    title = "Enter new informations"
    fieldNames = ["Date : ", "Hours : ", "Additional : "]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)

    newDate = fieldValues[0]
    newHours = fieldValues[1]
    newAdd = fieldValues[2]

    doc = ET.parse("work.xml")
    root = doc.getroot()



    data1 = ET.Element("Bobby", {"date": newDate,
                                "hours": newHours,
                               "added" : newAdd})

    root.append(data1)
    out = ET.tostring(root)
    dom = minidom.parseString(out)

    dom.toprettyxml()


    doc.write("work.xml")

def addStuffSarah():

    msg = "Enter new informations"
    title = "Enter new informations"
    fieldNames = ["Date : ", "Hours : ", "Additional : "]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)


    newDate = fieldValues[0]
    newHours = fieldValues[1]
    newAdd = fieldValues[2]

    doc = ET.parse("work.xml")
    root = doc.getroot()



    data1 = ET.Element("Sarah", {"date": newDate,
                                "hours": newHours,
                               "added" : newAdd})

    root.append(data1)
    out = ET.tostring(root)
    dom = minidom.parseString(out)

    dom.toprettyxml()


    doc.write("work.xml")



def addStuffSam():

    msg = "Enter new informations"
    title = "Enter new informations"
    fieldNames = ["Date : ", "Hours : ", "Additional : "]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)

    newDate = fieldValues[0]
    newHours = fieldValues[1]
    newAdd = fieldValues[2]

    doc = ET.parse("work.xml")
    root = doc.getroot()



    data1 = ET.Element("Sam", {"date": newDate,
                                "hours": newHours,
                               "added" : newAdd})

    root.append(data1)
    out = ET.tostring(root)
    dom = minidom.parseString(out)

    dom.toprettyxml()


    doc.write("work.xml")


msg1 = "What do you want to do ?"
choices = ["Bobby","Sarah","Sam","Add things to Bobby","Add things to Sarah","Add things to Sam"]
reply = buttonbox(msg1, choices=choices)

if reply == "Bobby":
    showResults = displayResultBobby()
    msg = "All informations for Bobby"
    title = "All informations for Bobby"
    fieldName = (
    "\nDate : " + str(totalDate1), "\nHours : " + str(totalHours1), "\nThings added : " + str(totalAdded1))
    textbox(msg=msg, title=title, text=fieldName)
elif reply == "Sam":
    showResults = displayResultSam()
    msg = "All informations for Sam"
    title = "All informations for Sam"
    fieldName = (
    "\nDate : " + str(totalDate1), "\nHours : " + str(totalHours1), "\nThings added : " + str(totalAdded1))
    textbox(msg=msg, title=title, text=fieldName)
elif reply == "Sarah":
    showResults = displayResultSarah()
    msg = "All informations for Sarah"
    title = "All informations for Sarah"
    fieldName = (
    "\nDate : " + str(totalDate1), "\nHours : " + str(totalHours1), "\nThings added : " + str(totalAdded1))
    textbox(msg=msg, title=title, text=fieldName)
elif reply == "Add things to Bobby":
    addStuffBobby()
elif reply == "Add things to Sarah":
    addStuffSarah()
elif reply == "Add things to Sam":
    addStuffSam()
else:
    sys.exit(0)

