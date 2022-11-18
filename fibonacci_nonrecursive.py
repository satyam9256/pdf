first_num = int(input("Enter the first number "))  # 0
second_num = int(input("Enter the second number "))  # 1
num_of_terms = int(input("Enter the number of terms "))

print(first_num, second_num)
print("The numbers in fibonacci series are : ")

while num_of_terms - 2 != 0:
    third_num = first_num + second_num
    print(third_num)
    first_num, second_num = second_num, third_num
    num_of_terms -= 1 #decrease the no of terms variable by 1
