# Challenge 2 Image resizing and storage

## Overview
This repository contains a python code for storing images into a database, resizing them, and performing operations based on the image data. It includes an API to request image frames, apply a custom color map, and manage image width refinement.

## Features
- **Image Resizing:** Resize image width from 200 to 150 pixels.
- **Database Storage:** Store resized images in a database.
- **API:** Request image frames based on depth range and apply a custom color map.

## Requirements
- Python 3.10

## Installation
Follow these steps to set up the project on your local system:

1. **Clone the Repository:**
    ```sh
    git https://github.com/usta-cyber/Challenge2_ImageDB_Resize.git
    cd Challenge2_ImageDB_Resize
    ```

2. **Create a Virtual Environment:**
    ```sh
    python -m venv env
    ```

3. **Activate the Virtual Environment:**
    - On Windows:
        ```sh
        .\env\Scripts\Activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Run the API Server:**
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8005
    ```

2. **Access the API Documentation:**
    - Open your browser and go to: `http://localhost:8005/docs`
    - Use the interactive API documentation to test the endpoints. Click "Try it out" and then "Execute" to run the functions.

## Application Details
- The image data is referenced by the column `depth` in the provided CSV file.
- The remaining columns (200) represent pixel values ranging from 0 to 255 at each depth.
- The image size is resized from 200 to 150 pixels in width.
- Resized images are stored in a database.
- An API is provided to request image frames based on `depth_min` and `depth_max` parameters.
- A custom color map is applied to the generated frames.

## Demo


https://github.com/usta-cyber/Challenge2_ImageDB_Resize/assets/61576602/72089f5d-47f7-4bc4-8503-0f4addb95387



## Example Workflow
1. **Store Images in Database:**
   - Resize images to a width of 150 pixels.
   - Store the resized images in the database.

2. **Request Image Frames:**
   - Use the API to request frames based on specific depth ranges.
   - Apply a custom color map to the requested frames.







---

*Note: Replace placeholder paths and URLs with actual values specific to your project structure.*

