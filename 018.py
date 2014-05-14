# triangles are represented as matrices
# A cell has coordinates (row, column)
# each cell (i, j) has two 'adjacent' cells at (i + 1, j) and (i + 1, j + 1)

# We suppose that cell values are positive

FILEPATH = "018_bigTriangle.txt"


def triangleFromString(string):
    tri = []
    string.strip()
    rows = string.split("\n")
    rows = [row for row in rows if len(row) > 0]  # filter empty rows
    for row in rows:
        triRow = []
        cells = row.split(" ")
        for cell in cells:
            triRow.append(int(cell))
        tri.append(triRow)
    return tri


def triangleFromFile(filepath):
    with open(filepath) as f:
        triString = f.read()
    return triangleFromString(triString)

tri = triangleFromFile(FILEPATH)
height = len(tri)
known_max_length = []
for i in range(height):
    known_max_length.append([0] * (i + 1))

known_max_length[0][0] = tri[0][0]
current_max = 0

for i, row in enumerate(tri[:-1]):
    for j, cellValue in enumerate(tri[i]):
        belowLeft = (i + 1, j)
        belowRight = (i + 1, j + 1)
        for belowI, belowJ in (belowLeft, belowRight):
            belowValue = tri[belowI][belowJ]
            candidateLength = known_max_length[i][j] + belowValue
            if candidateLength > known_max_length[belowI][belowJ]:
                known_max_length[belowI][belowJ] = candidateLength
            if candidateLength > current_max:
                current_max = candidateLength

print(current_max)
