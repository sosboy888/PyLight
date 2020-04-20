# -*- coding: utf-8 -*-


import cv2
import numpy as np
import PyLightSettings
import keyboard
from PIL import Image
import gc
import d3dshot
def vidMake(VIDEO_QUEUE):
    gc.collect()
    print("Capturing highlight")
    SCREEN_SIZE=(PyLightSettings.screen_width,PyLightSettings.screen_height)
    fourcc=cv2.VideoWriter_fourcc(*"H264")
    out=cv2.VideoWriter("highlight.mp4",fourcc,PyLightSettings.fps,(SCREEN_SIZE))
    for img in reversed(VIDEO_QUEUE):
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        out.write(img)
    gc.collect()
def vidCap():
    d=d3dshot.create(capture_output="numpy",frame_buffer_size=900)
    print("Initiating Buffer")
    d.capture(target_fps=30)
    while True:
        if(keyboard.is_pressed(PyLightSettings.recordButton)):
            d.stop()
            vidMake(d.frame_buffer)
            break
        if(keyboard.is_pressed(PyLightSettings.exitButton)):
            break
        
vidCap()
        
        
    
    