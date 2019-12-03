import pandas as pd
import numpy as np

print('reading dataframes')
deep_features = pd.read_csv('soccer-dataset/soccer_deep_features.csv')
query_deep_features = deep_features
ultraface = pd.read_csv('soccer-dataset/soccer_ultraface.csv')
gallery_files = open("soccer-dataset/gallery.txt","r")
identities = pd.read_csv('soccer-dataset/soccer_identities.csv')

print('building gallery')
gallery_features = pd.DataFrame()
gallery_ultraface = pd.DataFrame()
for line in gallery_files:
    line = line[:len(line)-1]
    gallery_features = gallery_features.append(deep_features[deep_features['FILE'].str.contains(line)])
    gallery_ultraface = gallery_ultraface.append(ultraface[ultraface['FILE'].str.contains(line)])
gallery_features = gallery_features.reset_index(drop=True)
gallery_ultraface = gallery_ultraface.reset_index(drop=True)

def find_identity(v):
    identityindex = int(v.split('/')[5])
    return identities.loc[identityindex, 'NAME']

def find_candidates(query):
    candidates = []
    for i in range(len(gallery_features)):
        candidate = gallery_features.loc[i].to_numpy()
        identity = find_identity(candidate[0])
        candidates.append((np.dot(candidate[1:], query), identity))
    candidates.sort(reverse=True)
    return candidates

print('processing faces')
best_matches = query_deep_features[['FILE']].copy()
for i in range(len(query_deep_features)):
    query = query_deep_features.loc[i].to_numpy()[1:]
    best_candidate = find_candidates(query)[0]
    #thresholding
    if best_candidate[0] < 1310:
        best_matches.loc[i, 'best_candidate'] = 'No match'
        best_matches.loc[i, 'best_candidate_score'] = best_candidate[0]
    else:
        best_matches.loc[i, 'best_candidate'] = best_candidate[1]
        best_matches.loc[i, 'best_candidate_score'] = best_candidate[0]

best_matches.to_csv('soccer-dataset/soccer_best_matches.csv')
