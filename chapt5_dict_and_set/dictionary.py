d={}       #empty dictionary

chai_types = {"Masala": "Spicy","Ginger":"Zesty","Green":"mild"}

print(chai_types)
print(chai_types["Masala"])
print(chai_types.get("Ginger"))

chai_types["Green"]="Fresh"
print(chai_types)

# for accessing the key and value 
for chai in chai_types:
    print(chai,chai_types[chai])

for key,value in chai_types.items():
    print(key,value)

if "Masala" in chai_types:
    print('I have masala chai')

print(len(chai_types))

chai_types["earl Grey"] = "Citrus"
print(chai_types)

chai_types.pop("Ginger")       #only pop ka sath to attribute matlab batana padega ky hatana hai 
print(chai_types)

chai_types.popitem()    #ismai last mai se automatic hat jata hai jab popitem deta hai
print(chai_types)

#dict in dict / Nested dict 
tea_shop ={"chai": {"masala":"spicy","Ginger":"Zesty"},"biscuit":{"parle": "sweet","monako":"spicy"}}
print(tea_shop)
# print(tea_shop["biscuit"])
# print(tea_shop["chai"]["Ginger"])

squared_num = {x:x**2 for x in range(6)}
print(squared_num)
squared_num.clear()
print(squared_num)

