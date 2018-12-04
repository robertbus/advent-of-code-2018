# Claim holder class
class Claim:
    def __init__(self, claim_str):
        claim_parts = claim_str.split()

        self.id = claim_parts[0]

        claim_xy = claim_parts[2].replace(":", "").split(",")
        self.x = int(claim_xy[0])
        self.y = int(claim_xy[1])

        claim_area = claim_parts[3].split("x")
        self.width = int(claim_area[0])
        self.height = int(claim_area[1])

        self.intact = True

    def __str__(self):
        return "Claim " + self.id + \
               " starts at " + str(self.x) + ", " + str(self.y) + \
               " and has a size of " + str(self.width) + ", " + str(self.height) + "."


# read input
with open('input.txt') as file:
    lines = [line.strip() for line in file]
    file.close()


# init
claims = [Claim(line) for line in lines]

w, h = 1000, 1000
fabric = [[0 for x in range(w)] for y in range(h)]


# part 1
for claim in claims:
    for i in range(claim.x, claim.x + claim.width):
        for j in range(claim.y, claim.y + claim.height):
            fabric[i][j] += 1

overbooked_fabric = 0

for i in range(w):
    for j in range(h):
        if fabric[i][j] > 1:
            overbooked_fabric += 1

print("Overbooked fabric area: " + str(overbooked_fabric))


# part 2
for claim in claims:
    for i in range(claim.x, claim.x + claim.width):
        for j in range(claim.y, claim.y + claim.height):
            if fabric[i][j] != 1:
                claim.intact = False
                break

for claim in claims:
    if claim.intact:
        print("Intact claim ID: " + claim.id)
        break
