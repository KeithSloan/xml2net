#!/usr/bin/python
# xml2net.py version 0.1 Alpha
# Copyright : Keith Sloan 2015
# email : keith@sloan-home.co.uk

import xml.sax
import codecs
import sys
import string

List = []
Pins = []
Names = []
Components = []
#net_fp = codecs.open(NetFile,"w","utf-8")

class xmlHandlerPass1(xml.sax.ContentHandler):
   def __init__(self):
     self.CurrentData = ""
     self.netlist = ""
     self.net = ""
     self.connector = ""
     self.pin = ""
     self.name = ""
     self.netNum = 0
     
   def startElement(self, name, attrs): 
#      if name == 'netlist':      
#         print("NetList")
#      elif name == "net" :
      if name == 'net' :
#           print("net")
           self.netNum += 1
      elif name == "connector":
#           print("connector")
           p = attrs.get("id")
           self.pin = str(string.atoi(p[9:])+1)
           self.name = attrs.get("name")
           Pins.append(self.pin)
           Names.append("N-%04d" % self.netNum)
      elif name == "part":
#           print("part")
           self.partLabel = attrs.get('label',"")
           Components.append(self.partLabel)
           t = attrs.get('title',"")
           self.partTitle = t.replace(" ","_")
#           print(self.partLabel)
#           print(self.partTitle)
           a = self.partLabel+","+self.partTitle
#           print(a)
           if a not in List :
              List.append(a)
      return

def formatList(l):
#    print(l)
    i = l.find(',')
    c = l[0:i]
    net_fp.write("( 0 $noname "+l[0:i]+" "+l[i+1:]+"\n")
    for j in range(len(Components)):
        if c == Components[j]:
           net_fp.write("( "+Pins[j]+" "+Names[j]+" )\n")
    net_fp.write(")\n")


class xmlHandlerPass2(xml.sax.ContentHandler):
   def __init__(self):
     self.CurrentData = ""
     self.netlist = ""
     self.net = ""
     self.connector = ""
     self.count = 1
     self.pin = ""
     
   def startElement(self, name, attrs): 
#      if name == 'netlist':      
#         print("NetList")
#      elif name == "net" :
      if name == "net" :
           net_fp.write("Net "+str(self.count)+' ""\n')
           self.count += 1
      elif name == "connector":
#           print("connector")
           p = attrs.get('id',"")
           self.pin = str(string.atoi(p[9:])+1)
      elif name == "part":
#           print("part")
           self.partLabel = attrs.get('label',"")
           net_fp.write(self.partLabel+" "+self.pin+"\n")
      return

if ( __name__ == "__main__"):
  
   if len(sys.argv) != 3 :
      print "Syntax is xml2net.py [input_xml_file] [output_net_file]" 
      exit(0)
   XMLfile = sys.argv[1] 
   print "Processing File : " + XMLfile
   NetFile = sys.argv[2]
   print "Output File : " + NetFile
   net_fp = codecs.open(NetFile,"w","utf-8")
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = xmlHandlerPass1()
   parser.setContentHandler( Handler )
   parser.parse(XMLfile)
#   print("==== List ====")
#   print '\n'.join(List)
   net_fp.write("# EESchema NetList Version 1.0\n(\n")
   for i in List:
       formatList(i)
   net_fp.write(")\n*\n")

   net_fp.write("{ Pin List by Nets\n")
   Handler = xmlHandlerPass2()
   parser.setContentHandler( Handler )
   parser.parse(XMLfile)
   net_fp.write("}\n#end\n")
   net_fp.close()
   print("Net file created") 
