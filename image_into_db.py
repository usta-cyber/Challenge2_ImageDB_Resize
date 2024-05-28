#Store Image into Database

import sqlite3
import numpy as np
import pandas as pd

def store_image_array_into_db(values_dataframe):
    try:
        conn = sqlite3.connect("image_database.db")
        with conn:
            values_dataframe.to_sql('image_data', conn, if_exists='replace', index=False)
        
        conn.close()
    except Exception as e:
        return "Issue in Image store in Database"


def calculate_min_max_depth():
    try:
        conn = sqlite3.connect("image_database.db")
        with conn:
            cursor = conn.cursor()

            cursor.execute(f"SELECT MIN(d), MAX(d) FROM image_data")
            min_depth, max_depth = cursor.fetchone()

        conn.close()

        return {"min_depth": min_depth, "max_depth": max_depth}

    except Exception as e:
        return {"error": str(e)}
    


def fetch_data_from_db(depth_min,depth_max):
    try:
        conn = sqlite3.connect("image_database.db")
        with conn:
            query = f"SELECT * FROM image_data WHERE d BETWEEN ? AND ?"
            params = (depth_min, depth_max)
            # Retrieve the data using Pandas
            filtered_df = pd.read_sql_query(query, conn, params=params)

        conn.close()
        print("Image data retrive from Database sucessfuly")
        return filtered_df
    except Exception as e:
        print("Issue with reading info from DataBase")
        return "Issue with reading info from DataBase"
