import cv2
import numpy as np
import os
import sys
import tensorflow as tf

# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras.models import Sequential


def get_model_for_img(img_h, img_w, catagorise_number):
    """
    CS50 img model implementor
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    # GitHub user||student : AtiChetsurakul from course cs50ai

    model = tf.keras.models.Sequential([

        # 30 x 30 RGB image as input
        # tf.keras.Input(shape=(img_h, img_w, 3)),
        tf.keras.layers.Rescaling(1./255, input_shape=(img_h, img_w, 3)),

        # convolutional test fromhandwriting lec src
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        # pooling pool size = 2x2
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        # convolutional test fromhandwriting lec src
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        # pooling pool size = 2x2
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # GitHub user||student : AtiChetsurakul

        # Flatten units
        tf.keras.layers.Flatten(),

        # hidden layer
        tf.keras.layers.Dense(6*catagorise_number, activation="relu"),
        # reduce overfit with dropout
        tf.keras.layers.Dropout(0.5),

        # Add an output layer with output units
        tf.keras.layers.Dense(catagorise_number, activation="softmax")
    ])
    # model compiling cp from handw lec src
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model
