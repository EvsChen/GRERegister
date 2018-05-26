from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

img = np.array(Image.open('INFF.jpg').convert('L'));
# im.show();

threshold = 128;

rows,cols = img.shape
white = [0] * cols # define the list of the number of white pixels along x-axis

# binarization

for i in range(rows):
    for j in range(cols):
        if (img[i,j]<=threshold):
            img[i,j]=0
        else:
            img[i,j]=1
            white[j] = white[j] + 1

# segmentation

line = np.where(np.array(white) > 0, 1, 0);
seg = [];
start = 0; end = 0;
for i in range(len(line)):
    if i == 0 or (line[i] == 0 and line[i-1] != 0):
        start = i;        
    elif i == len(line)-1 or (line[i] == 0 and line[i+1] != 0) :
        end = i;
        seg.append((start + end) // 2)   
        start = 0
        end = 0
print(seg);

# save image 


for i in range(len(seg) - 1):
    arr = img[:,seg[i]:seg[i+1]]
    arr_img = Image.fromarray(arr)
    plt.imsave('seg%d.jpg'%(i+1),arr_img,cmap=cm.gray)
    # plt.imshow(arr_img);
    # plt.show();
    # arr_img.save('seg%d.jpg'%(i+1))


# for i in range(rows):
#     for j in range(len(seg)):
#         img[i,seg[j]] =  1; 
    
plt.subplot(3,1,1)
plt.imshow(img,cmap=cm.gray)
plt.axis("off")
plt.subplot(3,1,2)
plt.plot(white);
plt.subplot(3,1,3)
plt.plot(line)
plt.show()
