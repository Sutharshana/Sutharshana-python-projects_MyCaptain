#print positive numbers in a range

x = int(input("enter a starting number: "))
y = int(input("enter a ending number: "))
for num in range(x, y):
	if (num >= 0):
		print("Positive number is: ", num)
		
#print positive numbers in a list

list = [12,32,-3,-21,2,-8,1]
print(list)
positive_no = [num for num in list
	if num >= 0]
print("positive numbers :" ,*positive_no)
