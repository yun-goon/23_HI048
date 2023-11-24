import os
import json
import shutil

json_folder_path = './label'
image_folder_path = './images'

# Iterate through all json files
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json'):
        # open and load the json file with explicit 'utf-8' encoding
        with open(os.path.join(json_folder_path, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)

# Check if 'type' is 'RGB'
        for image in data['images']:
            if image['type'] != 'RGB':
                image_filename = image['file_name']
                # If corresponding image file exists, remove it
                image_path = os.path.join(image_folder_path, image_filename)
                if os.path.exists(image_path):
                    os.remove(image_path)
                # Remove the json file
                os.remove(os.path.join(json_folder_path, filename))