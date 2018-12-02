countOfDoubleChars = 0
countOfTripleChars = 0


def contains(value, dictionary):
    for v in dictionary.values():
        if v == value:
            return True
    return False


with open('input.txt') as file:
    for line in file:
        counts = dict()

        for letter in line.strip():
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1

        if contains(2, counts):
            countOfDoubleChars += 1

        if contains(3, counts):
            countOfTripleChars += 1

    file.close()

    print(str(countOfDoubleChars * countOfTripleChars))
