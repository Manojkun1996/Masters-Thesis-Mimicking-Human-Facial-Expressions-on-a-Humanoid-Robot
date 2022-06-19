from feat import Detector
from feat.utils import get_test_data_path
from feat.plotting import imshow
from IPython.core.display import Video
from feat.data import Fex
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# This Function takes image name as an input and gives the log data as the output
def images(image_name=""):
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
    # print(detector)
    fex = Fex()
    # Helper to point to the test data folder
    test_data_dir = get_test_data_path()
    # Get the full path of image
    single_face_img_path = os.path.join(test_data_dir, image_name)

    imshow(single_face_img_path)

    single_face_prediction = detector.detect_image(single_face_img_path)

    # Show results
    print(single_face_prediction)
    detector.detect_image(single_face_img_path, outputFname="output.csv")

# Give the video to plot the emotions
def video_to_emotion(video="",csv_name=""):
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
    test_data_dir = get_test_data_path()
    test_video_path = os.path.join(test_data_dir, video)
    # test_video_path_2 = os.path.join(test_data_dir, "me.mp4")

    # Show video
    #Video(test_video_path, embed=True)

    video_prediction = detector.detect_video(test_video_path, skip_frames=24)

    print(video_prediction)
    # video_prediction.emotions.plot()
    print(video_prediction.emotions)

    df = pd.DataFrame(video_prediction.emotions)



    df.to_csv(r'C:/Users/manoj_jn/hr-little-api/Computer-Vision/newstart/py-feat-main/py-feat-main/'+csv_name+'.csv')

    csv_file = csv_name+'.csv'
    df1 = pd.read_csv(csv_file, usecols=['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise', 'neutral'])
    df2 = pd.read_csv(csv_file, usecols=['anger'])
    df3 = pd.read_csv(csv_file, usecols=['disgust'])
    df4 = pd.read_csv(csv_file, usecols=['fear'])
    df5 = pd.read_csv(csv_file, usecols=['happiness'])
    df6 = pd.read_csv(csv_file, usecols=['sadness'])
    df7 = pd.read_csv(csv_file, usecols=['surprise'])
    df8 = pd.read_csv(csv_file, usecols=['neutral'])

    fig, axes = plt.subplots(nrows=8)
    df1.plot(ax=axes[0])
    df2.plot(ax=axes[1])
    df3.plot(ax=axes[2])
    df4.plot(ax=axes[3])
    df5.plot(ax=axes[4])
    df6.plot(ax=axes[5])
    df7.plot(ax=axes[6])
    df8.plot(ax=axes[7])
    plt.show()

# images(image_name= "single_face.jpg")
#video_to_emotion(video="me.mp4",y="No" )
video_to_emotion(video="nope.mp4",csv_name="nope")