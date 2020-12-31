def split_str(str, str_size):
    return [str[i:i+str_size] for i in range(0, len(str), str_size)]

strn = split_str(str(input("Enter codon: ").upper()).split('AUG')[1], 3)
codon = ''
let = []
a_acid = []

f = open('table.txt', 'r')

for line in f:
    data = line.split()
    let.append(data[0])
    a_acid.append(data[1])

for c in strn:
    newC = ''
    if c in let:
        newC = a_acid[let.index(c)]
    codon += newC + ' '

print("Met " + codon.split("Stop")[0])
f.close()