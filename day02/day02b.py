# All functions depend on that all strings are of same length, no checks are performed.


def is_similar(str1, str2):
    diff = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1

            if diff > 1:
                return False

    return True


def common(str1, str2):
    common_parts = ""

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            common_parts += str1[i]

    return common_parts


with open('input.txt') as file:
    lines = [line.strip() for line in file]
    file.close()

l = len(lines)

for i in range(l):
    for j in range(i+1, l):
        if is_similar(lines[i], lines[j]):
            print(common(lines[i], lines[j]))
