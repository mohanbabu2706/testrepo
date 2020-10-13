import re

#return a list containing every occurance of "ai":

txt = "The rain in Spain"

x = re.findall("ai",txt)

print(x)
