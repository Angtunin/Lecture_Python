# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') #вариант 1
# data.writelines(colors)
# data.close()

# вариант 2
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')