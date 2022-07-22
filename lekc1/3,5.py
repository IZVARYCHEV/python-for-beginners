# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#замена строк х на у

#исходная строка asdxfghyxyx
#заменить буквы х на у
X="asdxfghyxyxx"
Y=""
for	x in X:
	if x == "x":
		Y +="y"
	else:
		Y +=x

print('Исходная строка:',X)
print('Измененная строка:',Y)

#замена строк х на у без дополнительной
str1 = 'asdxfghyxyxx'
str2 = str1.replace('x','y')
print(str1, str2)
