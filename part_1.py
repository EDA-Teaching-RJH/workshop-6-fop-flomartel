##task 1.1
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(sample_bay[0]) ##prints first item in list

print(sample_bay[len(sample_bay)-1])##prints last item in list

list_length = len(sample_bay)
print(list_length)##prints the number of items in the list

##task 1.2
for list in sample_bay:
    print("Transmitting data for:" , list)##prints "Transmitting data for:" then each item in the list

##task.1.3
new_findings = []
##for i in range(len(new_findings)):
user1 = input("Please enter a rock type: ")
user2 = input("Please enter a rock type: ")
user3 = input("Please enter a rock type: ")
new_findings.append(user1)
new_findings.append(user2)
new_findings.append(user3)
print(new_findings)

##task 1.4

