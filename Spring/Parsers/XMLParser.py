import xml.etree.ElementTree as ETree

class XMLParser:
	def getAttribute(self, xmlString, xmlTag):
		xmlString = ETree.fromstring(xmlString)
		for child in xmlString:
			for x in child.getchildren():
				if(x.tag == xmlTag):
					return x.text