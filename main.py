listA = []
listB = []
with open('imput.txt', 'r') as f:
    for line in f:
        a, b = map(int, line.split())
        listA.append(a)
        listB.append(b)

listA.sort()
listB.sort()

counting = 0

for i in range(len(listA)):
    counting += abs(listA[i]-listB[i])

print(counting)

counting = 0
for i in range(len(listA)):
    counting += listA[i]*listB.count(listA[i])
print(counting)