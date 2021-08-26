import csv 

# Opening the file
with open("height-weight.csv" , newline = "") as f :
    reader = csv.reader(f)
    file_data = list(reader)

# Removing the first row of headers(0th line)
file_data.pop(0)

new_data = []

# Creating a for loop for pushing each value of heights into variable num
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

# Getting how many elements are present in the data list
n = len(new_data)

total = 0

# Creating a for loop to add all values
for x in new_data:
    total += x
    print(total)

# Formula of mean
mean = total / n

print("Mean of the heights is : " + str(mean))

