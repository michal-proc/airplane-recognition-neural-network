# Airplane Recognition Neural Network

## Overview
This project is dedicated to developing a military aircraft recognition tool using Python and TensorFlow. It combines Python's accessibility and flexibility with TensorFlow's powerful machine learning and deep learning libraries to recognize and classify different types of military aircraft from images. The goal is to create a highly accurate and efficient recognition system. Currently in the development phase.


## Project Structure


```plaintext
application
      app.py: The main application file to launch the model in a graphical interface.
model
      model.py: Contains the definition and compilation of the CNN model.
utils
      data_preprocessing.py: Script for preprocessing the image data.
      data_summary.py: Generates a summary of the dataset.
      dataset_cleaning.py: Utility for cleaning and validating the dataset.
      dataset_verifier.py: Verifies the integrity of the dataset.
      model_summary.py: Provides a detailed summary of the model's architecture.
      names_generator.py: Generates names for model saving.
      oversampler.py: Balances the dataset by oversampling minority classes.
      small_files_remover.py: Removes files below a certain size threshold.
```

## Model 

The model, defined in model.py, is a sequential CNN.. It consists of several layers including Rescaling, Conv2D, MaxPooling2D, BatchNormalization, Flatten, Dense, and Dropout. The detailed architecture is as follows:

```plaintext
model: "sequential_1"
_____________________________________________________________________________________
 Layer (type)                                   Output Shape              Param #
=====================================================================================
 rescaling (Rescaling)                          (None, 128, 128, 3)       0
 conv2d (Conv2D)                                (None, 128, 128, 8)       104
 max_pooling2d (MaxPooling2D)                   (None, 64, 64, 8)         0
 batch_normalization (BatchNormalization)       (None, 64, 64, 8)         32
 conv2d_1 (Conv2D)                              (None, 64, 64, 16)        1168
 max_pooling2d_1 (MaxPooling2D)                 (None, 32, 32, 16)        0
 batch_normalization_1 (BatchNormalization)     (None, 32, 32, 16)        64
 conv2d_2 (Conv2D)                              (None, 32, 32, 32)        8224
 max_pooling2d_2 (MaxPooling2D)                 (None, 16, 16, 32)        0
 batch_normalization_2 (BatchNormalization)     (None, 16, 16, 32)        128
 flatten (Flatten)                              (None, 8192)              0
 dense (Dense)                                  (None, 8192)              67117056
 dropout (Dropout)                              (None, 8192)              0
 dense_1 (Dense)                                (None, 2048)              16779264
 dropout_1 (Dropout)                            (None, 2048)              0
 dense_2 (Dense)                                (None, 512)               1049088
 dropout_2 (Dropout)                            (None, 512)               0
 dense_3 (Dense)                                (None, 128)               65664
 dense_4 (Dense)                                (None, 44)                5676
=====================================================================================
Total params: 85,026,468
Trainable params: 85,026,356
Non-trainable params: 112
_____________________________________________________________________________________
```

## Running the GUI

The GUI for interacting with the model has been implemented using **PyQt**. To launch the graphical interface, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the `application` directory:
   ```bash
   cd application
   ```

3. Run the GUI application:
   ```bash
   python app.py
   ```

The graphical interface will open, allowing you to load images and view the model's predictions for airplane recognition.

## Training the Model

To train the neural network model from scratch, follow these steps:

1. Ensure that all necessary dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the `model` directory:
   ```bash
   cd model
   ```

3. Run the training script:
   ```bash
   python model.py
   ```

This will start training the Convolutional Neural Network (CNN) on the dataset, displaying progress and accuracy metrics during each epoch.

## Data 

The dataset comprises 318,588 images belonging to 44 different classes of military aircraft, with a training set of 254,871 images and a validation set of 63,717 images. The images are organized in directories named after the aircraft models.

```plaintext
Number of files in directory A10: 7860
Number of files in directory A400M: 7068
Number of files in directory AV8B: 7036
Number of files in directory B1: 7732
Number of files in directory B2: 7260
Number of files in directory B52: 7428
Number of files in directory C17: 7612
Number of files in directory C2: 8560
Number of files in directory C5: 6864
Number of files in directory E2: 7148
Number of files in directory E7: 6012
Number of files in directory EF2000: 7768
Number of files in directory F117: 6816
Number of files in directory F14: 7308
Number of files in directory F15: 10532
Number of files in directory F16: 5464
Number of files in directory F18: 10748
Number of files in directory F22: 7780
Number of files in directory F35: 9856
Number of files in directory F4: 7732
Number of files in directory J10: 6736
Number of files in directory J20: 7480
Number of files in directory JAS39: 7320
Number of files in directory KC135: 6228
Number of files in directory Mig31: 6964
Number of files in directory Mirage2000: 6972
Number of files in directory MQ9: 6712
Number of files in directory P3: 6640
Number of files in directory Rafale: 7432
Number of files in directory RQ4: 6628
Number of files in directory SR71: 6472
Number of files in directory Su24: 6348
Number of files in directory Su25: 6116
Number of files in directory Su34: 6988
Number of files in directory Su57: 6780
Number of files in directory Tornado: 7132
Number of files in directory Tu160: 6576
Number of files in directory Tu95: 6548
Number of files in directory U2: 6556
Number of files in directory US2: 7848
Number of files in directory V22: 8536
Number of files in directory Vulcan: 6864
Number of files in directory XB70: 6144
Number of files in directory YF23: 5988
```

