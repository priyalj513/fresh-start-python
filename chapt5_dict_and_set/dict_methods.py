marks={"harry":100,"Shubham":56,"rohan":23}
print(marks)
print(marks.items())
print(marks.keys())
print(marks.values())


marks.update({"harry":99,"Renuka":80})   #update method se jo hai vo to update ho jaiga aur jo nhi hai vo add ho jaiga 
print(marks)

print(marks.get("Harry"))     #print none 
print(marks["Harry"])         #return an error