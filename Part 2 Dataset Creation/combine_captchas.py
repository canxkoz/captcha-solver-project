import os
import shutil
from PIL import Image

import numpy as np
from tqdm import tqdm

root_dir1   = "char-1-epoch-1000/content/images/char-1-epoch-1000/train/"
root_dir2   = "outputs3/content/outputs3/"
save_dir    = "merged_imgs/"
num_images  = 4
num_iters   = 100
resize_same = False
del_dir = False

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)
elif del_dir:
    shutil.rmtree(save_dir)
    os.mkdir(save_dir)

files1 = [os.path.join(root_dir1, path) for path in os.listdir(root_dir1)]
files2 = [os.path.join(root_dir2, path) for path in os.listdir(root_dir2)]
files  = files1 + files2

for _ in tqdm(range(num_iters)):
    
    sel_files = np.random.choice(files, num_images, replace=False)
    save_filename = ""
    
    for filename in sel_files:
        last_dot   = filename.rfind(".")
        last_slash = filename.rfind("/") + 1
        save_filename += filename[last_slash:last_dot][0]
      
        
    images = [Image.open(img) for img in sel_files]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    
    if resize_same:
        for i in range(len(images)):
            images[i] = images[i].resize(
                (int((widths[i] * (max_height / heights[i]))), max_height)) 
    
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
            
    new_im = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    
    new_im.save(os.path.join(save_dir, save_filename + '.png'))
