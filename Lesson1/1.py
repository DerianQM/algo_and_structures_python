# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

cl = int(input("Введите 3-ч значное число"))
print (f"Произведение чисел числа равно {(cl//100)*(cl%100//10)*(cl%100%10)}")
print (f"Сумма чисел числа равно {(cl//100)+(cl%100//10)+(cl%100%10)}")