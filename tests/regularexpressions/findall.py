# A Python program to demonstrate working of
# findall()
import re
 
# A sample text string where regular expression
# is searched.
string = """-5+12/4201^2 - 72 + 3 = 56x+32 * 4x(25-32) - 32"""

string = string.replace(" ", "") #get rid of white spaces
print("removed white spaces:", string)

#split by parentheses as terms:
#print(re.split("(\(.+\))", string))

addition = "\+"
subtraction = "\-"
division = "/"
multiplication = "\*"
equalsign = "="
exponents = "\^"
startparentheses = "\("
endparentheses = "\)"
splitbyop = re.split(f"([{addition}|{subtraction}|{division}|{multiplication}|{equalsign}|{exponents}|{startparentheses}|{endparentheses}])", string) #split by any type of operator (+, -, /, *, =, ^, (, or ))
splitbyop = [i for i in splitbyop if i] #remove empty strings in list

print("split by operator:", splitbyop)
x_values = [i for i in splitbyop if "x" in i] #find all x values in the list
print(x_values)