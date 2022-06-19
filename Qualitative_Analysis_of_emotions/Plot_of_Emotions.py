from feat import Detector
from feat.utils import get_test_data_path
from IPython.core.display import Video
from feat.data import Fex
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from feat.plotting import imshow

def one_plot(csv_file = "",emotion="anger"): # To plot just one requried emotion
    #csv_file = "me.csv"
    # Read a CSV file
    #df1 = pd.read_csv(csv_file, usecols=['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise', 'neutral'])
    df1 = pd.read_csv(csv_file, usecols=[emotion])
    df1.plot()
    plt.show()

def plot_all_in_one(csv_file = ""): # To plot all graphs one after the other of a single file
    #csv_file = "me.csv"
    # Read a CSV file
    df1 = pd.read_csv(csv_file, usecols=['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise', 'neutral'])
    df2 = pd.read_csv(csv_file , usecols=['anger'])
    df3 = pd.read_csv(csv_file , usecols=['disgust'])
    df4 = pd.read_csv(csv_file , usecols=['fear'])
    df5 = pd.read_csv(csv_file , usecols=['happiness'])
    df6 = pd.read_csv(csv_file , usecols=['sadness'])
    df7 = pd.read_csv(csv_file , usecols=['surprise'])
    df8 = pd.read_csv(csv_file , usecols=['neutral'])

    fig, axes = plt.subplots(nrows=7)
    df1.plot(ax=axes[0])
    df2.plot(ax=axes[1])
    df3.plot(ax=axes[2])
    df4.plot(ax=axes[3])
    df5.plot(ax=axes[4])
    df6.plot(ax=axes[5])
    df7.plot(ax=axes[6])
    plt.show()

    fig, axes = plt.subplots(nrows=4, ncols=2)
    df1.plot(ax=axes[0,0])
    df2.plot(ax=axes[0,1])
    df3.plot(ax=axes[1,0])
    df4.plot(ax=axes[1,1])
    df5.plot(ax=axes[2,0])
    df6.plot(ax=axes[2,1])
    df7.plot(ax=axes[3,0])
    df8.plot(ax=axes[3,1])
    plt.show()

def plots(x = [''], y = ''): # To get Human vs Robot vs Diff Plot

    csv_file1 = "me.csv"
    csv_file2 = "Robot.csv"
    csv_file3= "Diff(R-M).csv"

    df1 = pd.read_csv(csv_file1,usecols=x )
    df2 = pd.read_csv(csv_file2,usecols=x)
    df3 = pd.read_csv(csv_file3,usecols=x)

    fig, axes = plt.subplots(nrows=3)

    df1.plot(ax=axes[0], title='        Human')
    df2.plot(ax=axes[1], title='        Robot')
    df3.plot(ax=axes[2], title='        Diff')

    save_results_to = 'C:/Users/manoj_jn/hr-little-api/Computer-Vision/newstart/py-feat-main/py-feat-main/plots/'
    plt.savefig(save_results_to + y+'.png', dpi = 300)

    plt.show()

'''plots(x=['anger'], y='anger')
plots(x=['disgust'],y = 'disgust')
plots(x = ['fear'], y = 'fear')
plots(x = ['happiness'], y = 'happiness')
plots(x = ['sadness'], y = 'sadness')
plots(x = ['surprise'], y = 'surprise')
plots(x = ['neutral'], y = 'neutral')'''

#plot_all_in_one(csv_file = "me.csv")

#one_plot(csv_file="diff(M-R).csv", emotion="surprise")
#one_plot(csv_file="nope.csv", emotion="neutral")

plot_all_in_one(csv_file="nope.csv")
