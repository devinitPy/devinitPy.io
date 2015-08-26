import os
from lxml import etree
import re

#function  to use for getting text from tag
build_text_list = etree.XPath("//text()")

def pdf_read(file_name):
    #cmd = "pdftotext "+file_name+" my_pdf.txt"
    cmd = "pdftohtml -xml -nodrm -zoom 1.5 -enc UTF-8 -noframes "+file_name+" my_pdf.xml"
    os.system(cmd)
    xml_file = open("my_pdf.xml","r")
    xml_data = xml_file.read()
    #print xml_data
    # #configuring parser
    parser = etree.XMLParser(remove_blank_text=True,recover=True)
    # #obtaining xml doc trees
    parsed_data = etree.XML(xml_data, parser)
    # data = etree.tostring(root, pretty_print=True)

    return parsed_data

def tree_manuplations(root):
    #first root child / tag
    child = root[1]
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
    for element in root.iter("text"):
        print("%s - %s" % (element.tag, element.text))
        #print("tag {0} ".format(element.text))

def write_to_file(data):
    filename="results.csv"
    file = open(filename, 'w')
    file.write(data)


data = pdf_read("cv.pdf")
tree_manuplations(data)
write_to_file(data[1])
