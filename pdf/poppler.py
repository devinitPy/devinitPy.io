import sys, os
from lxml import etree
import re

#global method to use for getting text from tag
build_text_list = etree.XPath("//text()")

def pdf_read(file_name):
    cmd = "pdftotext "+file_name+" my_pdf.txt"
    cmd = "pdftohtml -xml -nodrm -zoom 1.5 -enc UTF-8 -noframes "+file_name+" my_pdf.xml"
    os.system(cmd)
    xml_file = open("my_pdf.xml","r")
    xml_data = xml_file.read()
    #configuring parser
    parser = etree.XMLParser(remove_blank_text=True,recover=True)
    #obtaining xml doc tree
    root = etree.XML(xml_data, parser)
    data = etree.tostring(root, pretty_print=True)
    #print(data)
    return root

def tree_manuplations(root):
    #first root child / tag
    child = root[0]
    print ("========================================")
    print (child.tag)
    print ("========================================")
    #number of pages
    print(len(root))
    #iterating through first level tags
    for child in root:
            print (child.tag)
            #returns a dictionary
            attributes = child.attrib
            print attributes["height"]
            print ("========================================")
            #we can iterate through the  rest of the tags here
    #using iterators
    for element in root.iter():
        print("%s - %s" % (element.tag, element.text))
        #print("tag {0} ".format(element.text))

def data_by_attribute(tree, attribute):
    pass

def data_by_attribute_parameter(tree, parameter):
    pass

def write_to_file(data):
    filename="results.csv"
    file = open(filename, 'w')
    file.write(data)


root = pdf_read("cv.pdf")
tree_manuplations(root)
write_to_file("hey")
