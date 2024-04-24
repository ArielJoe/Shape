import square
import triangle
import hollow

def main():
    n = int(input('size : '))

    square.starSquare(n)
    square.numberSquare(n)
    square.starFrame(n)
    square.starWindow(n)
    square.rhombusWindow(n)

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

    hollow.pyramid(n)
    hollow.rTriangle(n)
    hollow.lTriangle(n)
    hollow.rDownwardTriangle(n)
    hollow.lDownwardTriangle(n)
    hollow.doubleHill(n)
    hollow.reversePyramid(n)
    hollow.butterfly(n)
    hollow.diamond(n)
    hollow.sandglass(n)
    hollow.lPascalTriangle(n)
    hollow.rPascalTriangle(n)

if __name__ == '__main__':
    main()