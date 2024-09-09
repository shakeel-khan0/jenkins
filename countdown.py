import time

try:
    user_input = 10  #int(input("Enter time (in seconds): "))
    if user_input <= 0:
        print("Value must be posotive.")
    else:
        print("Countdown is started. ")
        while user_input >= 0:
            minutes = user_input // 60
            seconds = user_input % 60
            print(f"Remaining time: {minutes:02d} : {seconds:02d}", end="\r")
            time.sleep(1)
            user_input -= 1
        print("Countdown Finished...!")
except ValueError:
    print("Invalid input..! Try to enter a valid input.")