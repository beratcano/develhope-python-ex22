num1 = 1122334455666
num1_str = str(num1)

print(len(num1_str))
print(num1_str[2])
print(num1_str[2:5])
print( "2" in num1_str)
print( "3" in num1_str)

string_with_0 = "0" + num1_str

print(string_with_0[:4])
print(string_with_0[4:])
#There is no 567 in this number
