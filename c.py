import cv2
import numpy as np
import glob
import os

# Path to the folder containing the input images
image_folder = '/home/jetson/AutonomousPhotogrammetry/imgT/'

# Read input images from the folder
images = []
for filename in glob.glob(image_folder + '*.jpg'):
    img = cv2.imread(filename)
    if img is not None:
        images.append(img)

# Check if there are enough images for stitching
if len(images) < 2:
    print("Insufficient images for stitching")
    exit()

# Create a stitcher object
stitcher = cv2.Stitcher_create()

# Stitch the images to create a panorama
status, panorama = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    # Remove duplicate objects from the panorama image
    gray = cv2.cvtColor(panorama, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 500:
            cv2.drawContours(mask, [contour], -1, 0, -1)
    panorama = cv2.bitwise_and(panorama, panorama, mask=mask)

    # Check if "panorama.jpg" exists
    existing_filename = "pano1.jpg"
    new_filename = "pano1.jpg"
    if os.path.exists(existing_filename):
        i = 2
        while os.path.exists(new_filename):
            new_filename = f"pano{i}.jpg"
            i += 1

    # Save the stitched panorama image
    cv2.imwrite(new_filename, panorama)
    print(f"Panorama image saved as {new_filename}")
    
    # Delete the images stored in the imgT folder
    for filename in glob.glob(image_folder + '*.jpg'):
       os.remove(filename)
    print("Images deleted successfully")
else:
    print("Error during stitching")