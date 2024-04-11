import square
import triangle

def main():
    n = 5

    square.starSquare(n)
    square.numberSquare(n)
    square.starFrame(n)
    square.starWindow(n)

    triangle.pyramid(n)
    triangle.rTriangle(n)
    triangle.lTriangle(n)
    triangle.rDownwardTriangle(n)
    triangle.lDownwardTriangle(n)
    triangle.doubleHill(n)
    triangle.reversePyramid(n)
    triangle.butterfly(n)
    triangle.diamond(n)
    triangle.sandglass(n)
    triangle.lPascalTriangle(n)
    triangle.rPascalTriangle(n)

if __name__ == '__main__':
    main()