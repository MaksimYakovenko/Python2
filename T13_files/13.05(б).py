f = open("input.txt") 
content = f.readline() 
counter = 0 
 
for line in f: 
    num= int(line)**0.5
    if int(line) > 0 and num % 2 != 0 and num**2==int(line):
        counter += 1 
         
print(counter) 
f.close()
