import random  
import time 
import os

print("""
   _____ _                                 
  / ____| |                                
 | (___ | |_ _ __ ___ _   _ _ __ ___ _   _ 
  \___ \| __| '__/ _ \ | | | '__/ _ \ | | |
  ____) | |_| | |  __/ |_| | | |  __/ |_| |
 |_____/ \__|_|  \___|\__, |_|  \___|\__, |
                       __/ |          __/ |
                      |___/          |___/ 
""")

print("Nitro Gen Made by Streyrey")

file = open("Codes.txt", "w")
upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letter = "abcdefghijklmnioqrstuvwxyz"
digits = '0123456789'

upper, lower, nums, = True, True, True,

all = ""

if upper:
    all += upper_letter
if lower:
    all += lower_letter
if nums:
    all += digits

length = 16

amount = int(input("How many Discord Nitro codes you want: "))
for x in range(amount):
    gen = "".join(random.sample(all, length))
    file.write("https://discord.gift/" + gen + "\n")

print("Codes done")
print("This window will close automatically in 5 seconds.")


time.sleep(5)
os.system("taskkill /f /im cmd.exe")