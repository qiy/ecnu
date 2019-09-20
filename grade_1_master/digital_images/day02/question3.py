import numpy as np

from copy import deepcopy
from random import choice
from PIL import Image, ImageEnhance, ImageFilter
from scipy import ndimage

'''
3. 对一副图像加噪声，进行平滑，锐化作用。
'''

def mid(array, wigth, height):
    new_array = []
    for i in range(height):
        for j in range(wigth):
            new_array.append(array[i][j])
    return new_array

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
    进行平滑(中值滤波处理)(❌)
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
        im_extend_arr = np.zeros((im_height+2, im_wigth+2))
        im_converted_arr = deepcopy(im_arr)
        for i in range(im_height):
            for j in range(im_wigth):
                if i == 0 or j == 0:
                    im_extend_arr[i][j] = im_arr[i][j]

                if i == im_wigth-1 or j == im_wigth-1:
                    im_extend_arr[i+2][j+2] = im_arr[i][j]
                
                im_extend_arr[i+1][j+1] = im_arr[i][j]

        for i in range(1, im_height+1):
            for j in range(1, im_wigth+1):
                template = [
                    [im_extend_arr[i-1][j-1], im_extend_arr[i-1][j], im_extend_arr[i-1][j+1]],
                    [im_extend_arr[i][j-1], im_extend_arr[i][j], im_extend_arr[i][j+1]],
                    [im_extend_arr[i+1][j-1], im_extend_arr[i+1][j], im_extend_arr[i+1][j+1]],
                ]
                im_converted_arr[i-1][j-1] = np.median(mid(template, 3, 3))

        im_converted = Image.fromarray(im_converted_arr)
        im.show()

def part_three():
    """
    进行平滑
    """
    with open("salt_noise.jpeg", "rb") as fp:
        im = Image.open(fp)
        im.show()
        
        smoothed_im = im.filter(ImageFilter.SMOOTH)
        smoothed_im.show()

def part_four():
    """
    进行锐化    
    """
    with open("salt_noise.jpeg", "rb") as fp:
        im = Image.open(fp)
        im.show()
        
        smoothed_im = im.filter(ImageFilter.SHARPEN)
        smoothed_im.show()

def main():
    # part_one()
    # part_three()
    part_four()

if __name__ == "__main__":
    main()
