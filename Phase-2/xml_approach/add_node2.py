import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from bs4 import BeautifulSoup 
import re

#tree.write('output.xml')
tree = ET.parse('xml_prac.xml')
root = tree.getroot()
file1 = open('transcript.txt','r')
lines = file1.readlines()
if_flag = 0
if_stack = []

def make_input(splitting):
	global prev
	for i in range(2,len(splitting)):
		addElement = ET.Element('var',input_tag='yes')
		j = splitting[1]
		sub = ET.SubElement(addElement,'type')
		sub.text = j
		sub = ET.SubElement(addElement,'name')
		sub.text = splitting[i]
		prev.append(addElement)
	
def make_if(splitting):
	global if_flag
	addElement = ET.Element('if')
	sub = ET.SubElement(addElement,'op1')
	sub.text = splitting[1]
	sub = ET.SubElement(addElement,'op2')
	sub.text = splitting[3]
	sub = ET.SubElement(addElement,'op')
	sub.text = splitting[2]
	sub = ET.SubElement(addElement,'exec')
	sub.text = " "
	if if_flag==0:
		root.append(addElement)
		global prev
		prev = sub
		if_stack.append(sub)
		if_flag = 1
	elif if_flag==1 and prev.text == " ":
		prev.append(addElement)
		prev = sub
		if_stack.append(sub)
	
def make_print():
	splitting = line.strip()[6:]
	#print(splitting)
	global prev
	if splitting.startswith('"') and splitting.endswith('"'):
		sub = ET.SubElement(prev,'type')
		sub.text = 'print'
		sub = ET.SubElement(prev,'content')
		sub.text = splitting

	
for line in lines:
	if "start the program" in line:
		global prev
		prev = root
		
	elif "input" in line:
		splitting = line.strip().split(" ")
		print(splitting)
		make_input(splitting)

	elif "endif" in line:
		if_flag = 0
		if_stack.pop(-1)
		if if_stack:
			prev = if_stack[-1]
	
	elif "if " in line:
		if if_flag==0:
			make_if(line.strip().split(" "))
		elif if_flag==1 and prev.text ==" ":
			make_if(line.strip().split(" "))
			
	elif "print" in line:
		make_print()
		
	
			
	tree.write('xml_prac.xml')

	
def pretty_xml(element, indent, newline, level=0):  
    if element:   
        if (element.text is None) or element.text.isspace():  
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
           
    temp = list(element) 
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  
            subelement.tail = newline + indent * (level + 1)
        else:   
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  


tree1 = ElementTree.parse('xml_prac.xml')  
root = tree1.getroot()  
pretty_xml(root, '\t', '\n')  
tree1.write('output.xml')
