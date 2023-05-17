import os
import pandas as pd
from PIL import Image

logo_folder = 'logos'
target_size = (70, 70) 
output = 'output'

data = []
for root, dirs, files in os.walk(logo_folder):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust the file extensions based on your logo image format
            logo_path = os.path.join(root, filename)
            brand_name = root.replace('logos\\', '')
            image = Image.open(logo_path).convert('RGB')
            # Resize the image
            resized_image = image.resize(target_size)

            brand_folder = os.path.join(output, brand_name)
            if not os.path.exists(os.path.join(output, brand_name)):
                os.makedirs(os.path.join(output, brand_name))

            # Save the resized image to the output folder
            output_path = os.path.join(brand_folder, filename)
            resized_image.save(output_path)
            
            data.append({'Filename': os.path.join(brand_folder, filename), 'Brand Name': brand_name, 'Label': 'Genuine'})

df = pd.DataFrame(data)
df.to_csv('file_map.csv')

print("Done")
