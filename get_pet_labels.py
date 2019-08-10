#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Alfred Cheung
# DATE CREATED: 13-02-2019                      
# REVISED DATE: 16-02-2019
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from PIL import Image

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create a list of filenames existing in the pets' image folder
    filename_list = listdir(image_dir)
    # Filter possible invalid files or file names by a dictionary (faster speed in iteration)
    results_dic = {}
    for filename in filename_list:
        alnum_check = 0
        trunc_name = ""
        pet_label = ""
        # avoid hidden files
        if not filename.startswith('.'):
            # avoid files of other format
            if filename.endswith('.jpg'):
                trunc_name = filename[:-4]
                # check whether there are spaces in filenames and replace then with underscore
                if trunc_name.find(' ') > 0:
                    trunc_name = trunc_name.replace(' ', '_')
                # Spliting the filename into segments whenever there is an underscore
                for word in trunc_name.split("_"):
                    # Spliting the filename into segments whenever there is an underscore
                    if word.isalpha():
                        pet_label += word.lower() + " "
                    elif not word.isdigit() and word.isalnum(): # Checking if filenames like Cat0123.jpg exist
                        alnum_check += 1
                
                if alnum_check == 0: 
                    if filename not in results_dic:
                        results_dic[filename] = [pet_label.strip()]
                    else:
                        print('Filename already exists in results_dic. Filename: {}, Label: {}'.format(filename, results_dic[filename]))
                else:         
                    print('Invalid filename which may lead to incorrect results: {}'.format(filename))
            else:
                print('Files with other formats found: {}'.format(filename))  
                                                                                  
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
