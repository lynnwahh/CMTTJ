# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Density.py
# Author     ：Chen Liuyin
# Description：Calculate Cell Imaging Density
"""
import cv2, os

if __name__ == '__main__':
    img_dir = 'D:\\Research\\Data\\Cell\\BBBC\\BBBC3\\mouse_embryos_dic_foreground'
    save_dir = 'effective'
    os.makedirs(os.path.join(img_dir, save_dir), exist_ok=True)

    for img_name in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        row, col = img.shape
        for i in range(col):
            if img.sum(axis=1)[i] >= 255:
                print(i)
                cv2.line(img, pt1=(0, i), pt2=(row, i), color=255, thickness=10)
                cv2.imwrite(os.path.join(img_dir, save_dir, img_name), img)
                break
