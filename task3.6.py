# Задание 6

def capitalize(arg):
    small_letter = arg[0]
    big_letter = chr(ord(small_letter) - ord('a') + ord('A'))
    return big_letter + arg[1:]

li = input("Введите слова через пробел:").split()
res = []
for el in li:
    res.append(capitalize(el))
print(' '.join(res))

# другой способ, но не получается пробелы вернуть
li1 = input("Введите слова через пробел:").split()
print(','.join(li1).title())
