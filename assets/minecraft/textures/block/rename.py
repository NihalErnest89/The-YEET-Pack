import os

folder_path = os.path.dirname(os.getcwd()+'/block')
for filename in os.listdir(folder_path):
    if filename.startswith('wool_colored_'):
        color_name = filename.split('_')[2]  # extracts color name (e.g., blue, pink)
        color_name = color_name.replace(".png", "")
        new_filename = f"{color_name}_wool.png"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))