import time

def countdown(user_input=10):
    if user_input <= 0:
        print("Value must be positive.")
    else:
        print("Countdown is started.")
        while user_input >= 0:
            minutes = user_input // 60
            seconds = user_input % 60
            print(f"Remaining time: {minutes:02d} : {seconds:02d}", end="\r")
            time.sleep(1)
            user_input -= 1
        print("Countdown Finished...!")

if __name__ == "__main__":
    countdown()  # Calls the countdown function with the default value of 10
