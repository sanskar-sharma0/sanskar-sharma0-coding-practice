# Challenge 17: NexCure Quick Command System ⚡
# command = input("Enter the command: ").lower()

# match command:
#     case "bill":
#         print("opening billing  module  ")



#     case "stock"|"inventory":
#         print("Checking Medicine Stock... 💊")

#     case "return":
#         print("Opening Expiry & Returns Module... 🔄")
#     case _:
#         print("Invalid Command! Type bill, stock, or return. 🛑")


# Challenge 18: NexCure Patient Triage (Check-up) System 🏥
patient_type = input("what kind of persion you have ").lower()

match patient_type:
    case "emergency" | "urgent":
        print("🚨 Turant ICU bed ready karo!")
    case "vip"|"staff":
        print("Private ward book ho gaya hai. 🛏️")
    case "opd":
        opd = "temp"
        temp = float(input("Patient ka temperature batao: "))
        if temp < 99:
            print("Patient normal hai, dawai de do.")
        elif 99 <= temp <= 102:
            print("Fever hai, doctor ko dikhao.")
        elif temp > 102 :
            print("High fever! Turant injection lagao! 💉")

    case _:        
     print("Galat category! Sahi option daalein.")
