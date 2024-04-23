def pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(end=' ')
        for k in range(i):
            if i == n or k == 0 or k == i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()

def rTriangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            if i == n or j == 0 or j == i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()

def lTriangle(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(end='  ')
        for k in range(i):
            if i == n or k == 0 or k == i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()

def rDownwardTriangle(n):
    for i in range(n):
        for j in range(n - i):
            if i == 0 or j == 0 or j == n - i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()

def lDownwardTriangle(n):
    for i in range(n):
        for j in range(i):
            print(end='  ')
        for k in range(n - i):
            if i == 0 or k == 0 or k == n - i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    print()

def doubleHill(n):
    for i in range(1, n + 1):
        for j in range(2):
            for k in range(n - i):
                print(end=' ')
            for k in range(i):
                if i == n or k == 0 or k == i - 1:
                    print(end='* ')
                else:
                    print(end='  ')
            for k in range(n - i):
                print(end=' ')
        print()
    print()

def reversePyramid(n):
    for i in range(n):
        for j in range(i):
            print(end=' ')
        for k in range(n - i):
            if i == 0 or k == 0 or k == n - i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()

def butterfly(n):
    for i in range(n - 1):
        for j in range(i):
            if j == 0 or j == i - 1:
                print(end='* ')
            else:
                print(end='  ')
        for j in range(n - i - 2):
            print(end='  ')
        for j in range(n - i - 1):
            print(end='  ')
        for j in range(i):
            if j == 0 or j == i - 1:
                print(end='* ')
            else:
                print(end='  ')
        print()
    for i in range(n * 2 - 3):
        if i == 0 or i == n * 2 - 3 - 1 or i == (n * 2 - 3) // 2:
            print(end='* ')
        else:
            print(end='  ')
    print()
    for i in range(n - 1):
        for j in range(n - 2 - i):
            if j == 0 or j == n - i - 3:
                print(end='* ')
            else:
                print(end='  ')
        for j in range(i + 1):
            print(end='  ')
        for j in range(i):
            print(end='  ')
        for j in range(n - 2 - i):
            if j == 0 or j == n - i - 3:
                print(end='* ')
            else:
                print(end='  ')
        print()

def diamond(n):
    space = n - 2
    star = 1
    for i in range(1, n * 2 - 1):
        for j in range(space):
            print(end=' ')
        for j in range(star):
            if j == 0 or j == star - 1:
                print(end='* ')
            else:
                print(end='  ')
        if i <= (n * 2 - 3) // 2:
            space -= 1
            star += 1
        else:
            space += 1
            star -= 1
        print()

def sandglass(n):
    space = 0
    star = n - 1
    for i in range(1, n * 2 - 2):
        for j in range(space):
            print(end=' ')
        for j in range(star):
            if i == 1 or i == n * 2 - 3 or j == 0 or j == star - 1:
                print(end='* ')
            else:
                print(end='  ')
        if i <= (n * 2 - 3) // 2:
            space += 1
            star -= 1
        else:
            space -= 1
            star += 1
        print()
    print()

def lPascalTriangle(n):
    star = 1
    for i in range(n * 2 - 3):
        for j in range(star):
            if j == 0 or j == star - 1:
                print(end='* ')
            else:
                print(end='  ')
        if i < (n * 2 - 3) // 2:
            star += 1
        else:
            star -= 1
        print()
    print()

def rPascalTriangle(n):
    star = 1
    space = n - 2
    for i in range(n * 2 - 3):
        for j in range(space):
            print(end='  ')
        for j in range(star):
            if j == 0 or j == star - 1:
                print(end='* ')
            else:
                print(end='  ')
        if i < (n * 2 - 3) // 2:
            star += 1
            space -= 1
        else:
            star -= 1
            space += 1
        print()
    print()