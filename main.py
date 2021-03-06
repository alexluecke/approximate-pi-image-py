import Image
import argparse

def calc_pi(filename):
    try:
        img = Image.open(filename)
    except:
        print "Couldn't open image."

    area = 0

    rgb_img = img.convert('RGB')
    rgb_values = rgb_img.load()
    (width, height) = rgb_img.size

    is_black = lambda (r,g,b): r==0 and g==0 and b==0

    # Circles are symmetric so I can use the y-diameter from the min and max
    # of the x-coords to calculate the radii.
    min_point_x, max_point_x  = (width, height), (0, 0)

    # Scan down instances of black pixels to store max, mins, and area.
    for x in range(width):
        for y in range(height):
            if is_black(rgb_values[x,y]):
                if x < min_point_x[0]:
                    min_point_x = (x,y)
                if x > max_point_x[0]:
                    max_point_x = (x,y)
                area += 1

    radius = (max_point_x[0] - min_point_x[0])/2

    return float(area)/float(radius*radius)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-f','--filename', help='Input file name', required=True)
    args = parser.parse_args()
    print calc_pi(args.filename)
