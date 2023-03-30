import cv2
import os

yourDirectory = "metal_dataset/death/"
# for filename in listdir('C:/tensorflow/models/research/object_detection/images/train'):
for filename in os.listdir(yourDirectory):
    if filename.endswith(".jpg"):
        print(yourDirectory + filename)
        # cv2.imread('C:/tensorflow/models/research/object_detection/images/train/'+filename)
        try:
            img = cv2.imread(yourDirectory + filename)
        except:
            if os.path.exists(yourDirectory + filename):
                os.remove(yourDirectory + filename)
                print("DELETED: ", yourDirectory + filename, "\n\n")
            else:
                print("The file does not exist")
                # delete if sus
        if img is None or img.size == 0:
            if os.path.exists(yourDirectory + filename):
                os.remove(yourDirectory + filename)
                print("DELETED: ", yourDirectory + filename, "\n\n")
            else:
                print("The file does not exist")
