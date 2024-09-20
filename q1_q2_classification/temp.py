import xml.etree.ElementTree as ET
tree = ET.parse('temp.xml')
root = tree.getroot()

labels = []

for child in root:
    if child.tag == "object":
        print(child.find("name").text)
        difficult = child.find("difficult")
        if difficult != None:
            print(difficult.text)
        # print(child.attrib)
        # for x in child:
        #     if x.tag == "name":
        #         labels.append(x.text)