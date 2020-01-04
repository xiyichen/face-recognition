import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

def clear_bg_faces(df_deep_features, df_ultraface): # clear background faces
    indexes = df_ultraface[(df_ultraface['FD_SCORE'] > 0.1) & (df_ultraface['UF_SCORE'] > 0.1)].index
    df_deep_features = df_deep_features.loc[indexes].reset_index(drop=True)
    df_ultraface = df_ultraface.loc[indexes].reset_index(drop=True)

    return df_deep_features, df_ultraface

def build_gallery(df_deep_features, df_ultraface): # choose 2 perfect images for each person based on YAW, ROLL, PITCH
    identity_group = df_ultraface.groupby('identity')
    gallery_deep_features = pd.DataFrame(columns=df_deep_features.columns[:-1])
    gallery_ultraface = pd.DataFrame()
    for id, df_id in identity_group:
        # include 40 identities (80% of the dataset) in the gallery
        if id < 40 and id != 2 and id != 33 and id != 34:
            # drop files with more than one faces to ensure the accuracy of choosing the correct identity
            df_id = df_id.drop_duplicates(subset=['file'], keep=False)
            # get absolute values for YAW, ROLL, PITCH
            df_id['A'] = df_id['YAW'].abs()
            df_id['B'] = df_id['ROLL'].abs()
            df_id['C'] = df_id['PITCH'].abs()
            # sort by the sum of the absolute values
            df_id['D'] = df_id['A'] + df_id['B'] + df_id['C']
            df_id.sort_values(['D'], ascending=True, inplace=True)
            df_id.drop(['A', 'B', 'C', 'D'], axis=1, inplace=True)
            # select the smallest two sums as the "perfect image" to put into the gallery
            perfect_images_ultraface = df_id.head(2)
            gallery_ultraface = gallery_ultraface.append(perfect_images_ultraface)
            # get the deep features of these two faces
            perfect_images_deep_features = df_deep_features.loc[perfect_images_ultraface.index].drop(['file'], axis=1)
            # compute the average and put into the gallery
            perfect_images_deep_features = np.mean(perfect_images_deep_features, axis=0)
            gallery_deep_features = gallery_deep_features.append(perfect_images_deep_features, ignore_index=True)
        # for the following three identities, the method above was not able to give the correct gallery faces, so I selected manually.
        if id == 2:
            perfect_images_ultraface = df_id[(df_id['file'] == 43) | (df_id['file'] == 53)]
            gallery_ultraface = gallery_ultraface.append(perfect_images_ultraface)
            perfect_images_deep_features = df_deep_features.loc[perfect_images_ultraface.index].drop(['file'], axis=1)
            perfect_images_deep_features = np.mean(perfect_images_deep_features, axis=0)
            gallery_deep_features = gallery_deep_features.append(perfect_images_deep_features, ignore_index=True)
        if id == 33:
            perfect_images_ultraface = df_id[(df_id['file'] == 4) | (df_id['file'] == 54)]
            gallery_ultraface = gallery_ultraface.append(perfect_images_ultraface)
            perfect_images_deep_features = df_deep_features.loc[perfect_images_ultraface.index].drop(['file'], axis=1)
            perfect_images_deep_features = np.mean(perfect_images_deep_features, axis=0)
            gallery_deep_features = gallery_deep_features.append(perfect_images_deep_features, ignore_index=True)
        if id == 34:
            perfect_images_ultraface = df_id[(df_id['file'] == 22) | (df_id['file'] == 54)]
            gallery_ultraface = gallery_ultraface.append(perfect_images_ultraface)
            perfect_images_deep_features = df_deep_features.loc[perfect_images_ultraface.index].drop(['file'], axis=1)
            perfect_images_deep_features = np.mean(perfect_images_deep_features, axis=0)
            gallery_deep_features = gallery_deep_features.append(perfect_images_deep_features, ignore_index=True)
    gallery_ultraface.reset_index(drop=True, inplace=True)
    gallery_deep_features['identity'].astype(int)

    return gallery_deep_features, gallery_ultraface

if __name__ == '__main__':
    df_deep_features = pd.read_csv('soccer-dataset/soccer_deep_features_cleanup.csv', index_col=[0])
    df_ultraface = pd.read_csv('soccer-dataset/soccer_ultraface_cleanup.csv', index_col=[0])
    df_deep_features, df_ultraface = clear_bg_faces(df_deep_features, df_ultraface)
    gallery_deep_features, gallery_ultraface = build_gallery(df_deep_features, df_ultraface)
    gallery_ultraface.to_csv('soccer-dataset/gallery_ultraface.csv')
    gallery_deep_features.to_csv('soccer-dataset/gallery_deep_features.csv')
