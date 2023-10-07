# your code goes here!
import time
def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        if number == 0:
            print('HAPPY NEW YEAR!')
            break
        
countdown (10)            
def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
        if number == 0:
            print('HAPPY NEW YEAR!')
            break

countdown_with_sleep(10)
            