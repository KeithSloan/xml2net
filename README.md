# xml2net.py version 0.1 Alpha

Python program to convert Fritzing XML Netlist to KiCAD netlist

Syntax

  python xml2net.py [Source XML file] [Output_Net_file]

##Workflow

###In Fritzing

-  Create breadboard circuit in Fritzing
-  Export circuit to XML Netlist - File | Export Netlist

###Run xml2net program

###In KiCAD

-  Invoke schematic EEschema
-  Then select run CvPCB - third icon from right - op amp & ic
-  Then open Netlist - File | Open
-  Allocate foot prints
-  Save as cmp file - helps to name same prefix as netlist`
-  Go to PcbNew
-  Open Netlist and associated cmp file
-  Make sure select option - top arrow right hand side`
-  Select Mode - fourth icon from right - ic with cross arrows
-  Right click mouse button on blank bit of board
-  Global Spread & place
-  Complete PCB design

##Known Challenges

  For the test file I had to change the standard footprint of the transistor  
  pins 1,2,3 to Emitter, Base, Collector. In the supplied Library they
  where E,B,C

##Files

  Sample test files in this repository

- LICENSE          - License
- Terms-Conditions - Terms & Conditions

- Transistor.fzz       - Fritzing sample transitor circuit
- Transistor_schem.png - Fritzing export image of circuit

- KiCAD_import - KiCAD project directory

  - KiCAD_import.cmp          - KiCAD component file
  - KiCAD_import.kicad_pcb    - KiCAD PCB File
  - KiCAD_import.net          - Converted KiCAD netlist
  - KiCAD_import.pro          - KiCAD Project file
  - KiCAD_import.sch          - KiCAD schematic
  - Transistor_netlist.xml    - Exported Fritzing XML netlist

- KiCAD_import.pretty - KS Library Modified footprint library

#Feedback

   Feedback to keith@sloan-home.co.uk

