import pandas as pd
import numpy as np

def normalize(gallery, dataset):
    # Normalize the deep features for vectors in the gallery and the dataset
    gallery[gallery.columns[:-1]] = gallery[gallery.columns[:-1]].div(gallery[gallery.columns[:-1]].sum(axis=1), axis=0)
    dataset[dataset.columns[:-2]] = dataset[dataset.columns[:-2]].div(dataset[dataset.columns[:-2]].sum(axis=1), axis=0)

    return gallery, dataset

def sort_candidates(gallery, query):
    # Sort candidates of the query based on the matching scores
    candidates = []
    for i in range(len(gallery)):
        candidate = gallery.loc[i].to_numpy()
        identity = gallery.loc[i, 'identity']
        # dot product of the normalized deep feature vectors
        candidates.append((np.dot(candidate[:-1], query[:-4]), identity))
    candidates.sort(reverse=True)
    return candidates

def find_position(arr, v):
    # Find the position of the query identity in the candidate list,
    # return -1 if the query identity isn't in the gallery
    for i in range(len(arr)):
        if arr[i][1] == v:
            return i
    return -1

def matching(gallery, dataset):
    # Find best matches and the position of query identities for every vector in the dataset
    dataset['best_match'] = 0
    dataset['query_id_position'] = 0
    for i in range(len(dataset)):
        query = dataset.loc[i].to_numpy()
        candidates = sort_candidates(gallery, query)
        dataset.loc[i, 'best_match'] = candidates[0][1]
        dataset.loc[i, 'query_id_position'] = find_position(candidates, dataset.loc[i, 'identity'])
    return dataset


if __name__ == '__main__':
    df_deep_features = pd.read_csv('soccer-dataset/soccer_deep_features_cleanup.csv', index_col=[0])
    gallery_deep_features = pd.read_csv('soccer-dataset/gallery_deep_features.csv', index_col=[0])
    gallery_deep_features, df_deep_features = normalize(gallery_deep_features, df_deep_features)
    df_deep_features = matching(gallery_deep_features, df_deep_features)
    df_deep_features.to_csv('soccer-dataset/matching.csv')