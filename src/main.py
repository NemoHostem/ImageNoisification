from noiselib import NoiseLib

# %% User's call side (for testing)
    
if __name__ == "__main__":
    
	folder_name = "../imgs"
	if (folder_name == ""):
		dir_path = os.path.dirname(os.path.realpath(__file__))
	else:
		dir_path = folder_name
	print("Using directory path", dir_path)
	nl = NoiseLib()
	nl.read_folder(dir_path)
	nl.add_human_noise_to_imgs(5)