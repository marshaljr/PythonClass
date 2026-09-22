items = ["apple", "banana", "orange", "apple", "mango"]
seen = []

for item in items:
    if item in seen:
       print(f"{item} is already in the list.") 
       break
    else:
        seen.append(item)
        
print(seen)
