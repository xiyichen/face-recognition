import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

def clear_bg_faces(df_deep_features, df_ultraface): # clear background faces
    indexes = df_ultraface[(df_ultraface['FD_SCORE'] > 0.1) & (df_ultraface['UF_SCORE'] > 0.1)].index
    df_deep_features = df_deep_features.loc[indexes].reset_index(drop=True)
    df_ultraface = df_ultraface.loc[indexes].reset_index(drop=True)

    return df_deep_features, df_ultraface

def build_gallery(df_deep_feature, df_ultraface): # choose 2 perfect images for each person based on YAW, ROLL, PITCH
    identity_group = df_ultraface.groupby('identity')
    gallery_deep_features = pd.DataFrame()
    gallery_ultraface = pd.DataFrame()
    for id, df_id in identity_group:
        if id < 40:
            # sort ascendingly by the absolute value of YAW, ROLL, PITCH
            df_id = df_id.drop_duplicates(subset=['file'], keep=False)
            df_id['A'] = df_id['YAW'].abs()
            df_id['B'] = df_id['ROLL'].abs()
            df_id['C'] = df_id['PITCH'].abs()
            df_id['D'] = df_id['A'] + df_id['B'] + df_id['C']
            df_id.sort_values(['D'], ascending=True, inplace=True)
            df_id.drop(['A', 'B', 'C', 'D'], axis=1, inplace=True)
            perfect_images_ultraface = df_id.head(2).drop(['FILE'], axis=1)
            perfect_images_deep_features = df_deep_feature.loc[df_id.head(2).index].drop(['FILE', 'file'], axis=1)
            perfect_images_deep_features = np.mean(perfect_images_deep_features, axis=0)
            gallery_ultraface = gallery_ultraface.append(perfect_images_ultraface)
            gallery_deep_features = gallery_deep_features.append(perfect_images_deep_features, ignore_index=True)
    gallery_ultraface.reset_index(drop=True, inplace=True)
    gallery_deep_features['identity'].astype(int)

    return gallery_deep_features, gallery_ultraface

if __name__ == '__main__':
    df_deep_features = pd.read_csv('soccer-dataset/soccer_deep_features_cleanup.csv').drop(['Unnamed: 0'], axis=1)
    df_ultraface = pd.read_csv('soccer-dataset/soccer_ultraface_cleanup.csv').drop(['Unnamed: 0'], axis=1)
    df_deep_features, df_ultraface = clear_bg_faces(df_deep_features, df_ultraface)
    gallery_deep_features, gallery_ultraface = build_gallery(df_deep_features, df_ultraface)
    gallery_ultraface.to_csv('soccer-dataset/gallery_ultraface.csv')
    gallery_deep_features.to_csv('soccer-dataset/gallery_deep_features.csv')
