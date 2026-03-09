# import random
Device = 180
# Device = random.randint(0, 200)
print("Enter the number betweeen 0 - 200")
attempts = 0
while attempts < 5:
    try:
        user_input  = int(input())
        attempts += 1 
        if user_input > Device:
            print(f"Enter Smaller number than {user_input}")
        elif user_input < Device:
            print(f"Enter Larger number than {user_input}")
        else:
            print(f"You guess the number at {attempts} iteration!")
            break

    except ValueError:
        print("Invalid Input, kindly enter correct value")

