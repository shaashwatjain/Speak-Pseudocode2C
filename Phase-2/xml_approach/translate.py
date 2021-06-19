import xml.etree.ElementTree as ET
from xml.etree import ElementTree
tree = ET.parse('xml_prac.xml')
root = tree.getroot()
f = open('output.c','a')

indent = 0
var_flag = 0
if_flag = 0
store_var = {}
def insert():
	print("#include<stdio.h>")
	print("#include<stdlib.h>")
	print("int main(int argc, char* argv[])")
	print("{")
	
def give_indent(indent):
	for i in range(indent):
		print("\t",end= '')
#print("hi")
for p in tree.iter():
	if p.tag=='root':
		insert()
		indent+= 1
	elif p.tag=='var' and p.attrib['input_tag']=='yes':
		var_flag = 1
		prev = p
	elif var_flag==1:
		give_indent(indent)
		for i in prev.iter():
			if i.tag=='type' and i.text=='integer':
				print("int",end =" ")
			elif i.tag=='name':
				print(i.text+';')
		for i in prev.iter():
			if i.tag=='type' and i.text=='integer':
				give_indent(indent)
				print('scanf("%d",',end = '')
			elif i.tag=='name':
				print("&{});".format(i.text))
		var_flag = 0
	elif p.tag=='if':
		if_flag = 1
		prev = p
	elif if_flag ==1 and p.tag=='op1':
		give_indent(indent)
		for i in prev.iter():
			if i.tag=='op1':
				op1 = i.text
			elif i.tag=='op':
				op = i.text
			elif i.tag=='op2':
				op2 = i.text
			elif i.tag=='exec':
				prev = i
		
		print("if ({}{}{})".format(op1,op,op2))
		
		give_indent(indent)
		print("{")
		indent+= 1
	elif if_flag==1 and p.tag =='exec':
		for i in prev.iter():
			if i.tag=='type':
				if i.text=='print':
					give_indent(indent)
					print("printf(",end='')
			elif i.tag=='content':
				print(i.text+');\n')
		if_flag = 0
		indent-=1
		give_indent(indent)
		print("}")
print("}")
		
		
		
		
	
