import streamlit as st
import cv2
from PIL import Image
import numpy as np
st.title("Photo Sketcher generator")
st.write("This webApp converts the given image into a pencil sketch")
st.write("This is the miniproject")
st.write("Rajat Agarwal 2014797")
img=st.sidebar.file_uploader("Upload the image to convert", type=['jpeg','png'])
def photo_sketch(img):
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)
    blur_img=cv2.GaussianBlur(invert_img, (111,111),0)
    invblur_img=cv2.bitwise_not(blur_img)
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    return(sketch_img)

if img is None:
    st.write("Please upload image")
else:
    input_img=Image.open(img)
    final_sketch=photo_sketch(np.array(input_img))
    st.image(img)
    st.write("Final Photo Sketch")
    st.image(final_sketch)

