# multithreading = used to perform multiple tasks concurrently (multitasking)
# good for I/O boundtasks like reading files or fetching data from API's
# threading.Thread(target=my_function) 

import threading
import time

def walk_dog(first_name):
    time.sleep(8)
    print(f"You finish walking {first_name}!")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail(first, last):
    time.sleep(4)
    print(f"{first} {last} get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby",)) # pass the tuple as an argument and end with , if there is only one argument
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail, args=("John", "Matis"))
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("All chores are complete!")