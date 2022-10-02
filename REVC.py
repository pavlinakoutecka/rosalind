
string = "AAAACCCGGT"
string = list(string)


for idx, letter in enumerate(string):
    if letter == 'A':
        string[idx] = 'T'
    elif letter == 'T':
        string[idx] = 'A'
    elif letter == 'C':
        string[idx] = 'G'
    elif letter == 'G':
        string[idx] = 'C'

for idx in range(len(string)-1, -1, -1):
    print(string[idx], end='')
