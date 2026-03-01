# # Q1 Write a program to print Twinkle twinkle little star poem in python
# print('''TWINKLE, TWINKLE, LITTLE STAR
# Twinkle, twinkle, little star, 
# how I wonder what you are. 
# Up above the world so high,
# like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# how I wonder what you are.
# When the blazing sun is set
# and the grass with dew is wet.
# Then you show your little
# light, twinkle, twinkle all the night. 
# Twinkle, twinkle little star, how I wonder what you are.
# Then the traveler in the dark thanks you for your tiny spark. 
# How could he see where to go if you did not twinkle so?
# Twinkle, twinkle little star, how I wonder what you are.
# As your bright and tiny spark lights the traveler in the dark, 
# though I know not what you are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')


# #Q2 Use REPL and print the table of 5 of using it 
# ##iska ans to ya tha terminal mai jakar manualy 5 ki table print ki 

# #Q3 install and external module and use it to perform an operation of your interest
# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("I will speak this text")
# engine.runAndWait()


#write a python program to print the contents of a directory using the os module 
#search online for the function which does that 
import os
#here r is used as row string otherwise compiler give error
#select the directory path
path = r"C:\Users\priya\OneDrive\Desktop\fresh start python"

#use the os module to list the directory
contents = os.listdir(path)

for item in contents:
    print(item)



