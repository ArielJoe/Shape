def starSquare(n):
    for i in range(n):
        for j in range(n):
            print(end='* ')
        print()
    print()

def numberSquare(n):
    for i in range(1, n + 1):
        for j in range(n):
            print(i, end=' ')
        print()
    print()

def starFrame(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print(end='* ')
            elif j == 0 or j == n - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()

def starWindow(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or i == n // 2:
                print(end='* ')
            elif j == 0 or j == n - 1 or j == n // 2:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()