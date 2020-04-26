# -*- coding: utf-8 -*-
"""
@author: Matias
"""

# %% Imports (TODO: Add these for requirements)

from noisify import recipes
import os
from PIL import Image
from scipy import misc
import cv2
import numpy as np
import matplotlib.pyplot as plt

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
            
            self.visualize_plt(img)
            for out_image in human_noise(img):
                self.visualize_plt(out_image)
                out_imgs.append(out_image)
        return out_imgs
        
    def add_human_noise(self, img, value=5):
        human_noise = recipes.human_error(value)
        for out_image in human_noise(img):
            self.visualize_plt(out_image)
        return out_image
    
    def add_human_noise_from_file(self, img_path, value=5, mode="L"):
        human_noise = recipes.human_error(value)
        image  = misc.imread(img_path, mode=mode)
        for out_image in human_noise(image):
            self.visualize_plt(out_image)
        noisy_img = Image.fromarray(out_image)
        self.visualize_plt(noisy_img)
        return out_image
    
    def add_machine_noise(self, img, value=5):
        machine_noise = recipes.machine_error(value)
        for out_image in machine_noise(img):
            out_image.show()
            
    def add_machine_noise_from_file(self, img_path, value=5, mode="L"):
        machine_noise = recipes.machine_error(value)
        image  = misc.imread(img_path, mode=mode)
        for out_image in machine_noise(image):
            self.visualize_plt(out_image)
        noisy_img = Image.fromarray(out_image)
        self.visualize_plt(noisy_img)
        return out_image
    
    def add_mixed_noise(self, img, values=[5,5]):
        combined_noise = recipes.machine_error(values[0]) + recipes.human_error(values[1])
        for out_image in combined_noise(img):
            out_image.show()
 
    def read_with_misc(self, img_path, mode="L"):
        image  = misc.imread(img_path,mode=mode)
        self.test_imgs.append(image)
        return image

    def add_random_noise(self, img_path, mode="L"):
        image  = misc.imread(img_path, mode=mode)
        noisy1 = image + 2 * image.std() * np.random.random(image.shape)
        noise  = 2 * image.max() * np.random.random(image.shape)
        noisy2 = image + noise
        
        self.visualize_plt_4(image, noisy1, noisy2, noise)
        
    def add_blur(self, img_path, blur="avg", area=[5,5,5]):
        image = cv2.imread(img_path)
        
        if blur == "avg":
            blurred = cv2.blur(image, (area[0],area[1]))
        elif blur == "gauss":
            blurred = cv2.GaussianBlur(image, (area[0],area[1]), 0)
        elif blur == "median":
            blurred = cv2.medianBlur(image, area[0])
        elif blur == "bilateral":
            blurred = cv2.bilateralFilter(image, area[0], area[1], area[2])
        else:
            blurred = cv2.blur(image, (area[0],area[1]))
    
        cv2.imshow("Original image", image)
        cv2.imshow("Blurred image", blurred)

    def visualize_plt(self, img):
        plt.show(img)
    
    def visualize_plt_4(self, img1, img2, img3, noise):
        
        f, axarr = plt.subplots(2, 2)
        axarr[0, 0].imshow(img1, cmap = plt.get_cmap('gray'))
        axarr[0, 0].set_title('Image gray')
        
        axarr[0, 1].imshow(img2, cmap = plt.get_cmap('gray'))
        axarr[0, 1].set_title('Image noise 1')
        
        axarr[1, 0].imshow(img3, cmap = plt.get_cmap('gray'))
        axarr[1, 0].set_title('Image noise 2')
        
        axarr[1, 1].imshow(noise, cmap = plt.get_cmap('gray'))
        axarr[1, 1].set_title('Added Noise')

        plt.show() 
        