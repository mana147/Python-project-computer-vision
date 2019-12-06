array_num = []

for int_num in range(2000, 3201):
    if (int_num % 7 == 0) & (int_num % 5 != 0):
           array_num.append(int_num)

print (array_num)