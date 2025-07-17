import os
import shutil
from tqdm import tqdm  # Make sure to install tqdm if you haven't already

source_dir = r'C:\Users\anura\OneDrive\Desktop\Machine Learning\GEN\DCGAN\anime_images'
destination_dir = r'C:\Users\anura\OneDrive\Desktop\Machine Learning\GEN\DCGAN\all_images'

# Create destination folder if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Count total files for tqdm
all_files = []
for root, dirs, files in os.walk(source_dir):
    for file in files:
        all_files.append(os.path.join(root, file))

for file_path in tqdm(all_files, desc="Moving images"):
    file = os.path.basename(file_path)
    dest_path = os.path.join(destination_dir, file)
    
    # Handle file name conflicts by appending a counter
    counter = 1
    while os.path.exists(dest_path):
        base, ext = os.path.splitext(file)
        dest_path = os.path.join(destination_dir, f"{base}_{counter}{ext}")
        counter += 1

    shutil.copy2(file_path, dest_path)

print("✅ All images have been moved successfully.")