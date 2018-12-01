freq = 0
freqs = set()

while True:
    f = open('input.txt')

    for line in f:
        freq = freq + int(line.strip())
        if freq in freqs:
            print("Frequency: " + str(freq))
            exit(0)
        else:
            freqs.add(freq)

    f.close()
