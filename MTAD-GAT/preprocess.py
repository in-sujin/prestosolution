import os
import numpy as np
import pandas as pd
from pickle import dump

def load_and_save(category, filename, dataset_folder, output_folder):
    # Load the data using pandas
    temp = pd.read_csv(os.path.join(dataset_folder, category, filename), delimiter=",").values
    print(category, filename, temp.shape)
    with open(os.path.join(output_folder, category + ".pkl"), "wb") as file:
        dump(temp, file)

def process_data():
    dataset_folder = "datasets/data"  # Replace with the path to your dataset folder
    output_folder = os.path.join(dataset_folder, "processed")
    os.makedirs(output_folder, exist_ok=True)

    categories = ["train"]
    for category in categories:
        file_list = os.listdir(os.path.join(dataset_folder, category))
        for filename in file_list:
            if filename.endswith(".csv"):
                load_and_save(category, filename, dataset_folder, output_folder)

if __name__ == "__main__":
    process_data()