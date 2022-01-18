# Implementation of Captcha-Solver and Generating Unsolvable Captchas
Comp 430 - Data Privacy and Security - Final Project

# Part 1
First, we created different datasets of different sizes. In order to understand how to create different sized datasets read the readme of the code that we are also using: https://github.com/JackonYang/captcha-tensorflow.git
Our jupyter notebooks are also commented, so you can also analyze the code row by row in our notebooks.
Based on the figure in title "Benchmarking", we prove that the accuracy of the model is directly related to to the number of samples that the model was trained on.
## Running Instructions for Part 1
For CNN:
Run captcha_project1.ipynb in order to generate a dataset using python_captcha package. You can train 4 models by uncommenting the one that you want to train. These models differ on hyperparameters such as activation functions, maxpoolings, etc.
During experiment we trained for 4 epochs for the two dataset variations which we had. You do not necessaily have to train these models on the same dataset which we had since the accuracy is directly correlated to the dataset size.
For YOLO:
Run Captcha_Solver_YOLO_Algorithm.ipynb. This algorithm will yield over 70% accuracy with only 587 training images.
# Part 2
You can see that both notebooks save the model separately. Just use the model which the best accuracy that youy obtain from part 1. Note that you have to load that specific highly accurate model 90%+.
You have to set the test_idx variable to the directory of the newly created test set which you will obtain by our novel captcha creation method by using the codes in the folder named "Part 2 Dataset Creation".
Once you do that you can run the cell which tests the model on any given dataset.
This way we tested our already trained model -which acts as the adversary- on our dataset -which acts as defenders dataset-.
Adversary's model had a 40% accuracy drop from what it was trained on which means that the proposed captcha generation method works nicely for an attacker that uses CNN. 
The figure for comparing how our approach affected the accuracy of our model:

![image](https://user-images.githubusercontent.com/53303474/149988697-a71bd07e-2a62-43e9-b39f-0cf4719921b7.png)
## Running Instructions for Part 2
See the file captcha_solver_one_digit.ipynb in "Part 2 Dataset Creation" directory to see our novel unsolvable captcha approach.
Run captcha_project2.ipynb as discussed above.

# Before Running
Any randomized dataset can be used for both part 1 and part 2. 

For part 1 in order for the models to have a 90% accuracy you should not be limiting the number of samples. However you should limit the number of samples if you would like to see lower accuracies.
Around 22k samples would yield 90% accuracy and around 2k samples will yield 10% accuracy on all models for DATASETS THAT ONLY CONTAIN NUMBERS FROM 0-9. Remember to keep the datasplit 80% to 20%.
# Benchmarking
Benchmarking of training dataset in CNN models:

![image](https://user-images.githubusercontent.com/53303474/149988468-6121ea53-5e1f-46ac-bf68-75461afeb181.png)

Benchmarking of training dataset in YOLO models:

![image](https://user-images.githubusercontent.com/53303474/149991263-eea874b5-86f2-4bf6-953e-d35dd79ca132.png)
