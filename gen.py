from PIL import Image
import os
import sys
import imageio
from images2gif import writeGif

def main(sheet, row_num, col_num, total, duration):
    im = Image.open(sheet)
    print im.size
    w, h = im.size
    w_offset = w/col_num
    h_offset = h/row_num
    print w_offset, h_offset
    images = []
    names = [total-1] + range(total-1)
    idx = 0
    for i in range(row_num):
        for j in range(col_num):
            print idx
            if idx >= total:
                break
            bbox = (j*w_offset, i*h_offset, j*w_offset + w_offset, i*h_offset + h_offset)
            print bbox
            cropped = im.crop(bbox)
            cropped.save("frames-%d.png" % names[idx])
            idx += 1
    for i in range(total):
        images.append(Image.open("frames-%d.png" % i))
    os.system("convert -resize 100x100  -delay %s -loop 0 frames-*.png -alpha remove -dispose Background animated.gif"%duration)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))