#Вариант 29.Даны числа х, у, x1, y 1, х2, у2. Проверить истинность высказывания: «Точка с
#координатами (х, у) лежит внутри прямоугольника, левая верхняя вершина которого
#имеет координаты (х1, у1), правая нижняя — (х2, у2), а стороны параллельны
#координатным осям».
x = input ("введите число x=")
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("ошибка нужно ввести число")
        x = input("введите число")
y = input ("введите число y=")
while type(y) != float:
    try:
        y = float(y)
    except ValueError:
        print("ошибка нужно ввести число")
        y = input("введите число")
x1 = input ("введите число x1=")
while type(x1) != float:
    try:
        x1 = float(x1)
    except ValueError:
        print("ошибка нужно ввести число")
        x1 = input("введите число")
y1 = input("введите число y1=")
while type(y1) != float:
            try:
                y1 = float(y1)
            except ValueError:
                print("ошибка нужно ввести число")
                y1 = input("введите число")
y2 = input("введите число y2=")
while type(y2) != float:
    try:
        y2 = float(y2)
    except ValueError:
        print("ошибка нужно ввести число")
        y2 = input("введите число")
x2 = input ("введите число x2=")
while type(x2) != float:
    try:
        x2 = float(x2)
    except ValueError:
        print("ошибка нужно ввести число")
        x2 = input("введите число.")
if x1 <= x <= x2 and y2 <= y <= y1:
    print("\nИстина: точка лежит внутри прямоугольника (или на его границе).")
else:
    print("\nЛожь: точка лежит вне прямоугольника.")
