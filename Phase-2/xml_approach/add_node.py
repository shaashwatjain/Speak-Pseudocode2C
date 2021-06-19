import xml.etree.ElementTree as ET
tree = ET.parse('xml_prac.xml')
root = tree.getroot()

file1 = open('transcript.txt','r')
 
count = 0
while True:
    count += 1
 
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    line = line.strip()+ ' '
    s = line.split(" ")
    '''
    indent = 0
    line = line.rstrip('\n')
    s = line.split(" ")
    for i in s[0]:
    	if i=='\t':
    		indent+= 1
    print(indent)
    '''
    if s[0]=='if':
    	a = root.find('a')
    	if_stat = ET.SubElement(a,'if')
    	if_stat.tail = '\n\t'
    	op1 = ET.SubElement(if_stat,'op1')
    	op1.tail = '\n\t\t'
    	op1.text = s[1]
    	op2 = ET.SubElement(if_stat,'op2')
    	op2.text = s[3]
    	op2.tail = '\n\t\t'
    	operand = ET.SubElement(if_stat,'op')
    	if s[2] == '=':
    		operand.text = '=='
    	operand.tail = '\n\t'
    	exec_stat = ET.SubElement(if_stat,'exec')
    	exec_stat.tail = '\n\t\t'
    	
    elif s[0]=='for':
    	a = root.find('a')
    	addElement = ET.Element('for')
    	addElement.tail = "\n" 
    	addElement.text = "\n\n\t" 
    	newData = ET.SubElement(addElement, "init")
    	newData.tail = '\n\t'
    	newData.text = "\n\t\t" 
    	op1 = ET.SubElement(newData,'op1')
    	op1.text = s[1]
    	op1.tail = '\n\t\t'
    	op2 = ET.SubElement(newData,'op2')
    	op2.text = s[3]
    	op2.tail = '\n\t'
    	newData2 = ET.SubElement(addElement, "terminate")
    	newData2.tail = '\n'
    	newData2.text = "\n\t\t"
    	op1 = ET.SubElement(newData2,'op1')
    	op1.text = s[1]
    	op1.tail = '\n\t\t'
    	op2 = ET.SubElement(newData2,'op2')
    	op2.text = s[5]
    	op2.tail = '\n\t\t'
    	op = ET.SubElement(newData2,'op')
    	op.tail = '\n\t'
    	if s[4]=='to':
    		op.text = 'lt'
    	a.append(addElement)
    
    #if s[0]=='if':
    #	prev = if_stat.exec
    tree.write('xml_prac.xml')
    
    print(s)
 
file1.close()

