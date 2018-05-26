#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to process captcha '

__author__ = 'EvsChen'


from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def process(filepath,threshold=128):
    img = np.array(Image.open(filepath).convert('L'))
    rows,cols = img.shape
    white = [0] * cols # define the list of the number of white pixels along x-axis
    # binarization 
    for i in range(rows):
        for j in range(cols):
            if (img[i,j]<=threshold):
                img[i,j]=0
            else:
                img[i,j]=1
                white[j] = white[j] + 1 # white is the array storing the number of white pixels per column
    # segmentation
    line = np.where(np.array(white) > 0, 1, 0) #the segmentation line 
    seg = []
    start = 0
    end = 0
    for i in range(len(line)):
        if i == 0 or (line[i] == 0 and line[i-1] != 0):
            start = i        
        elif i == len(line)-1 or (line[i] == 0 and line[i+1] != 0) :
            end = i
            seg.append((start + end) // 2)   
            start = 0
            end = 0
    if len(seg) < 4:
        seg.insert(0,0)
    print(seg)
    # save image 
    filename = filepath.split('/')[-1]
    foldername = filename.split('.')[0]
    for i in range(len(seg) - 1):
        arr = img[:,seg[i]:seg[i+1]]
        arr_img = Image.fromarray(arr)
        plt.imsave('./captcha/%s/seg%d.jpg'%(foldername,i+1),arr_img,cmap=cm.gray)
    return len(seg)


import os
import subprocess

def image_to_string(img, cleanup=True, plus=''):
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text

def readCaptcha(filepath):
    numOfChar = process(filepath)
    filename = filepath.split('/')[-1]
    foldername = filename.split('.')[0]    
    result = '';
    for i in range(1,numOfChar): 
        segName = './captcha/%s/seg%d.jpg'%(foldername,i)
        img = np.array(Image.open(segName).convert('L'))
        rows,cols = img.shape
        # print(rows)
        # print(cols)
        if cols >= 28 :
            result = result + image_to_string(segName,True,'-psm 7 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            result = result + image_to_string(segName,True,'-psm 10 -l eng -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return result