import os
import streamlit as st
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

from fastai.vision.all import *
from fastai.vision.widgets import *


learn_inf = load_learner('model.pkl')


class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(os.path.join(os.getcwd(), filename))
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()

    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload Files", type=['png', 'jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(250, 250), caption='Uploaded Image')

    def get_prediction(self):

        if st.button('Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.write(f'**Prediction**: {pred}')
            st.write(f'**Probability**: {probs[pred_idx] * 100:.02f}%')
        else:
            st.write(f'Click the button to classify')


if __name__ == '__main__':
    file_name = 'model.pkl'
    predictor = Predict(file_name)
