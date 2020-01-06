import pandas as pd

if __name__ == '__main__':
    df_deep_features = pd.read_csv('soccer-dataset/soccer_deep_features.csv')
    df_ultraface = pd.read_csv('soccer-dataset/soccer_ultraface.csv')
    # get identity and file numbers for each face
    df_ultraface['identity'] = df_ultraface['FILE'].str.split('/').str[5].astype(int)
    df_ultraface['file'] = df_ultraface['FILE'].str.split('/').str[6]
    df_ultraface['file'] = df_ultraface['file'].str[:-4].astype(int)
    df_deep_features['identity'] = df_deep_features['FILE'].str.split('/').str[5].astype(int)
    df_deep_features['file'] = df_deep_features['FILE'].str.split('/').str[6]
    df_deep_features['file'] = df_deep_features['file'].str[:-4].astype(int)
    # remove the wrong images
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 1) & (df_ultraface['file'] > 76))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 2) & (df_ultraface['file'] > 85))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 6) & (df_ultraface['file'] > 76))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 12) & (df_ultraface['file'] > 72))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 14) & (df_ultraface['file'] > 77))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 18) & (df_ultraface['file'] > 73))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 20) & (df_ultraface['file'] > 74))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 25) & (df_ultraface['file'] > 67))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 31) & (df_ultraface['file'] > 78))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 36) & (df_ultraface['file'] > 71))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 38) & (df_ultraface['file'] > 73))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 39) & (df_ultraface['file'] > 67))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 41) & (df_ultraface['file'] > 75))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 45) & (df_ultraface['file'] > 80))]
    df_ultraface = df_ultraface[~((df_ultraface['identity'] == 47) & (df_ultraface['file'] > 75))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 1) & (df_deep_features['file'] > 76))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 2) & (df_deep_features['file'] > 85))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 6) & (df_deep_features['file'] > 76))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 12) & (df_deep_features['file'] > 72))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 14) & (df_deep_features['file'] > 77))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 18) & (df_deep_features['file'] > 73))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 20) & (df_deep_features['file'] > 74))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 25) & (df_deep_features['file'] > 67))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 31) & (df_deep_features['file'] > 78))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 36) & (df_deep_features['file'] > 71))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 38) & (df_deep_features['file'] > 73))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 39) & (df_deep_features['file'] > 67))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 41) & (df_deep_features['file'] > 75))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 45) & (df_deep_features['file'] > 80))]
    df_deep_features = df_deep_features[~((df_deep_features['identity'] == 47) & (df_deep_features['file'] > 75))]
    df_ultraface.drop(['FILE'], axis=1, inplace=True)
    df_deep_features.drop(['FILE'], axis=1, inplace=True)
    df_ultraface['file'].astype(int)
    # sort identity and file numbers
    df_ultraface.sort_values(by=['identity', 'file'], inplace=True)
    df_deep_features['file'].astype(int)
    df_deep_features.sort_values(by=['identity', 'file'], inplace=True)
    df_ultraface.reset_index(drop=True, inplace=True)
    df_deep_features.reset_index(drop=True, inplace=True)
    df_ultraface.to_csv('soccer-dataset/soccer_ultraface_cleanup.csv')
    df_deep_features.to_csv('soccer-dataset/soccer_deep_features_cleanup.csv')