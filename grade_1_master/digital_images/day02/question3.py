import numpy as np

from copy import deepcopy
from random import choice
from PIL import Image, ImageEnhance

'''
3. 对一副图像加噪声，进行平滑，锐化作用。
'''

def part_one():
    """
    对一副图像加噪声
    """
    with open("source2.jpeg", "rb") as fp:
        im = Image.open(fp).convert("L")
        im.show()
        im.save("gray_source2.jpeg")

        im_arr = np.asarray(im)
        im_converted_arr = deepcopy(im_arr)
        for i, m in enumerate(im_arr):
            for j, n in enumerate(m):
                if n % 5 == 0:
                    im_converted_arr[i][j] = choice((0, 255))

        im = Image.fromarray(im_converted_arr)
        im.show()
        im.save("salt_noise.jpeg")

def part_two():
    """
    进行平滑(中值滤波处理)
    """
    with open("salt_noise.jpeg", "rb") as fp:
        im = Image.open(fp)
        im.show()

        im_arr = np.asarray(im)
        # im_converted_arr = 

def main():
    # part_one()
    part_two()

if __name__ == "__main__":
    main()
