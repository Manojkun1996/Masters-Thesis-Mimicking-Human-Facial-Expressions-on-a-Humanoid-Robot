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
    emotion_model="rf",
    facepose_model="pnp"
)

#print(detector)

from feat.utils import get_test_data_path
from feat.plotting import imshow
import os
# Helper to point to the test data folder
test_data_dir = get_test_data_path()
# Get the full path
single_face_img_path = os.path.join(test_data_dir, "Happy.JPEG")
# Plot it
imshow(single_face_img_path)
single_face_prediction = detector.detect_image(single_face_img_path)
#print(type(single_face_prediction))
# Show results
#print(single_face_prediction)

#print(single_face_prediction.aus)

#print(single_face_prediction.emotions)

#detector.detect_image(single_face_img_path, outputFname = "output.csv")

from feat.utils import read_feat
import matplotlib.pyplot as plt

#input_prediction = read_feat("output.csv")

# Show results
#print(input_prediction)

#figs = single_face_prediction.plot_detections(poses=True)
#plt.plot('figs')
#plt.show()

from feat import Detector

face_model = "img2pose"
landmark_model = "mobilenet"
au_model = "logistic"
emotion_model = "fer"
facepose_model = "img2pose"
detector = Detector(
    face_model=face_model,
    landmark_model=landmark_model,
    au_model=au_model,
    emotion_model=emotion_model,
    facepose_model=facepose_model,
)
#print(detector)

from feat.utils import get_test_data_path
import os
import cv2
import numpy as np

from feat.utils import get_test_data_path
import os

test_data_dir = get_test_data_path()
test_video_path = os.path.join(test_data_dir, "einstein.mp4")

# Show video
from IPython.core.display import Video
Video(test_video_path, embed=True)
video_prediction = detector.detect_video(test_video_path, skip_frames=30)
#print(video_prediction.head())

#print(video_prediction.shape)
'''x = video_prediction.loc[[48, 408]].plot_detections(faceboxes=False, add_titles=False)
plt.plot('x')
plt.show()'''

axes = video_prediction.emotions.plot()
plt.plot('axes')
plt.show()












