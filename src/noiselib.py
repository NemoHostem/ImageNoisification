# -*- coding: utf-8 -*-
"""
@author: Matias
"""

# %% Imports (TODO: Add these for requirements)

from noisify import recipes
import os
from PIL import Image

# %% NoiseLib library

class NoiseLib:
    
    def __init__(self):
        self.test_imgs = []
        self.supported_extensions = [".png", ".PNG", ".jpeg", ".jpg", ".JPG", ".JPEG", ".tiff"]
        pass
    
    def read_image(self, filename):
        test_image = Image.open(filename)
        test_image.show()
        return test_image
    
    def read_folder(self, folder_name):
        
        for filename in os.listdir(folder_name):
            if (filename.endswith(tuple(self.supported_extensions))):
                img_file = folder_name + "/" + filename
                print("Reading file", img_file)
                f_img = Image.open(img_file)
                self.test_imgs.append(f_img)
        
    def clear_images(self):
        self.test_imgs = []
        
    def add_human_noise_to_imgs(self, value=5):
        human_noise = recipes.human_error(value)
        out_imgs = []
        for img in self.test_imgs:
            img.show()
            for out_image in human_noise(img):
                out_image.show()
                out_imgs.append(out_image)
        return out_imgs
        
    def add_human_noise(self, img, value=5):
        human_noise = recipes.human_error(value)
        for out_image in human_noise(img):
            out_image.show()
        return out_image
    
    def add_machine_noise(self, img, value=5):
        machine_noise = recipes.machine_error(value)
        for out_image in machine_noise(img):
            out_image.show()
    
    def add_mixed_noise(self, img, values=[5,5]):
        combined_noise = recipes.machine_error(values[0]) + recipes.human_error(values[1])
        for out_image in combined_noise(img):
            out_image.show()
 
    
# %% User's call side (for testing)
    
#if "__name__" == "__main__":
    
folder_name = "../imgs"
if (folder_name == ""):
    dir_path = os.path.dirname(os.path.realpath(__file__))
else:
    dir_path = folder_name
print("Using directory path", dir_path)
nl = NoiseLib()
nl.read_folder(dir_path)
nl.add_human_noise_to_imgs(5)