## Training
The model was trained over 25 epochs, showing consistent improvement in accuracy and a decrease in loss. Here is a summary of the training process:
```plaintext
Found 318588 files belonging to 44 classes.
Using 254871 files for training.
Using 63717 files for validation.

Epoch 1/25
1992/1992 [========================] - 447s 155ms/step - loss: 3.5752 - accuracy: 0.0787 - val_loss: 2.8924 - val_accuracy: 0.2401
Epoch 2/25
1992/1992 [========================] - 279s 140ms/step - loss: 2.3299 - accuracy: 0.3791 - val_loss: 1.3714 - val_accuracy: 0.6257
Epoch 3/25
1992/1992 [========================] - 308s 154ms/step - loss: 1.4879 - accuracy: 0.5924 - val_loss: 0.8906 - val_accuracy: 0.7595
Epoch 4/25
1992/1992 [========================] - 304s 153ms/step - loss: 1.0790 - accuracy: 0.6993 - val_loss: 0.6142 - val_accuracy: 0.8349
Epoch 5/25
1992/1992 [========================] - 303s 152ms/step - loss: 0.8399 - accuracy: 0.7647 - val_loss: 0.4612 - val_accuracy: 0.8781
Epoch 6/25
1992/1992 [========================] - 282s 141ms/step - loss: 0.6878 - accuracy: 0.8064 - val_loss: 0.3742 - val_accuracy: 0.9048
Epoch 7/25
1992/1992 [========================] - 289s 145ms/step - loss: 0.5838 - accuracy: 0.8355 - val_loss: 0.3296 - val_accuracy: 0.9153
Epoch 8/25
1992/1992 [========================] - 305s 153ms/step - loss: 0.5071 - accuracy: 0.8578 - val_loss: 0.2664 - val_accuracy: 0.9343
Epoch 9/25
1992/1992 [========================] - 307s 154ms/step - loss: 0.4454 - accuracy: 0.8759 - val_loss: 0.2378 - val_accuracy: 0.9426
Epoch 10/25
1992/1992 [========================] - 314s 158ms/step - loss: 0.3946 - accuracy: 0.8896 - val_loss: 0.2197 - val_accuracy: 0.9478
Epoch 11/25
1992/1992 [========================] - 320s 161ms/step - loss: 0.3524 - accuracy: 0.9018 - val_loss: 0.2162 - val_accuracy: 0.9521
Epoch 12/25
1992/1992 [========================] - 308s 154ms/step - loss: 0.3233 - accuracy: 0.9107 - val_loss: 0.1951 - val_accuracy: 0.9570
Epoch 13/25
1992/1992 [========================] - 299s 150ms/step - loss: 0.2913 - accuracy: 0.9203 - val_loss: 0.1720 - val_accuracy: 0.9624
Epoch 14/25
1992/1992 [========================] - 300s 151ms/step - loss: 0.2692 - accuracy: 0.9269 - val_loss: 0.1832 - val_accuracy: 0.9621
Epoch 15/25
1992/1992 [========================] - 286s 144ms/step - loss: 0.2430 - accuracy: 0.9344 - val_loss: 0.1556 - val_accuracy: 0.9679
Epoch 16/25
1992/1992 [========================] - 300s 151ms/step - loss: 0.2285 - accuracy: 0.9391 - val_loss: 0.1563 - val_accuracy: 0.9676
Epoch 17/25
1992/1992 [========================] - 299s 150ms/step - loss: 0.2120 - accuracy: 0.9437 - val_loss: 0.1509 - val_accuracy: 0.9688
Epoch 18/25
1992/1992 [========================] - 295s 148ms/step - loss: 0.1998 - accuracy: 0.9474 - val_loss: 0.1444 - val_accuracy: 0.9712
Epoch 19/25
1992/1992 [========================] - 289s 145ms/step - loss: 0.1852 - accuracy: 0.9512 - val_loss: 0.1507 - val_accuracy: 0.9711
Epoch 20/25
1992/1992 [========================] - 292s 147ms/step - loss: 0.1810 - accuracy: 0.9530 - val_loss: 0.1368 - val_accuracy: 0.9747
Epoch 21/25
1992/1992 [========================] - 295s 148ms/step - loss: 0.1746 - accuracy: 0.9550 - val_loss: 0.1397 - val_accuracy: 0.9741
Epoch 22/25
1992/1992 [========================] - 299s 150ms/step - loss: 0.1577 - accuracy: 0.9593 - val_loss: 0.1316 - val_accuracy: 0.9748
Epoch 23/25
1992/1992 [========================] - 299s 150ms/step - loss: 0.1536 - accuracy: 0.9610 - val_loss: 0.1301 - val_accuracy: 0.9747
Epoch 24/25
1992/1992 [========================] - 301s 151ms/step - loss: 0.1427 - accuracy: 0.9637 - val_loss: 0.1336 - val_accuracy: 0.9752
Epoch 25/25
1992/1992 [========================] - 300s 151ms/step - loss: 0.1399 - accuracy: 0.9651 - val_loss: 0.1352 - val_accuracy: 0.9771
```

## Visualization


Below is a graph showcasing the training and validation accuracy over the epochs:


![image](https://github.com/MaciejGrzybacz/AirplaneRecognition/assets/128727060/38799349-483d-47f3-9dc4-7ead9a529613)

## Usage


To demonstrate the model's capabilities in a user-friendly manner, we have developed a basic GUI application using PyQt. This interface allows users to interact with the model directly, providing a practical and visual way to test model on new images.
Sample below:

![image](https://github.com/MaciejGrzybacz/AirplaneRecognition/assets/128727060/af8dfbba-c5b3-4f43-bdd1-0ae30beb018e)
Test image was downloaded from Google.
