f = open('input.txt')

freq = 0

for line in f:
    freq = freq + int(line.strip())

print("Frequency: " + str(freq))
