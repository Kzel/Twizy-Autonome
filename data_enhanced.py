import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

def date_enhancement(img_input_path,img_output_path):
    image = load_img(img_input_path)
    image = img_to_array(image) # Image transforme a array
    image = np.expand_dims(image, axis=0) # Ajouter un axe
    img_dag = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,
                            height_shift_range = 0.1, shear_range = 0.2, zoom_range = 0.2,
                            horizontal_flip = False, fill_mode = "nearest") # Rotation, le shift de largeur et hauter, Couper, Rotation horizontale, remplissage

    img_generator = img_dag.flow(image, batch_size=1,
                                 save_to_dir=img_output_path,
                                 save_prefix = "image", save_format = "jpg")# Tester le 1er image avec bath_size=1
    count =0 # compteur
    for img in img_generator:
        count += 1
        if count == 5:  # generer 5 sample et quitter
            break

if __name__=="__main__":
    image_path ="./right/2.jpg"
    image_out_path = "./right/enhanced/"
    date_enhancement(image_path, image_out_path)