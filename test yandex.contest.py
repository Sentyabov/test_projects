a, b = input(), input()
count = 0
new_word = ''
for i in a:
    for j in a:
        if i not in new_word:
            new_word += i
for i in b:
    for j in a:
        if i == j:
            count += 1
            break
print(count)
