from collections import Counter

import copy
import numpy as np
import sys
import tensorflow as tf

import check50
import check50.py


@check50.check()
def exists():
    """traffic.py exists"""
    check50.include("dataset")
    check50.exists("traffic.py")


@check50.check(exists)
def imports():
    """traffic.py imports"""
    sys.path = [""] + sys.path
    check50.py.import_("traffic.py")


@check50.check(imports)
def load_data_lines():
    """load_data returns correct number of images and labels"""

    # Setup
    sys.path = [""] + sys.path
    traffic = check50.py.import_("traffic.py")
    traffic.NUM_CATEGORIES = 43
    traffic.IMG_WIDTH = 30
    traffic.IMG_HEIGHT = 30
    images, labels = traffic.load_data("dataset")
    expected = 129

    if len(images) != expected:
        raise check50.Mismatch(f"{expected} images",
                               f"{len(images)} images")

    if len(labels) != expected:
        raise check50.Mismatch(f"{expected} labels",
                               f"{len(labels)} labels")

@check50.check(imports)
def load_data_dimensions():
    """load_data returns images with correct dimensions"""

    # Setup
    sys.path = [""] + sys.path
    traffic = check50.py.import_("traffic.py")
    traffic.NUM_CATEGORIES = 43
    traffic.IMG_WIDTH = 30
    traffic.IMG_HEIGHT = 30
    images, labels = traffic.load_data("dataset")
    expected = (30, 30, 3)

    for image in images:
        if image.shape != expected:
            raise check50.Mismatch(f"image with shape {expected}",
                                   f"image with shape {image.shape}")


@check50.check(imports)
def load_data_labels():
    """load_data returns correct labels"""

    # Setup
    sys.path = [""] + sys.path
    traffic = check50.py.import_("traffic.py")
    traffic.NUM_CATEGORIES = 43
    traffic.IMG_WIDTH = 30
    traffic.IMG_HEIGHT = 30
    images, labels = traffic.load_data("dataset")

    counter = Counter(labels)
    for i in range(43):
        if counter.get(i) != 3 and counter.get(str(i)) != 3:
            raise check50.Failure(f"expected 3 labels for category {i}, got {counter.get(i)}")


@check50.check(imports)
def get_model_is_model():
    """get_model returns a Keras model"""

    # Setup
    sys.path = [""] + sys.path
    traffic = check50.py.import_("traffic.py")
    traffic.NUM_CATEGORIES = 43
    traffic.IMG_WIDTH = 30
    traffic.IMG_HEIGHT = 30
    model = traffic.get_model()

    if not isinstance(model, tf.keras.Model):
        raise check50.Failure(f"expected a model, got {str(type(model))} instead")


@check50.check(imports)
def get_model_layers():
    """model has multiple layers"""

    # Setup
    sys.path = [""] + sys.path
    traffic = check50.py.import_("traffic.py")
    traffic.NUM_CATEGORIES = 43
    traffic.IMG_WIDTH = 30
    traffic.IMG_HEIGHT = 30
    model = traffic.get_model()

    if len(model.layers) < 2:
        raise check50.Failure(f"expected model to have multiple layers")

