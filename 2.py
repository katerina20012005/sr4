# Заданы два массива А и В (размерность массива задается пользователем с клавиатуры,
# сами элемента массива либо вводятся с клавиатуры, либо генерируются случайно) .
# Написать программу, которая вывод на экран элементы, общие для А и В (содержатся в обоих массивах).

n = int(input("Размерность массива a: "))
a = [0] * n
for i in range(n):
    print("a[", i, "]=", sep = "", end = "")
    a[i] = int(input())

n = int(input("Размерность массива b: "))
b = [0] * n
for i in range(n):
    print("b[", i, "]=", sep = "", end = "")
    b[i] = int(input())

print(set(a) & set (b))


