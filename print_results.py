#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    print('Images Input Stats:\n Number of images = {}\n'.format(results_stats_dic['n_images']))
    print('Number of dog images = {}\n'.format(results_stats_dic['n_dogs_img']))
    print('Number of non-dog images = {}\n'.format(results_stats_dic['n_notdogs_img']))
    
    print('Performance of Classifier models: {}\n'.format(model))
    print('Percentage of Correctly Classified Dogs = {}%\n'.format(results_stats_dic['pct_correct_dogs']))
    print('Percentage of Correctly Classified Dogs\' Breeds = {}%\n'.format(results_stats_dic['pct_correct_breed']))
    print('Percentage of Correctly Classified Non-dogs = {}%\n'.format(results_stats_dic['pct_correct_notdogs']))
    print('Percentage of Correctly Classified Pets = {}%\n'.format(results_stats_dic['pct_label_match']))
    
    if print_incorrect_dogs:
        print('-- Missclassified Dogs from model {} --\n'.format(model))
        n_miss_dogs = 0
        if results_stats_dic['pct_correct_dogs'] < 100 or results_stats_dic['pct_correct_notdogs'] < 100:
            for image in results_dic:
                if sum(results_dic[image][3:]) == 1:
                    n_miss_dogs += 1
                    print('{} is misclassifed as another type of pets: {}\n'.format(image, results_dic[image][1]))
            print('Model {} has misclassifed {} image(s).\n'.format(model, n_miss_dogs))
        else:
            print('There is no misclassifed dog from the model ({}).\n'.format(model))
    else:
        print('The function of showing misclassified dog is switched off.\n')

    if print_incorrect_breed:
        print('-- Missclassified Breeds from model {} --\n'.format(model))
        n_miss_breeds = 0
        if results_stats_dic['pct_correct_breed'] < 100:
            for image in results_dic:
                if sum(results_dic[image][3:]) == 2 and results_dic[image][2] == 0:
                    n_miss_breeds += 1
                    print('{} is misclassified as another type of dogs: {}\n'.format(image, results_dic[image][1]))
            print('Model {} has misclassifed breeds of {} images of dogs.\n'.format(model, n_miss_breeds))
        else:
            print('There is no misclassified breeds of dogs from the model ({}).\n'.format(model))
    else:
        print('The function of showing misclassifed breeds is switched off.')
                         
    None
                
