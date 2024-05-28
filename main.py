import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import sqlite3
from matplotlib import cm
from image_resize import resize_image
from image_into_db import store_image_array_into_db,fetch_data_from_db,calculate_min_max_depth


#  API Development with FastAPI
app = FastAPI()
@app.get("/")
async def get_image_frames():
    try:
        #Perfrom Image read and resize operation
        image_csv_path = r'Challenge2.csv'
        resized_img_df = resize_image(image_csv_path)


        #Image into Databse within table
        store_image_array_into_db(resized_img_df)

        #depth values
        min_max_depth = calculate_min_max_depth()
        depth_min = min_max_depth.get("min_depth")
        depth_max = min_max_depth.get("max_depth")
        filtered_frames = fetch_data_from_db(depth_min,depth_max)
        
        #AppExtracted Image Frames
        img_frames = filtered_frames.values
        img_frames = img_frames[:,:-1]
        img_frames = img_frames.astype(np.uint8)
        print("img>>>>",img_frames.shape)

        # Apply the custom color map to the image array
        color_map = plt.get_cmap('gist_rainbow')
        # Apply the colormap like a function to any array:
        color_mapped_frames = color_map (img_frames)
        Image.fromarray((color_mapped_frames[:, :, :3] * 255).astype(np.uint8)).save('clolored_frames.png')
        return "Successfully generate the response"
    except:
        return "Issue in generating final response"


