# # Challenge 10: The Smart Traffic Light 🚦
# user = input("What are the colors of a traffic light?").strip().lower()
# if (user == "red"):
#     print("plese stop the car ")
# elif (user=="yellow"):
#     print("plese start the engine and wait ")
# elif (user=="green"):
#     print("you can go now")
# else:
#     print("you enter wrong colour ")
    


# Challenge 11: The Smart Speed Fine Calculator 🚗💨
# speed = int(input("Enter The vehicle speed: "))
# if speed < 60:
#     print("Speed normal hai, araam se chalao. (No Fine)")
# elif speed >= 60 and speed <= 90 :
#     print("Warning! Speed limit cross ho rahi hai, dheere karo.")

# else:
#     print("Bahut tez chala rahe ho! ₹2000 ka Challan katega!")


# Challenge 12: Smart Food Delivery System 🛵 (Zomato/Swiggy Logic)
# user = float(input("Enter the order distance: "))
# if user <=2 :
#     print("Khushkhabri! Delivery bilkul FREE hai! 🎉")
# elif 2<user<=5:
#     print("Aapka Delivery Charge: ₹30 lagega.")
# elif 5<user<=10:
#     print("Aapka Delivery Charge: ₹60 lagega.")
# else:
#     print("Sorry bhai, itni door delivery nahi ho payegi! ❌")



# Challenge 13: Pharmacy Stock Alert System 💊
# medicine_stock = int(input("Dawai ke kitne patte (strips) bache hain? "))
# if medicine_stock ==0:
#     print("🚨 ALERT: Dawai bilkul khatam ho gayi hai! OUT OF STOCK!")
# elif 1<= medicine_stock <=10:
#     print("⚠️ WARNING: Stock khatam hone wala hai, naya order place karein!")
# elif 11<=medicine_stock<=50:
#     print("✅ Stock bilkul normal aur safe hai.")
# else:
#     print("📦 Overstocked! Is dawai ka naya order mat lagana.")

# Challenge 14: E-Commerce Mega Sale (Real-World Task) 🛒
# bill_amount = float(input("Enter your total amount: "))
# if bill_amount >= 5000:
#     discount = (bill_amount * 20) / 100
#     final_amount = bill_amount - discount

# elif 2000 <= bill_amount < 5000:
#     discount = (bill_amount * 10) / 100
#     final_amount = bill_amount - discount
# else:
#     final_amount = bill_amount + 50
# print(final_amount)



# # Challenge 15: NexCure Security Login (Real-World Task) 🔐
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username=="admin":
#     if password == "pharma123":
#         print("Welcome to Dashboard! 🚀")
#     elif password != "pharma123":
#         print("Alert: Wrong Password entered! ❌")
# else:
#     print("Error: Invalid Username! 🛑\n \tInvalid password")
