# Challenge 17: NexCure Quick Command System ⚡
command = input("Enter the command: ").lower()

match command:
    case "bill":
        print("opening billing  module  ")



    case "stock"|"inventory":
        print("Checking Medicine Stock... 💊")

    case "return":
        print("Opening Expiry & Returns Module... 🔄")
    case _:
        print("Invalid Command! Type bill, stock, or return. 🛑")