# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1 способ
X = sum(range(0, 88888888))
print(X)

# 2 способ
X = list(range(0, 88888888))
a = 0
for x in X:
    a = x + a
    print(a)
print('Итоговое значение', a)
