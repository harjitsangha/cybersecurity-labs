# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")
# print(len(name)) # length of the string
# print(name.find("h")) # firts occurence index starts at 0, method will return -1 if there are no results
# print(name.rfind("h"))  # last occurence index starts at 0, method will return -1 if there are no results
# print(name.capitalize()) 
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(phone_number.count("-")) # count number of -'shes
# print(phone_number.replace("-", " ")) # replace -'shes with a space

username = input("Enter a username: ")

if len(username) > 12:
    print("Username cannot be greater than 12 characters")
if not username.find(" ") == -1:
    print("username cannot contain spaces")
if not username.isalpha():
    print("Username cannot contain digits")

# indexing = accessing elements of a sequence using [] (indexing operatos)
# [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[0:4])
print(credit_number[3:])
print(credit_number[0:4:2])
print(credit_number[-4])
print(credit_number[::3]) # count every 3rd character
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}") # last 4 digit numbers
print(credit_number[::-1]) # reverse the string

