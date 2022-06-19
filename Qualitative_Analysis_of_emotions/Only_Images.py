'''from feat import Detector
detector = Detector(au_model='rf', emotion_model='svm')
detector'''

#To define a detector
'''from feat.detector import Detector
detector = Detector(verbose=True)
print(detector)'''

#To change any detector model
'''detector.change_model(
    face_model="MTCNN", emotion_model="svm", au_model="svm", landmark_model=None
)
detector'''

'''from feat.data import Fex
import pandas as pd
fex = Fex()
x=isinstance(fex, pd.DataFrame)
print(x)'''

from feat import Detector

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilenet",
    au_model="rf",
    emotion_model="fer",
    facepose_model="pnp"
)

#print(detector)

from feat.utils import get_test_data_path
from feat.plotting import imshow
import os
import matplotlib.pyplot as plt
# Helper to point to the test data folder
test_data_dir = get_test_data_path()
# Get the full path
single_face_img_path = os.path.join(test_data_dir, "angry_face.jpg")
# Plot it
print(imshow(single_face_img_path))
single_face_prediction = detector.detect_image(single_face_img_path)
#print(type(single_face_prediction))
# Show results
print(single_face_prediction)

print(single_face_prediction.aus)

print(single_face_prediction.emotions)

detector.detect_image(single_face_img_path, outputFname = "output.csv")



figs = single_face_prediction.plot_detections(poses=True)
plt.plot('figs')
plt.show()












