# # Challenge 1: The Profile Formatter (Basic)
# a = input("Enter your first name: ")
# b = input("Enter your last name : ")
# print(len(a+b), )
# print(a+b)
# Variables ko meaningful naam diya
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Strings ko joda, beech mein space ke saath
# full_name = first_name + " " + last_name

# # Escape sequences (\n nayi line ke liye, \t tab space ke liye) aur .upper() ka use
# print("\n--- User Profile ---")
# print("Full Name:\t" + full_name.upper()) 

# # Total length nikalte time humne space ko count nahi kiya (isliye first_name aur last_name ko direct joda)
# # Integer length ko wapas string mein Typecast kiya taki print function mein error na aaye
# length_of_name = len(first_name + last_name)
# print("Total Letters:\t" + str(length_of_name))
# print("--------------------")

# a = int(input("Enter your number: "))     #word.replace("cod", "done")
# print = (f"Secure Mobile Number: +91-", word.replace("a", "x"))
#example 
# Step 1: User se input liya. (input by default string hi hota hai)
# mobile_number = input("Enter your 10-digit mobile number: ")

# # Step 2: String Slicing - Last ke 3 digits nikalne ke liye
# # [7:] ka matlab hai index 7 se le kar string ke end tak
# last_three = mobile_number[7:] 

# # Step 3: Masking logic - "XXXXXXX" string ke sath last_three ko jod diya
# secure_number = "XXXXXXX" + last_three

# # Step 4: Final print
# print("Secure Mobile Number: +91-" + secure_number)



# Challenge 3
# # Step 1: Module ko import kiya
# import datetime

# # datetime module se aaj ki date nikali
# aaj_ki_date = datetime.date.today()

# # Step 2: User Input aur Typecasting
# item_name = input("Kya kharidna hai? (Item Name): ")

# # input() string deta hai, isliye float() ka use karke usko number mein badla
# price = float(input("Ek item ki price kitni hai?: ")) 

# # Quantity humesha puri hoti hai (jaise 2, 3), isliye int() ka use kiya
# quantity = int(input("Kitni quantity chahiye?: "))

# # Step 3: Calculation logic
# total_amount = price * quantity

# Step 4: Output ko ek bill ki tarah format karna
# "=" * 30 likhne se "=" 30 baar print ho jayega (String operation)
# print("\n" + "="*30)
# print("\tMINI INVOICE")
# print("="*30)

# # Date, price, quantity aur total_amount number/date hain,
# # isliye print karte time unhe wapas str() mein typecast kiya
# print("Date:\t\t" + str(aaj_ki_date))
# print("Item:\t\t" + item_name)
# print("Price:\t\t₹" + str(price))
# print("Quantity:\t" + str(quantity))
# print("-" * 30)
# print("TOTAL AMOUNT:\t₹" + str(total_amount))
# print("=" * 30)




# English_word = input("Enter your favorite English word: =  ")
# total_length = len(English_word)
# in_uppercase = (English_word.upper())
# String_Slicing = English_word[:3]
# String_Slicing1 = English_word[-2:]


# print(("Total letters:"),total_length)
# print("IN Uppercase :",in_uppercase)
# print("First 3 letters : ",String_Slicing)
# print("First 2 letters :",String_Slicing1)



# challenge 4 
# user = input("Enter your first name:  ")
# user_last = (input("Enter your last name: "))
# user_name = (user +" "+ user_last)
# name = (user_name.upper())
# age =  int(input("Enter your age: "))
# city = input ("Enter your city: ")
# graduation_age = (age + 4)
# Slicing = name[:2]
# Slicing1 = name[-2:]
# id = (Slicing+Slicing1)
# secret_id = (id.upper())
# print("-----------------------  \n  Student ID Card  \n ---------------------" )
# print("Name:   \t",name)
# print("city:   \t",city.upper())
# print("secret_id:   ",secret_id)
# print("graduation_age:\t",graduation_age)
# print("-----------------------------------")



# Challenge5
# user = input("Enter a password (min 6 letters): ")
# secret_pin = int(input("Enter a secret 2-digit PIN: "))
# security_key = (secret_pin*3)
# slicing = user[:3]
# slicing1 = user[-3:]
# Original = (slicing.upper())
# orignal1 = (slicing1.lower())
# encrypted_password = (Original+str(security_key)+orignal1)
# total_length = (len(encrypted_password))
# print("****************************************\n ENCRYPTION REPORT \n **************************************** \n")
# print("Original Password:\t",user)
# print("Security Key:      \t",security_key)
# print("Encrypted Password: \t",encrypted_password)
# print("Password Length: \t",total_length)
# print("****************************************")




#  Challenge 6: The Profile URL Creator 🌐
company_name = input("Enter your company name: ")
user_first = input("Enter your First name : ")
user_DOB = input("Enter your Birth year: ")
lower = (company_name.lower())
lower1 = (user_first.lower())
slicing = user_DOB[-2:]
url = (f"www.{lower}.com/{lower1}{slicing}")
secret_number = (int(user_DOB)*2)
slicing1 = (company_name[:3])
upper = (slicing1.upper())
slicing2 = (user_first[-3:])
lower2 = (slicing2.lower())
Password = (upper+lower2+str(secret_number))

print("-----------------------------------\nEMPLOYEE PROFILE GENERATED \n-----------------------------------")
print("Profile URL:", url)
print("Temp Password: ",Password)
print("-----------------------------------")



