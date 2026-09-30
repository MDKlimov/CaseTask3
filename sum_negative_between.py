# Сумма отрицательных элементов между максимальным и минимальным элементами массива.

n = int(input("Введите количество элементов массива N: "))
if n <= 0:
    raise ValueError("Размер массива должен быть положительным.")

A = list(map(int, input(f"Введите {n} целых чисел через пробел: ").split()))
if len(A) != n:
    raise ValueError(f"Требуется ввести ровно {n} элементов.")

max_index = A.index(max(A))
min_index = A.index(min(A))

left = min(max_index, min_index) + 1
right = max(max_index, min_index)

result = 0
for i in range(left, right):
    if A[i] < 0:
        result += A[i]

print("Сумма отрицательных элементов между максимумом и минимумом:", result)
