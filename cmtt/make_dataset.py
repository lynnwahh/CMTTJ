# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : make_dataset.py
# Author     ：Chen Liuyin
# Description：For ssl-transfer/semantic-segmentation formatted dataset
reference: https://hackmd.io/wNGlmMq2RC-lY3l8JhO4SA?view
"""
import os, shutil, json
from PIL import Image
from sklearn.model_selection import train_test_split
from pathlib import Path, PurePosixPath

def split_dataset(data_dir, val=0.3, img_dir_name='data', anno_dir_name='mask'):
    '''
    split the whole dataset into training and validation part
    '''

    # get img and anno original list
    img_dir = data_dir / img_dir_name
    anno_dir = data_dir / anno_dir_name
    imgs = []
    annos = []
    for img_name in sorted(img_dir.iterdir()):
        img_path = img_dir / img_name
        imgs.append(img_path)
    for anno_name in sorted(anno_dir.iterdir()):
        anno_path = anno_dir / anno_name
        annos.append(anno_path)

    train_x, val_x, train_y, val_y = train_test_split(imgs, annos, test_size=val, random_state=42)
    os.makedirs(os.path.join(data_dir, 'images', 'training'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'images', 'validation'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'annotations', 'training'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'annotations', 'validation'), exist_ok=True)

    for path in train_x:
        new_path = str(path).replace(str(img_dir), str(os.path.join(data_dir, 'images', 'training')))
        shutil.move(path, new_path)

    for path in val_x:
        new_path = str(path).replace(str(img_dir), str(os.path.join(data_dir, 'images', 'validation')))
        shutil.move(path, new_path)

    for path in train_y:
        new_path = str(path).replace(str(anno_dir), str(os.path.join(data_dir, 'annotations', 'training')))
        shutil.move(path, new_path)

    for path in val_y:
        new_path = str(path).replace(str(anno_dir), str(os.path.join(data_dir, 'annotations', 'validation')))
        shutil.move(path, new_path)

def odgt(data_dir, img_path):
    #seg_path = img_path.replace('images','annotations')
    #seg_path = seg_path.replace('.jpg','.png')
    img_name = img_path.stem
    anno_dir = data_dir / 'annotations'
    seg_path = list(anno_dir.rglob(img_name + '.*'))[0]
    img_print = str(img_path).replace(str(data_dir.parent), '').replace('\\', '/').strip('/')
    seg_print = str(seg_path).replace(str(data_dir.parent), '').replace('\\', '/').strip('/')

    if seg_path.exists():
        img = Image.open(img_path)
        h = img.height
        w = img.width

        odgt_dic = {}
        odgt_dic["fpath_img"] = img_print
        odgt_dic["fpath_segm"] = seg_print
        odgt_dic["width"] = h
        odgt_dic["height"] = w
        return odgt_dic
    else:
        # print('the corresponded annotation does not exist')
        # print(img_path)
        return None

if __name__ == '__main__':

    data_dir = Path('D:\Research\Data\Cell\CellTracking\DIC-C2DH-HeLa\ssl\set')
    '''
    split_dataset(data_dir)
    '''
    modes = ['training', 'validation']
    saves = ['training.odgt', 'validation.odgt'] # customized

    for i, mode in enumerate(modes):
        save = saves[i]
        dir_path = data_dir / 'images' / mode
        img_list = dir_path.iterdir()

        with open(os.path.join(os.path.split(data_dir)[0], save), mode='wt', encoding='utf-8') as myodgt:
            for i, img in enumerate(img_list):
                a_odgt = odgt(data_dir, img)
                if a_odgt is not None:
                    myodgt.write(f'{json.dumps(a_odgt)}\n')

