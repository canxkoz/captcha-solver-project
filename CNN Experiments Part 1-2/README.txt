Part 1:
Just create different datasets of different sizes. In order to understand how to create different sized datasets read the readme of the code that we are also using: https://github.com/JackonYang/captcha-tensorflow.git
I also left comments on the notebook. This way we prove that the accuracy of the model is directly related to to the number of samples that the model was trained on.
Run captcha_project1 in order to generate a dataset using python_captcha package. You can train 4 models by uncommenting the one that you want to train. 
During experiment we trained for 4 epochs for the two dataset variations which we had. You do not necessaily have to train these models on the same dataset which we had since the accuracy is directly correlated to the dataset size.
Part 2:
You can see that both notebooks save the model separately. Just use the model which the best accuracy that youy obtain from part 1. Note that you have to load that specific highly accurate model 90%+.
You have to set the test_idx variable to the directory of the newly created test set which you will obtain by our novel captcha creation method by using the codes in the folder named "Part 2 Dataset Creation".
Once you do that you can run the cell which tests the model on any given dataset.
This way we tested our already trained model -which acts as the adversary- on our dataset -which acts as defenders dataset-.
Adversary's model had a 40% accuracy drop from what it was trained on which means that the proposed captcha generation method works nicely for an attacker that uses CNN. 

Any randomized dataset can be used for both part 1 and part 2. 

For part 1 in order for the models to have a 90% accuracy you should not be limiting the number of samples. However you should limit the number of samples if you would like to see lower accuracies.
Around 22k samples would yield 90% accuracy and around 2k samples will yield 10% accuracy on all models for DATASETS THAT ONLY CONTAIN NUMBERS FROM 0-9. Remember to keep the datasplit 80% to 20%.


