from PIL import Image, ImageEnhance
import numpy as np
import cv2


def adjust_saturation(image_path, output_path, saturation_level):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Color(image)
    adjusted_image = enhancer.enhance(saturation_level)
    adjusted_image.save(output_path)


def adjust_brightness(image_path, output_path, brightness_level):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    adjusted_image = enhancer.enhance(brightness_level)
    adjusted_image.save(output_path)


def adjust_contrast(image_path, output_path, contrast_level):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    adjusted_image = enhancer.enhance(contrast_level)
    adjusted_image.save(output_path)


def adjust_white_balance(image_path, output_path):
    image = cv2.imread(image_path)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_image)
    l = cv2.equalizeHist(l)
    balanced_lab = cv2.merge((l, a, b))
    balanced_image = cv2.cvtColor(balanced_lab, cv2.COLOR_LAB2BGR)
    cv2.imwrite(output_path, balanced_image)