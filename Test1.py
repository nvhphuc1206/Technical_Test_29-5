# Question 1:
dna = "CCCTACTTCACTCCAGTACTATAGTAGTAGCTGGGGTTTTCTTACTTATTCGCTTCCACCCACCAATAGAAAATAATACAACAATTCAAAGTCTTACACTATGCCTAGGAGCTATTACTACCATATTCATAGCAATCTGCGCCCTAACACAAAATGACATTAAAAAAATTGTAGCCTTCTCTACCTCAA"
base_counts = { "A" : dna.count("A"),
                "C" : dna.count("C"),
                "G" : dna.count("G"),
                "T" : dna.count("T")}

import matplotlib.pyplot as plt
x = list(base_counts.keys())
y = list(base_counts.values())
plt.bar(x,y)
plt.xlabel('Base')
plt.ylabel('Count')
plt.show()
plt.savefig("Question1.png")



# Question 2:
def reverse_complement(x):
    base_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for i in reversed(x):
        complement_base = base_pairs[i]
        result += complement_base
    return result


seq = "CAACTGTCGTTTTCTCAACTAATAAAAATTTATTTCACACACCACCCTTGACACCTCCACCCACCTCTTCTTTCCCATAATCCCCAAAGATGGTATCATAATACCCATTATT"
target_seq = reverse_complement(seq)
print(target_seq)




# Question 3:
ref = "CGCCCATATCACTCGAGACGTAAACTACGGCTGAATTATCCGCTACCTTCATGCCAATGGTGCCTCCATATTCTTTATCTGC"
dna3 = "CGCCCATACCACTCGAGACGTAAACTACGGCTGAAATATCCGCTACCTTCATGCCAATGGTGCGTCCATATTCTTTATCTGC"

dif = 0
for x,y in zip(ref, dna3):
    if x != y:
        dif += 1
print("So diem khac biet giua 2 trinh tu la : ",dif)
for i, (x, y) in enumerate(zip(ref, dna3)):
    if x != y:
        print(i," : ", x, " : ", y)
