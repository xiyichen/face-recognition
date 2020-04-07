import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

def build_gallery(df_deep_features, df_ultraface): # choose 2 perfect images for each person based on YAW, ROLL, PITCH
    identity_group = df_ultraface.groupby('identity')
    gallery_deep_features = pd.DataFrame(columns=df_deep_features.columns[:-1])
    gallery_ultraface = pd.DataFrame()
    for id, df_id in identity_group:
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
    gallery_ultraface.reset_index(drop=True, inplace=True)
    gallery_deep_features['identity'].astype(int)

    return gallery_deep_features, gallery_ultraface

if __name__ == '__main__':
    df_deep_features = pd.read_csv('./deep_features_cleanup.csv', index_col=[0])
    df_ultraface = pd.read_csv('./ultraface_cleanup.csv', index_col=[0])
    gallery_deep_features, gallery_ultraface = build_gallery(df_deep_features, df_ultraface)
    gallery_ultraface.to_csv('./gallery_ultraface.csv')
    gallery_deep_features.to_csv('./gallery_deep_features.csv')
