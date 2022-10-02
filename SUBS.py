
string = 'GATATATGCATATACTT'
substring = 'ATAT'

start = 0
start_indices = []
while True:
    start = string.find(substring, start)
    if start == -1:
        break
    start_indices.append(start + 1)
    start += 1

for index in start_indices:
    print(index, end=' ')
