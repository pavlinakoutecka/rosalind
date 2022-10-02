
def hamming_distance(s, t):
    hd = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hd += 1
    return hd


s = 'GTTTCAACCTCTGTAGGTTTGGTTCC'
t = 'GCTCCCCCCACTGAGGGTCCGGTGAG'
print(hamming_distance(s, t))

