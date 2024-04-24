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

def rhombusWindow(n):
    space = n - 2
    star = 1
    for i in range(n * 2 - 3):
        for j in range(space):
            print(end='  ')
        for k in range(star):
            if k == 0 or k == star - 1 or i == n - 2 or k == star // 2:
                print(end='* ')
            else:
                print(end='  ')
        if i < (n * 2 - 3) // 2:
            space -= 1
            star += 2
        else:
            space += 1
            star -= 2
        print()
    print()