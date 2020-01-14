import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageFont
import pandas as pd

def resize(image, maxwidth): # resize the image to fit the canvas window
    w = image.size[0]
    h = image.size[1]
    ratio = w/h
    newsize = (maxwidth, int(maxwidth/ratio))
    image = image.resize(newsize, Image.ANTIALIAS)
    return image

def delete(rowindex, root): # command for the delete button
    # remove this face in two dataframes
    df_ultraface.drop([rowindex], inplace=True)
    df_deep_features.drop([rowindex], inplace=True)
    root.destroy()

def render_canvas(id, file, x, y, rowindex): # render GUI canvas for the current face
    root = tk.Tk()
    image = Image.open("soccer-dataset/" + str(id) + "/" + str(file) + ".jpg")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arialbd.ttf", 30)
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), "Face Locator", fill=color, font=font)
    image = resize(image, 800)
    renderimage = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=renderimage)
    label.pack()
    canvas = tk.Canvas(root, width=800, height=100)
    canvas.pack()
    # delete button
    button1 = tk.Button(root, text='delete', command=lambda: delete(rowindex, root))
    button1.pack()
    canvas.create_window(200, 50, window=button1)
    # continue button
    button2 = tk.Button(root, text='continue', command=lambda: root.destroy())
    button2.pack()
    canvas.create_window(600, 50, window=button2)
    root.mainloop()

if __name__ == '__main__':
    df_ultraface = pd.read_csv('soccer-dataset/soccer_ultraface_cleanup.csv', index_col=[0])
    df_deep_features = pd.read_csv('soccer-dataset/soccer_deep_features_cleanup.csv', index_col=[0])
    for i in range(len(df_deep_features)):
        identity = int(df_deep_features.loc[i]["identity"])
        file = int(df_deep_features.loc[i]["file"])
        x = df_ultraface.loc[i]['FACE_X']
        y = df_ultraface.loc[i]['FACE_Y']
        delete_flag = False
        render_canvas(identity, file, x, y, i)
    df_ultraface.reset_index(drop=True, inplace=True)
    df_deep_features.reset_index(drop=True, inplace=True)
    # save the cleaned up dataframes
    df_ultraface.to_csv('soccer-dataset/soccer_ultraface_selected.csv')
    df_deep_features.to_csv('soccer-dataset/soccer_deep_features_selected.csv')