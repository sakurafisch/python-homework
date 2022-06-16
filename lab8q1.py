def main() -> None:
    ans: list[tuple] = []
    stu: list[str] = []
    filename: str = input('Enter student file name: ')
    order: list[str] = ['1st', '2nd', '3rd']
    column_length: list[int] = []
    for i in range(0, 3):
        column_length.append(int(input(f'Enter {order[i]} column length: ')))
    with open(filename, 'r') as file:
        i: int = 0
        for line in file:
            if line == '\n':
                continue
            # stu.append(line.split('\n')[0])
            stu.append(line.rsplit()[0])
            i += 1
            if i % 3 == 0:
                ans.append(tuple(stu))
                stu.clear()
    print(f"{'Student Number':>{column_length[0]}}{'First Name':>{column_length[1]}}{'Last Name':>{column_length[2]}}")
    for a in ans:
        print(f"{a[0]:>{column_length[0]}}{a[1]:>{column_length[1]}}{a[2]:>{column_length[2]}}")

if __name__ == '__main__':
    main()


# 张婷答案
# file_path: str = input('Enter student file name: ')
# column_length1 = int(input(('Enter 1st column length: ')))
# column_length2 = int(input(('Enter 2nd column length: ')))
# column_length3 = int(input('Enter 3rd column length: '))
# print(f"{'Student Number':>{column_length1}}{'First Name':>{column_length2}}{'Last Name':>{column_length3}}")
# with open(file_path, 'r') as file:
#     i: int = 0
#     for line in file:
#         i = i + 1
#         if i % 3 == 0:
#             print(f"{line.rstrip():>{column_length3}}")
#         if i % 3 == 1:
#             print(f"{line.rstrip():>{column_length1}}", end="")
#         if i % 3 == 2:
#             print(f"{line.rstrip():>{column_length2}}", end="")

