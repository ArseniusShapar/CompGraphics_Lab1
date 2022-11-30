from PIL import Image, ImageDraw


def transform(point):
    return point[1], -point[0] + 540


def main():
    with open('DS8.txt', 'r') as file:
        lines = file.readlines()

    pointList = []
    for line in lines:
        coords = line.strip().split(' ')
        x = int(coords[0])
        y = int(coords[1])
        point = (x, y)
        pointList.append(transform(point))

    image = Image.new('1', (960, 540))
    draw = ImageDraw.Draw(image)
    for point in pointList:
        draw.point(point, fill='white')
    image.save('result.png', 'PNG')


if __name__ == '__main__':
    main()
