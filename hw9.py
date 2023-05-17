class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_perimeter(self):
        length = abs(self.x2 - self.x1)
        width = abs(self.y2 - self.y1)
        return 2 * (length + width)

    def get_area(self):
        length = abs(self.x2 - self.x1)
        width = abs(self.y2 - self.y1)
        return length * width

x1 = float(input("직사각형의 좌측 상단 꼭짓점의 x 좌표를 입력하세요: "))
y1 = float(input("직사각형의 좌측 상단 꼭짓점의 y 좌표를 입력하세요: "))
x2 = float(input("직사각형의 우측 하단 꼭짓점의 x 좌표를 입력하세요: "))
y2 = float(input("직사각형의 우측 하단 꼭짓점의 y 좌표를 입력하세요: "))

rectangle = Rectangle(x1, y1, x2, y2)

perimeter = rectangle.get_perimeter()
area = rectangle.get_area()

print("둘레:", perimeter)
print("넓이:", area)
