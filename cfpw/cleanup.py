import pandas as pd

def clear_bg_faces(df_deep_features, df_ultraface): # clear background faces
    indexes = df_ultraface[(df_ultraface['FD_SCORE'] > 0.1) & (df_ultraface['UF_SCORE'] > 0.1)].index
    df_deep_features = df_deep_features.loc[indexes].reset_index(drop=True)
    df_ultraface = df_ultraface.loc[indexes].reset_index(drop=True)

    return df_deep_features, df_ultraface

if __name__ == '__main__':
    df_deep_features = pd.read_csv('./quick_test_deepfeatures.csv')
    df_ultraface = pd.read_csv('./quick_test_ultraface.csv')
    # get identity and file numbers for each face
    df_ultraface['identity'] = df_ultraface['FILENAME'].str.split('/').str[-3].astype(int)
    df_ultraface['file'] = df_ultraface['FILENAME'].str.split('/').str[-1]
    df_ultraface['file'] = df_ultraface['file'].str[:-4].astype(int)
    df_deep_features['identity'] = df_deep_features['FILE'].str.split('/').str[-3].astype(int)
    df_deep_features['file'] = df_deep_features['FILE'].str.split('/').str[-1]
    df_deep_features['file'] = df_deep_features['file'].str[:-4].astype(int)
    df_ultraface.drop(['FILENAME'], axis=1, inplace=True)
    df_deep_features.drop(['FILE'], axis=1, inplace=True)
    # sort identity and file numbers
    df_ultraface.sort_values(by=['identity', 'file'], inplace=True)
    df_deep_features.sort_values(by=['identity', 'file'], inplace=True)
    df_ultraface.reset_index(drop=True, inplace=True)
    df_deep_features.reset_index(drop=True, inplace=True)
    df_deep_features, df_ultraface = clear_bg_faces(df_deep_features, df_ultraface)
    df_ultraface.to_csv('./ultraface_cleanup.csv')
    df_deep_features.to_csv('./deep_features_cleanup.csv')