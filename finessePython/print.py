l = ['hat', 'scarf', 'socks']

print(l)

f = open('temp.txt', 'w')

for element in l:
    f.write(element + "\n")

f.close()