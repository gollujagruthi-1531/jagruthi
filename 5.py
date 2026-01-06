num_1 = input("ENTER FIRST NUMBER: ")
num_2 = input("ENTER SECOND NUMBER:")

num_1 = int(num_1)
num_2 = int(num_2)

print("Sum:", num_1 + num_2)
print("Difference:", num_1 - num_2)
print("Product:", num_1 * num_2)

if num_1 > num_2:
    print(num_1, "IS BIGGER THAN", num_2)
elif num_1 < num_2:
    print(num_2, "IS BIGGER THAN",num_1)
else:
    print("BOTH ARE EQUAL")
