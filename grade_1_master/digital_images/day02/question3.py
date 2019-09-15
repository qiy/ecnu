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
        im_wigth, im_height = im.size

        template = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ] # 3x3 中值模版
        im_arr = np.asarray(im)
        im_converted_arr = deepcopy(im_arr)
        for i in range(im_height):
            for j in range(im_wigth):
                if i == 0 and j == 0:
                    template = [
                        [im_arr[i][j], im_arr[i][j], im_arr[i+1][j]],
                        [im_arr[i][j], 0, im_arr[i+1][j]],
                        [im_arr[i][j+1], im_arr[i][j+1], im_arr[i+1][j+1]],
                    ]
                elif i == 0 and j == im_wigth - 1:
                    template = [
                        [im_arr[i][j-1], im_arr[i][j], im_arr[i][j]],
                        [im_arr[i][j-1], 0, im_arr[i][j]],
                        [im_arr[i+1][j-1], im_arr[i+1][j], im_arr[i+1][j]],
                    ]
                elif j == 0 and i == im_height - 1:
                    template = [
                        [im_arr[i-1][j], im_arr[i-1][j], im_arr[i-1][j+1]],
                        [im_arr[i][j], 0, im_arr[i][j+1]],
                        [im_arr[i][j], im_arr[i][j], im_arr[i][j+1]],
                    ]
                elif i == im_height - 1 and j == im_wigth - 1:
                    template = [
                        [im_arr[i-1][j-1], im_arr[i-1][j], im_arr[i-1][j]],
                        [im_arr[i][j-1], 0, im_arr[i][j]],
                        [im_arr[i][j-1], im_arr[i][j], im_arr[i][j]],
                    ]
                elif i > 0 and i < im_wigth - 1:
                    template = [
                        [im_arr[i-1][j], im_arr[i-1][j], im_arr[i-1][j+1]],
                        [im_arr[i][j], 0, im_arr[i][j+1]],
                        [im_arr[i][j], im_arr[i][j], im_arr[i][j+1]],
                    ]
                template[1][1] = im_arr[i][j]
                im_converted_arr[i][j] = np.median(template)

        im_converted = Image.fromarray(im_converted_arr)
        im.show()

def main():
    # part_one()
    part_two()

if __name__ == "__main__":
    main()
