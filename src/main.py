from noiselib import NoiseLib
import os


# %% User's call side (for testing)
    
if __name__ == "__main__":

    folder_name = "../imgs"
    if (folder_name == ""):
        dir_path = os.path.dirname(os.path.realpath(__file__))
    else:
        dir_path = folder_name
    
    print("Using directory path", dir_path)
    nl = NoiseLib()
    
    """
    # Applies human noise to all images in folder
    nl.read_folder(dir_path)
    img = nl.add_human_noise_to_imgs(5)
    nl.visualize_plt(img)
    """
    
# %%
    # Visualization of salt-n-pepper
    nl.add_random_noise("../imgs/lena.png")
# %% 
    nl.add_random_noise("../imgs/beard-2.jpg")
# %% 
    nl.add_random_noise("../imgs/amish.jpg")
# %%
    nl.add_random_noise("../imgs/1_0027_-49_-239_434.jpg")

# %% 
    # Visualization of blur effects   
    nl.add_blur("../imgs/amish.jpg", blur="avg", area=[10,10]) 
# %%
    nl.add_blur("../imgs/amish.jpg", blur="gauss", area=[25,25])
# %%
    nl.add_blur("../imgs/lena.png", blur="median", area=[3])
    # %%
    nl.add_blur("../imgs/1_0027_-49_-239_434.jpg", blur="median", area=[9])
# %%
    nl.add_blur("../imgs/beard-2.jpg", blur="bilateral", area=[10,5,5])
# %%
    nl.add_blur("../imgs/1_0027_-49_-239_434.jpg", blur="bilateral", area=[10,200,200])
# %%

    # Add human noise
    nl.add_human_noise_from_file("../imgs/beard-2.jpg")
# %%
    nl.add_human_noise_from_file("../imgs/amish.jpg")
# %%
    
    # Add machine noise
    nl.add_machine_noise_from_file("../imgs/beard-2.jpg")
# %%
    nl.add_machine_noise_from_file("../imgs/amish.jpg")
# %%
    print("Done")