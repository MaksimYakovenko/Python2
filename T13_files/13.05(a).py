f = open("input.txt") 
content = f.readline() 
counter = 0 
 
for line in f: 
    if int(line) % 2 == 0: 
        counter += 1 
         
print(counter) 
f.close()
