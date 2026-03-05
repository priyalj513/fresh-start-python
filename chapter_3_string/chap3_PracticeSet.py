# #WAP to display a user entered name followed by Good Afternoon using input() function
# name=input("enter your name: ")
# print(f"Good Afternnon {name} ")


#Q2 WAP to fill n a letter template given below with name and date.
# letter='''Dear <|Name|>,
# you are selected!
# <|Date|>'''

# print(letter.replace("<|Name|>","Priyal").replace("<|Date|>","15 March 2026"))



#Q3WAP to detect double space in a strng   
# name="my name is  priyal"
# print(name.find("  "))      #find func is used to find the index value of string

# #Q4 Replace the double space from que3 with single space
# name="my name is  priyal  and  i want to become  sof eng"
# print(name.replace("  "," "))      #dhar dusra memory ref mai change hua ha only
# print(name)    #idhar name strng change nhi hui hai bec it is mmutable

#Q5 WAP to format the following letter using espace seq charactres
#letter="Dear Harry, this python course is nice. Thanks!"

letter="Dear Harry,\n\t this python course is nice.\n Thanks!"
print(letter)



