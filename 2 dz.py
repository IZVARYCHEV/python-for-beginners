# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1 способ
X=[3,4,56,100,2,2,3]
a=0
c=len(X)

for x in X:
    a = x + a
    #print(a)

print('Итоговое значение',a/c)

#2 способ
X=[3,4,56,100,2,2,3]
a=sum(X)
c=len(X)

print(a/c)