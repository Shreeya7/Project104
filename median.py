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

n = len(new_data)
new_data.sort()

if n % 2 == 0 :
    median1 = float(new_data[n//2])

    median2 = float(new_data[n//2-1])

    median = (median1 + median2)/2

else :
    median = new_data[n//2]

print("Median of the heights is : " + str(median))
