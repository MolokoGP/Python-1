#Loops

#Using a while loop to count from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1 # Increments the count by 1

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break # Exits the loop when the count is reached 3