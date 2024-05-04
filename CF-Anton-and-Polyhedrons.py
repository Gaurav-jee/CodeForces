t = int(input())

sumOfFaces = 0
ShapeFaceCount = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}

for _ in range(t):
    polyhedron = input()
    sumOfFaces += int(ShapeFaceCount.get(polyhedron))

print(sumOfFaces)
