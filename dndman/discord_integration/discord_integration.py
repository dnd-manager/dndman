assembly_path = r"C:\School\Grade10\ICS3U\DnDMan\dndman\discord_integration"

import sys
sys.path.append(assembly_path)

import clr
clr.AddReference("DnDManBot")

from DnDManBot import Test

testObj = Test()
testObj.Print()
print(testObj.Add(1, 2))