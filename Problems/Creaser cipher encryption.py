# Creaser cipher encryption of 10 characters {replace a with c, b with d, and so on}

input_string = input("Enter Message :")
separated_String = list(input_string)
result = ""

for i in separated_String:
    temp = (ord(i)+2)
    result += chr(temp)
print("Encrypted Message :", result)
