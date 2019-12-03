import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from os import listdir
from os.path import isfile, join
files_in_dir = [f for f in listdir('rendering_input/') if isfile(join('rendering_input/',f))]

pd_results = pd.read_csv('soccer-dataset/soccer_best_matches.csv')
pd_ultraface = pd.read_csv('soccer-dataset/soccer_ultraface.csv')

for file in files_in_dir:
    with open(file, 'w') as f:
        input_name = f.name
        image = Image.open('rendering_input/' + input_name)
        image_name = input_name.split('_')
        image_name = '/' + image_name[0] + '/' + image_name[1]
        pd_results_image = pd_results[pd_results['FILE'].str.contains(image_name)].reset_index(drop=True)
        pd_ultraface_image = pd_ultraface[pd_ultraface['FILE'].str.contains(image_name)].reset_index(drop=True)
        pd_face_coordinates = pd_ultraface_image[['FACE_X','FACE_Y']].reset_index(drop=True)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arialbd.ttf", 20)
        for i in range(len(pd_face_coordinates)):
            x = pd_face_coordinates.loc[i]['FACE_X']
            y = pd_face_coordinates.loc[i]['FACE_Y']
            name = pd_results_image.loc[i]['best_candidate']
            if name != 'No match':
                color = 'rgb(255, 255, 255)'
                draw.text((x, y), name, fill=color, font=font)
            image.save('rendering_output/' + input_name)
