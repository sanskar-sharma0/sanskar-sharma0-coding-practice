# 02/08/2026

# Challenge 7: The Data Cleaner 🧹

messy_data = "   hello vansh bhai...!!!   "
clean_data = (messy_data.rstrip("...!!!   "))
data = (clean_data.replace("   " , ""))
clean = (data)
title = (clean.title())

word_list = (title.split(" "))
count = (clean.count("a"))
replace = (title.replace("bhai","sir"))
print(f"orignal:\t{messy_data}\nCleaned: \t{title}\nWord List:\t{word_list} \nCount of 'a':\t{count} \nReplaced:\t{replace}")

# Challenge 8: Pharmacy Inventory Formatter 💊
# check , () . " every time showw a error 
user = input("Enter medicine name: ").strip().title()
price = float(input("Enter Price: " ))
category = input("Enter Category: ").strip().upper()
cutting = (user[:3]).upper()
cut_category = (category[-2:]).lower()
med_id = (cutting+cut_category)
total_price = (price+15)
heading = ("NEW MEDICINE ADDED TO STOCK").center(40)
print(f"----------------------------------------\n{heading}\n----------------------------------------\nMedicine:\t{user}\nCategory:\t{category}\nMed ID:   \t{med_id}\nTotal Price:\t{total_price}\n----------------------------------------")


# Challenge 9: Smart Pharma Billing & Loyalty Module 🧾
customer_name = input("Enter customer name: ").strip().title()
total_bill = float(input("Enter your bill amount:  "))
discount_percent =int(input("Enter Discount (%): "))
discount_value = (total_bill*discount_percent)/100
final_amount = (total_bill-discount_value)
code = (customer_name[:3]).upper()
code1 = (customer_name[-2:]).lower()
loyalty_code = code + str(len(customer_name)) + code1


heading = ("PHARMACY RETAIL RECEIPT").center(40)
print(f"========================================\n{heading}\n========================================\nCustomer Name:\t{customer_name}\nTotal Bill:\t{total_bill}\nDiscount:\t{discount_value}\nFinal Payable:\t{final_amount}\n----------------------------------------\nLoyalty Code:\t{loyalty_code}\n========================================")
