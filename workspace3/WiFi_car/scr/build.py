import os
a = "D:\workspace3\WiFi_car\scr"
b = raw_input("Podaj nazwe skryptu (.py) do skompilowania: ")
c = "FreezePython --install-dir"+" "+a+" "+b
print c
os.system(c)
