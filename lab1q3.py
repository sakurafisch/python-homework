if __name__ == '__main__':
    matrix: list = [
        [4, "Tetrahedron", 4],
        [6, "Cube", 8],
        [8, "Octahedron", 6],
        [12, "Dodecahedron", 20],
        [20, "Icosahedron", 12]
    ];
    print("{0:>10}{1:^30}{2:<10}".format("Faces", "Name", "Vertices"));
    for face, name, vertice in matrix:
        print("{0:>10}{1:^30}{2:<10}".format(face, name, vertice));

# 张婷答案
# print("{0:>10}{1:^30}{2:<10}".format("Faces","Name","Vertices"))
# print("{0:>10}{1:^30}{2:<10}".format(4, "Tetrahedron", 4))
# print("{0:>10}{1:^30}{2:<10}".format(6, "Cube", 8))
# print("{0:>10}{1:^30}{2:<10}".format(8, "Octahedron", 6))
# print("{0:>10}{1:^30}{2:<10}".format(12, "Dodecahedron", 20))
# print("{0:>10}{1:^30}{2:<10}".format(20, "Icosahedron", 12))