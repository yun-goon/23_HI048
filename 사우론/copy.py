import os
import random
import json
import shutil

def copy_files(json_dir, jpg_dir, dst_dir, num_files=50):
    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

# If there are less than num_files, copy all of them
    if len(json_files) < num_files:
        num_files = len(json_files)

    selected_files = random.sample(json_files, num_files)

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for file in selected_files:
        # Copy JSON file
        shutil.copy(os.path.join(json_dir, file), os.path.join(dst_dir, file))

# Copy JPG file with the same name
        jpg_file = file.rsplit(".", 1)[0] + ".jpg"
        shutil.copy(os.path.join(jpg_dir, jpg_file), os.path.join(dst_dir, jpg_file))

# Example of use
json_dir = './ummjongwoo/OriginData/data/label/pig'
jpg_dir = './ummjongwoo/OriginData/data/images/pig'
dst_dir = './copydata'
copy_files(json_dir, jpg_dir, dst_dir)