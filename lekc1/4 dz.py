# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1 способ
X=[3,4,56,100,15,2,20,30]
a=1
for x in X:
    if x % 3 == 0:
        if x % 5 == 0:
            #print('перемножаемые эл-ты',x)
            a = x * a
print('Итоговое значение',a)

