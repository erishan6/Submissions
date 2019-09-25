import argparse
from PIL import Image, ImageStat

def convert_level(val):
    val = (val*10)/255
    return round(val,2)

def brightness_level(im_file):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    return convert_level(stat.mean[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', required=True, help='Path to input image')
    args = parser.parse_args()
    file = args.input_image
    z = brightness_level(file)
    print(z)
